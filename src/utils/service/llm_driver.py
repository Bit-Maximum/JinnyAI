import abc


class LLMDriver:
    """LLM Service Driver Interface"""

    @abc.abstractmethod
    def get_response(self, message: str) -> str:
        """Send message to LLM and return the response text"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_response_stream(self, messages: str):
        """Send list of messages to LLM and return the response stream"""
        raise NotImplementedError
