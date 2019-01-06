from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"])
@app.route("/status", methods=['GET'])
def server_status():
    return "Welcome to Recommender server.The server is running"


if __name__ == '__main__':
    #port = 8080
    app.run()





