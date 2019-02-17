import nltk
import requests
import json
from bs4 import BeautifulSoup
import re
import os

# Download relevant NLTK data
#from source.news_articles_processor import get_parts_of_speech

nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')

dirname = os.path.dirname(__file__)
url_path = os.path.join(dirname, 'article_data.json')


def get_article_content(url):
    read_content = requests.get(url)
    content = read_content.text
    text = remove_spec_char(content)
    return text


def get_parsed_text(text):
    soup = BeautifulSoup(text, 'html.parser')
    text = get_clean_text(soup)

    def remove_special_char():
        cleaned_text = re.sub('[^a-zA-Z0-9-_.]', ' ', text)
        return cleaned_text
    return remove_special_char


remove_spec_char = get_parsed_text()
remove_spec_char()

# #regular expression as a DSL
# def remove_special_char(text):
#     cleaned_text = re.sub('[^a-zA-Z0-9-_.]', ' ', text)
#     return cleaned_text


def get_clean_text(soup):
    for script in soup(["script", "style"]):
        script.decompose()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)
    return text


def get_tokens(text):
    text_tokens = nltk.tokenize.word_tokenize(text)
    return text_tokens


def get_parts_of_speech(tokens_list):
        tagged = nltk.pos_tag(tokens_list)
        return tagged


def get_nouns(tagged):
    token = tagged[0]
    tag_token = tagged[1]
    if tag_token in ["NN", "NNS", "NNP", "NNPS"]:
        return token


def get_common_words(list_one, list_two):

    common_words = [value for value in list_two if value in list_one]
    return common_words


def write_article_to_json(articles_list):
    for url in articles_list:
        text = get_article_content(url)
        list_tokens = get_tokens(text)
        list_pos = get_parts_of_speech(list_tokens)
        list_nouns = list(map(get_nouns, list_pos))
        dict_data = {
            "url": url,
            "text": text,
            "tokens": list_tokens,
            "pos": list_pos,
            "nouns": list_nouns
        }

        try:
            with open(url_path) as f:
                data = json.load(f)
                dict_data["id"] = data["counter"]
                data["data"].append(dict_data)
                data["counter"] = data["counter"] + 1

            with open(url_path, 'w') as outfile:
                json.dump(data, outfile, indent=4)
        except ValueError:
            dict_data = {
                "counter": 1,
                "data": [
                    dict_data
                ]
            }
            with open(url_path, 'w') as outfile:
                json.dump(dict_data, outfile, indent=4)


def read_article_from_json():
    content = {}
    try:
        with open(url_path) as f:
            content = json.load(f)
            content = content['data']
    except ValueError:
        print("File is empty")
    return content


def get_article_by_url(article_list, url):
    try:
        url_found = next(item for item in article_list if item["url"] == url)
    except StopIteration:
        write_article_to_json([url])
        article_list = read_article_from_json()
        url_found = next(item for item in article_list if item["url"] == url)
    return url_found


def sort_by_value(tosort_dict):
    return sorted(tosort_dict.items(), key=lambda x: x[1])


def get_top_3_articles(url):
    article_list_from_json = read_article_from_json()
    text = get_article_content(url)
    list_tokens = get_tokens(text)
    list_pos = get_parts_of_speech(list_tokens)
    list_nouns = list(map(get_nouns, list_pos))
    common_words_dict = {}
    for article in article_list_from_json:
        common_words = get_common_words(
            article['nouns'],
            list_nouns
        )
        common_words_dict[article['url']] = len(common_words)
    sorted_dict = sort_by_value(common_words_dict)
    top_3_match = sorted_dict[-3:]
    top_3_match = list(reversed(top_3_match))
    return top_3_match


