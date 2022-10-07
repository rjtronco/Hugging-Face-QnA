import flask
import json
import os
from flask import send_from_directory, request


# Flask app should start in global layout
app = flask.Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/favicon.png')

@app.route('/')
@app.route('/home')
def home():
    return "Hello World"

@app.route('/webhook', methods=['POST'])
def webhook():
    query = request.get_json(force=True)

    queryText = str(query['queryResult']['queryText'])
    print(queryText)
    print("haha")

    if "bye" in queryText:
        return {
        'fulfillmentText': 'Bye ka rin!'
    }

    return {
        'fulfillmentText': 'Hello from the bot world supot!'
    }

if __name__ == "__main__":
    app.secret_key = 'ItIsASecret'
    app.debug = True
    app.run()