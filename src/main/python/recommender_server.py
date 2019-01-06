from flask import Flask
from flask import request
from flask import jsonify
import news_articles_processor as nap


app = Flask(__name__)


@app.route("/", methods=["GET"])
@app.route("/status", methods=['GET'])
def server_status():
    return "Welcome to Recommender server.The server is running"


@app.route("/rec_articles", methods=['GET'])
def recommended_articles():
    input_url = request.args.get("url", type=str)
    top_3_match_articles = nap.get_top_3_articles(str(input_url))
    return jsonify(top_3_match_articles)


if __name__ == '__main__':
    #port = 8080
    app.run()





