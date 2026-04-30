
from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot import ChatBot

app = Flask(__name__)

# Allow only your Angular application
CORS(app, origins=["http://localhost:4200"]) 



@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/chat', methods=['POST'])
def chat():

    data = request.get_json(silent=True) or {}
    
    user_message = data.get("query", "")
    user_id = data.get("userId", "")
    
    print("user_id:", user_id)
    print(f"User: {user_message}")
    
    # For testing purpose, you can replace this with dynamic input from the request body as shown above.  

    if not user_message:
        return jsonify({"error": "validation_error", "message": "'message' is required."}), 400

    try:
        # Default response object when chatbot.chat is not available
        response_message = {
            "answer": "Server cannot process your request at the moment.",
            "response": "Server cannot process your request at the moment."
        }
        response_message = chatbot.chat(user_message, user_id)  

    except Exception as e:
        print(f"Error: {e}")
        response_message = {
            "answer": "Server cannot process your request at the moment.",
            "response": "Server cannot process your request at the moment."
        }

    print(f"Final Response: {response_message}")
    return jsonify(response_message)    


if __name__ == "__main__":
    chatbot = ChatBot("Travel Assistant")
    app.run(host='0.0.0.0', port=8080)