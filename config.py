from providers.deepgram_stt import DeepGramSTT
from providers.openai_llm import OpenAILLM
from providers.elevenlabs_tts import ElevenLabsTTS


def get_stt_provider(api_key: str):
    """
    Get an instance of the DeepGramSTT provider.

    Args:
        api_key (str): The API key for the DeepGramSTT provider.

    Returns:
        DeepGramSTT: An instance of the DeepGramSTT provider initialized with the provided API key.
    """
    return DeepGramSTT(api_key=api_key)


def get_llm_provider(api_key: str):
    """
    Get an instance of the OpenAILLM provider.

    Args:
        api_key (str): The API key for the OpenAILLM provider.

    Returns:
        OpenAILLM: An instance of the OpenAILLM provider initialized with the provided API key.
    """
    return OpenAILLM(api_key=api_key)


def get_tts_provider(api_key: str):
    """
    Get an instance of the ElevenLabsTTS provider.

    Args:
        api_key (str): The API key for the ElevenLabsTTS provider.

    Returns:
        ElevenLabsTTS: An instance of the ElevenLabsTTS provider initialized with the provided API key.
    """
    # you can use DeepGramTTS as well
    return ElevenLabsTTS(api_key=api_key)
