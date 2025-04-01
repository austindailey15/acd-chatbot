from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Chatbot is running!"

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    bot_response = f"You said: {user_message}"  # Simple echo bot
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
