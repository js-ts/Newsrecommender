import nltk
import requests
import re
import json
from bs4 import BeautifulSoup


# Download relevant NLTK data
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')


def get_article_content(url):
    read_content = requests.get(url)
    content = read_content.text
    text = get_parsed_text(content)
    return text


def get_parsed_text(text):
    soup = BeautifulSoup(text, 'html.parser')
    text = get_remove_text(soup)
    return text



def get_remove_text(soup):
    for script in soup(["script", "style"]):
        script.decompose()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)
    return text


def get_tokens(text):
	text_tokens = nltk.tokenize.word_tokenize(text)		
#	return text_tokens
	def get_parts_of_speech():
		pos_tagged = nltk.pos_tag(text_tokens)
		return pos_tagged
	return get_parts_of_speech


#def get_parts_of_speech(tokens_list):
#	tagged = nltk.pos_tag(tokens_list)
	#pos_tagged = list(map(get_parts_of_speach, tagged))
#	return tagged

def get_nouns(tagged):
	#tagged = nltk.pos_tag(text_tokens)
	#tagged = get_part_of_speach(text_token)
	list_noun_tokens = []
	 
	for token, tag_token in tagged:
	    if tag_token in ["NN", "NNS", "NNP", "NNPS"]:
	        list_noun_tokens.append(token)
	return list_noun_tokens

def get_common_words(list_one, list_two):
    common_words = [value for value in list_two if value in list_one]
    return common_words


def write_article_to_json(articles_list):
    for url in articles_list:
        text = get_article_content(url)
        list_tokens = get_tokens(text)
        list_pos = get_parts_of_speach(list_tokens)
        list_nouns = get_nouns(list_tokens)
        dict_data = {
            "url": url,
            "text": text,
            "tokens": list_tokens,
            "pos": list_pos,
            "nouns": list_nouns
        }

        try:
            with open('article_data.json') as f:
                data = json.load(f)
                dict_data["id"] = data["counter"]
                data["data"].append(dict_data)
                data["counter"] = data["counter"] + 1

            with open('article_data.json', 'w') as outfile:
                json.dump(data, outfile, indent=4)
        except ValueError:
            dict_data = {
                "counter": 1,
                "data": [
                    dict_data
                ]
            }
            with open('article_data.json', 'w') as outfile:
                json.dump(dict_data, outfile, indent=4)



def read_article_from_json():
    content = {}
    try:
        with open('article_data.json') as f:
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
	pos_function = get_tokens(text)
	list_of_pos = pos_function() 
	list_nouns = get_nouns(list_of_pos)
	common_words_dict = {}
	for article in article_list_from_json:
		common_words = get_common_words(
			article['nouns'], 
			list_nouns
		)
		common_words_dict[ article['url'] ] = len(common_words)
	sorted_dict = sort_by_value(common_words_dict)
	top_3_match = sorted_dict[-3:]
	top_3_match = list(reversed(top_3_match))
	return top_3_match


if __name__ == '__main__':
	pos_tags = get_tokens('khan is angry because little Khan can not remember things from 5 minutes earlier.')
	print(pos_tags())
