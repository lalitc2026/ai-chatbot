
from flask import Flask, request, jsonify
from chatbot import ChatBot

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/chat', methods=['GET'])
def chat():
    #data = request.get_json(silent=True) or {}
    #user_message = data.get("message", "")

    user_message = "I want 3 day itinerary for Mysuru, budget friendly hotels and advice on the best time to visit and available mode of transportation." 
    # For testing purpose, you can replace this with dynamic input from the request body as shown above.

    print(f"User: {user_message}")

    if not user_message:
        return jsonify({"error": "validation_error", "message": "'message' is required."}), 400

    response_message = chatbot.chat(user_message)

    #print(f"ChatBot: {response}")   

    return jsonify({"message": response_message})    


if __name__ == "__main__":
    chatbot = ChatBot("Travel Assistant")
    app.run(host='0.0.0.0', port=8080)