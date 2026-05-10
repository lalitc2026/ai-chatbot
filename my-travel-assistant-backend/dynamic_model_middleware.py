from langchain.agents.middleware import ModelRequest, ModelResponse, wrap_model_call
from typing import Callable
from langchain_aws import ChatBedrock

class DynamicModelMiddleware:

    def __init__(self):
        self.aws_llm_large_model = ChatBedrock(model="apac.amazon.nova-lite-v1:0", region="ap-south-1")
        self.aws_llm_standard_model = ChatBedrock(model="apac.amazon.nova-micro-v1:0", region="ap-south-1")

    @wrap_model_call
    def state_based_model(self, request: ModelRequest, 
        handler: Callable[[ModelRequest], ModelResponse]) -> ModelResponse:
        """Select model based on State conversation length."""
        # request.messages is a shortcut for request.state["messages"]
        message_count = len(request.messages)  

        if message_count > 10:
            # Long conversation - use model with larger context window
            model = self.aws_llm_large_model
        else:
            # Short conversation - use efficient model
            model = self.aws_llm_standard_model

        request = request.override(model=model)  

        return handler(request)