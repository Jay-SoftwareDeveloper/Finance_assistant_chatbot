from flask import Flask, render_template, request, jsonify
from chatbot import parse_expense
from kafka_producer import send_to_kafka

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    parsed_data = parse_expense(user_input)
    if parsed_data:
        send_to_kafka(parsed_data)
        response = f"Got it! Added {parsed_data['amount']} for {parsed_data['category']} on {parsed_data['date']}"
    else:
        response = "Sorry, I couldn't understand that. Try something like 'Add $20 for food today'"
    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)