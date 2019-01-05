import news_articles_processor as nap

# # write articles from following url list to content.json 
articles_list = [
    "https://www.bbc.com/sport/football/46386440",
    "https://www.bbc.com/sport/football/46335948",
    "https://www.bbc.com/sport/football/46366274",
    "https://www.bbc.com/sport/live/football/45685103",
    "https://www.bbc.co.uk/programmes/p06t6jsz",
    "https://www.bbc.com/sport/football/46379846",
    "https://www.bbc.com/sport/football/46390437",
    "https://www.bbc.com/sport/football/46379846",
    "https://www.bbc.com/sport/football/46378014",
    "https://www.bbc.com/sport/cricket/46385163",
    "https://www.bbc.com/sport/cricket/46374261",
    "https://www.bbc.co.uk/programmes/p06ssdx4",
    "https://www.bbc.co.uk/programmes/w3cswngn",
    "https://www.bbc.com/sport/cricket/18427186",
    "https://www.dawn.com/news/1448238/clarrie-who-yasir-eyes-australian-legends-record",
    "https://www.dawn.com/news/1448076/5-takeaways-from-new-zealand-versus-yasir-shah",
    "https://www.dawn.com/news/1448015/comment-test-series-set-for-a-grand-finale",
    "https://www.dawn.com/news/1448233/clarke-katich-clash-over-aussie-non-aggression-pact",
    "https://www.bbc.com/news/world-europe-46386160",
    "https://www.bbc.com/news/world-us-canada-46390368",
    "https://www.bbc.com/news/business-46381897",
    "https://www.bbc.com/news/world-us-canada-46376807",
    "https://www.bbc.com/news/world-us-canada-46377563",
    "https://www.bbc.com/news/world-us-canada-40138733",
    "https://www.bbc.com/news/world-us-canada-46283775",
    "https://www.bbc.com/news/business-46344113",
    "https://www.bbc.com/news/uk-politics-46384207",
    "https://www.bbc.com/news/uk-england-sussex-46391287",
    "https://www.dawn.com/news/1448848/west-indies-crash-in-spin-trial-after-mahmudullah-hits-ton",
    "https://www.dawn.com/news/1448652/pcb-invites-interested-bidders-for-sale-of-sixth-psl-team",
    "https://www.dawn.com/news/1448636/kohli-backing-gives-gower-hope-for-test-crickets-future",
    "https://www.dawn.com/news/1448889/mbs-trump-and-some-crude-realities",
    "https://www.dawn.com/news/1448812/us-to-keep-aiding-saudis-in-yemen-despite-furore-pompeo"
]

nap.write_article_to_json(articles_list)
