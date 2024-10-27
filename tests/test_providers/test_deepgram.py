import pytest
import httpx
from providers.deepgram_stt import DeepGramSTT
from tests.mocks import (
    mock_post,
    mock_post_error,
    mock_get,
    mock_get_error,
)  # Import mocks


@pytest.mark.asyncio
async def test_deepgram_stt_transcribe(mocker):

    mock_client = httpx.AsyncClient()
    mocker.patch.object(mock_client, "post", side_effect=mock_post)
    stt_provider = DeepGramSTT(api_key="fake_key")
    stt_provider.http_client = mock_client  # Mocking HTTP client

    transcription = await stt_provider.transcribe(b"fake_audio_data")
    assert transcription == "Hello world"
    mock_client.post.assert_called_once_with(
        endpoint="/listen", content=b"fake_audio_data"
    )


@pytest.mark.asyncio
async def test_deepgram_stt_transcribe_error(mocker):

    mock_client = httpx.AsyncClient()
    mocker.patch.object(mock_client, "post", side_effect=mock_post_error)
    stt_provider = DeepGramSTT(api_key="invalid_key")
    stt_provider.http_client = mock_client  # Mocking HTTP client

    await stt_provider.transcribe(b"fake_audio_data")

    mock_client.post.assert_called_once_with(
        endpoint="/listen", content=b"fake_audio_data"
    )


@pytest.mark.asyncio
async def test_deepgram_stt_health_check(mocker):
    mock_client = httpx.AsyncClient()
    mocker.patch.object(mock_client, "get", side_effect=mock_get)
    stt_provider = DeepGramSTT(api_key="fake_key")
    stt_provider.http_client = mock_client  # Mocking HTTP client

    assert await stt_provider.health_check() is True


@pytest.mark.asyncio
async def test_deepgram_stt_health_check_error(mocker):
    mock_client = httpx.AsyncClient()
    mocker.patch.object(mock_client, "get", side_effect=mock_get_error)
    stt_provider = DeepGramSTT(api_key="fake_key")
    stt_provider.http_client = mock_client  # Mocking HTTP client

    assert await stt_provider.health_check() is False
