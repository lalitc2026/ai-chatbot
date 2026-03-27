from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.messages import HumanMessage

class ChatBot:
    def __init__(self, name):
        self.name = name
        system_prompt = "You are a professional and knowledgeable Travel Assistance AI agent. "
        "Your goal is to help users plan trips, discover destinations, and manage travel logistics. "
        "Response Formatting: Use proper HTML tags like <h3>, <ul>, <li>, <strong>, and <p>. "
        "Scope & Restrictions: Only answer questions related to destinations, logistics, "
        "planning, and local knowledge. If the question is unrelated, answer exactly with: "
        "'Sorry, I can only answer questions related to travel planning, destinations, and trip logistics.'"
        self.model =init_chat_model(
                    model="gpt-5-nano",
                    # Kwargs passed to the model:
                    temperature=1.0
            )
        self.agent = create_agent(model=self.model, system_prompt=system_prompt)

    #Test Function
    def greet(self):
        return f"Hello! I am {self.name}, your friendly chatbot. How can I assist you today?"
    #Test Function
    def respond(self, user_input):
        # This is a simple response mechanism. You can expand this with more complex logic.
        if "how are you" in user_input.lower():
            return "I'm just a bunch of code, but I'm doing great! Thanks for asking."
        elif "what is your name" in user_input.lower():
            return f"My name is {self.name}."
        else:
            return "I'm not sure how to respond to that. Can you please rephrase?"
        
    def chat(self, user_input):
        # This method can be expanded to integrate with a language model for more dynamic responses.
        
        response = self.agent.invoke({"messages": [HumanMessage(content=user_input)]})

        print(response.messages[-1].content)
        
        return response.messages[-1].content