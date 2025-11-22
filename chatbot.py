from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    user_query = req.get("queryResult").get("queryText")

    # Simple response (You will improve later)
    response_text = f"You asked: {user_query}. I will help you!"
    
    return jsonify({"fulfillmentText": response_text})

@app.route('/')
def hello():
    return "Dialogflow Webhook Running!"

if __name__ == '__main__':
    app.run(debug=True)