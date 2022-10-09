import flask
import json
import os
from flask import send_from_directory, request
import random

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
    print("Reached!")
    sample_return_messages = {
        "bye":['bye ka rin!','k bye!'],
        "supot":["supot ka ba?","baka ikaw supot?","kausap ko supot. haha"],
        "mama":["your mom!","mama mo"],
        "ha":["hakdog","hakdog ka"]
    }

    queryText = str(query['queryResult']['queryText'])

    explode_str = queryText.split(" ")

    for i in explode_str:
        if i in sample_return_messages:
            # randomize from list what to return
            rand_index = random.randint(0,len(sample_return_messages[i])-1)
            message = sample_return_messages[i][rand_index]
            return {
                'fulfillmentText': message
            }


    return {
        'fulfillmentText': 'Hello from the bot world supot!'
    }

if __name__ == "__main__":
    app.secret_key = 'ItIsASecret'
    app.debug = True
    app.run()
