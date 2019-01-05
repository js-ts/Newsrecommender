import news_articles_processor as nap


input_url = raw_input("Enter url:")
top_3_match_articles = nap.get_top_3_articles(str(input_url))
print(top_3_match_articles)
