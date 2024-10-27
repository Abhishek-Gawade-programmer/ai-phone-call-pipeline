from abc import ABC, abstractmethod


class BaseSTTProvider(ABC):
    """
    Abstract base class for Speech-to-Text (STT) providers.

    This class defines the interface for different STT implementations.
    Concrete subclasses should implement the transcribe method.
    """

    @abstractmethod
    async def transcribe(self, audio_data: bytes) -> str:
        """
        Transcribes the given audio data to text.

        Args:
            audio_data (bytes): The audio data to be transcribed.

        Returns:
            str: The transcribed text from the audio data.

        Raises:
            NotImplementedError: If the method is not implemented by a subclass.
        """
        pass

    @abstractmethod
    async def health_check(self) -> bool:
        """Check if the provider is operational"""
        pass
