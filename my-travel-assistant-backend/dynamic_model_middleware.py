from langchain.agents.middleware import ModelRequest, ModelResponse, wrap_model_call
from typing import Callable
from langchain_aws import ChatBedrock

class DynamicModelMiddleware:

    
    aws_llm_large_model = ChatBedrock(model="apac.amazon.nova-lite-v1:0", region="ap-south-1")
    aws_llm_standard_model = ChatBedrock(model="apac.amazon.nova-micro-v1:0", region="ap-south-1")

    @staticmethod
    @wrap_model_call
    def state_based_model(request: ModelRequest, 
        handler: Callable[[ModelRequest], ModelResponse]) -> ModelResponse:
        """Select model based on State conversation length."""
        # request.messages is a shortcut for request.state["messages"]
        message_count = len(request.messages)  
        print(f"message count = {message_count}")
        if message_count > 5:
            # Long conversation - use model with larger context window
            model = DynamicModelMiddleware.aws_llm_large_model
            print(f"large model")
        else:
            # Short conversation - use efficient model
            print(f"small model")
            model = DynamicModelMiddleware.aws_llm_standard_model

        request = request.override(model=model, system_message=request.system_message)   #Ensures the system prompt message is not overriden

        return handler(request)