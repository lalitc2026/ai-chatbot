from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langchain_aws import ChatBedrock
from langgraph.checkpoint.memory import MemorySaver

class ChatBot:
    def __init__(self, name):
        self.name = name

        checkpointer = MemorySaver()

        system_prompt = """You are a professional and knowledgeable Travel Assistance AI agent.
        Your goal is to help users plan trips, discover destinations, and manage travel logistics.
        I will be printing the answer in HTML page so include proper formatting in the response as well without
        any additional metadata and HTML title block as I will be printing whole response in HTML. 
        I have setup a chatbot in my HTML
        Scope & Restrictions: Only answer questions related to destinations, logistics,
        planning, and local knowledge. If the question is unrelated, answer exactly with:
        'Sorry, I can only answer questions related to travel planning, destinations, and trip logistics.'"""
        
        # self.model =init_chat_model(
        #              model="amazon.nova-lite-v1:0",
        #              model_provider="bedrock_converse",
        #              region_name="ap-south-1",
        #              max_tokens=1024,
        #              temperature=1.0,
        #              checkpointer=checkpointer
        #     )
        aws_llm = ChatBedrock(model="apac.amazon.nova-micro-v1:0", region="ap-south-1")

        #self.agent = create_agent(model=self.model, system_prompt=system_prompt)
        self.agent = create_agent(aws_llm, system_prompt=system_prompt, checkpointer=checkpointer)

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
        
    def chat(self, user_input: str, user_id: str):
        # This method can be expanded to integrate with a language model for more dynamic responses.
        print(f"User input to chat method: {user_input}")
        print(f"User ID: {user_id}")

    
        config = {"configurable": {"thread_id": user_id}}
        response = self.agent.invoke({
            "messages": [HumanMessage(content=user_input)]
        },
        config=config)

        # print("Agent Response:", response)
        print(f"\n\nFull Response Object: {response}\n\n")
        print(response["messages"][-1].content)
        
        return response["messages"][-1].content