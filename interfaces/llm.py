from abc import ABC, abstractmethod


class BaseLLMProvider(ABC):
    """
    Abstract base class for Language Model providers.

    This class defines the interface for different LLM implementations.
    Concrete subclasses should implement the generate_response method.
    """

    @abstractmethod
    async def generate_response(self, prompt: str) -> str:
        """
        Generates a response from a given prompt.

        Args:
            prompt (str): The input prompt for the language model.

        Returns:
            str: The generated response from the language model.

        Raises:
            NotImplementedError: If the method is not implemented by a subclass.
        """
        pass

    @abstractmethod
    async def health_check(self) -> bool:
        """Check if the provider is operational"""
        pass
