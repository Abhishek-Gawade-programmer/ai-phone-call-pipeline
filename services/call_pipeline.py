from interfaces.stt import BaseSTTProvider
from interfaces.llm import BaseLLMProvider
from interfaces.tts import BaseTTSProvider
from typing import Dict


class CallPipelineService:
    """
    CallPipelineService orchestrates the process of handling a call by
    transcribing audio to text, generating a response using a language model,
    and synthesizing the response back to audio.
    """

    def __init__(
        self,
        stt_provider: BaseSTTProvider,
        llm_provider: BaseLLMProvider,
        tts_provider: BaseTTSProvider,
    ):
        """
        Initializes the CallPipelineService with the provided STT, LLM, and TTS providers.

        Args:
            stt_provider (BaseSTTProvider): The speech-to-text provider.
            llm_provider (BaseLLMProvider): The language model provider.
            tts_provider (BaseTTSProvider): The text-to-speech provider.
        """
        self.stt_provider = stt_provider
        self.llm_provider = llm_provider
        self.tts_provider = tts_provider

    async def handle_call(self, audio_data: bytes) -> bytes:
        """
        Handles the call by transcribing the audio, generating a response, and synthesizing the response to audio.

        Args:
            audio_data (bytes): The audio data of the call.

        Returns:
            bytes: The synthesized speech audio data of the response.
        """
        text = await self.stt_provider.transcribe(audio_data)
        response_text = await self.llm_provider.generate_response(text)

        synthesized_audio = await self.tts_provider.synthesize(response_text)

        return synthesized_audio

    async def health_check(self) -> Dict[str, bool]:
        """Check health of all providers"""
        return {
            "stt": await self.stt_provider.health_check(),
            "llm": await self.llm_provider.health_check(),
            "tts": await self.tts_provider.health_check(),
        }
