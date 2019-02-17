from flask import Flask
from flask import request
from flask import jsonify
import news_articles_processor as nap


app = Flask(__name__)

@app.route("/", methods=['GET'])
def recommended_articles_get():
    recommended_articles = """
        <h2>News recommender system</h2>
        <form method="POST" action="/rec_articles">
            <label>Enter your url</label>
            <input type='text' name='url'>
            <input type='submit'>
        </form>
    """

    return recommended_articles

@app.route("/rec_articles", methods=['POST'])
def recommended_articles_post():
    input_url = request.form["url"]
    print(input_url)
    top_3_match_articles = nap.get_top_3_articles(str(input_url))
#    return jsonify(top_3_match_articles)

    recommended_articles = """
        <h2> Your top3 article are:</h2>
        <ul>
            <li>
                <a href='""" + top_3_match_articles[0][0] + """'>First recommended article</a>
            </li>
            <li>
                <a href='""" + top_3_match_articles[1][0] + """'>Second recommended article</a>
            </li>
            <li>
                <a href='""" + top_3_match_articles[2][0] + """'>Third recommended article</a>
            </li>
        </ul>
    """

    return recommended_articles


if __name__ == '__main__':
    #port = 8080
    app.run()






