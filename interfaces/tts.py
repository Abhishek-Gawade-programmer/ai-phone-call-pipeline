from abc import ABC, abstractmethod


class BaseTTSProvider(ABC):
    """
    Abstract base class for Text-to-Speech (TTS) providers.

    This class defines the interface for different TTS implementations.
    Concrete subclasses should implement the synthesize method.
    """

    @abstractmethod
    async def synthesize(self, text: str) -> bytes:
        """
        Converts the given text to audio data.

        Args:
            text (str): The text to be converted to audio.

        Returns:
            bytes: The synthesized speech audio data.

        Raises:
            NotImplementedError: If the method is not implemented by a subclass.
        """
        pass

    @abstractmethod
    async def health_check(self) -> bool:
        """Check if the provider is operational"""
        pass
