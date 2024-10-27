# AI Phone Call Pipeline Library

## Project Objective

The objective of this project is to create a library that serves as an interface between the three stages of an AI phone call pipeline: Speech-to-Text (STT), Language Model (LLM), and Text-to-Speech (TTS). The library is designed to provide a consistent and intuitive API, allowing developers to easily switch out providers across the stack. For this assessment, the following providers have been implemented:

1. **DeepGram** for STT
2. **OpenAI** for LLM
3. **ElevenLabs** for TTS

The library does not use client libraries for these providers. Instead, it creates an abstraction around their APIs, ensuring clean, well-documented, and well-thought-out code.

## Project Structure

The project is organized into several key components:

- **`interfaces/`**: Contains abstract base classes defining the interfaces for STT, LLM, and TTS providers.
- **`providers/`**: Contains concrete implementations of the provider interfaces for DeepGram, OpenAI, and ElevenLabs.
- **`services/`**: Contains the `CallPipelineService` class, which orchestrates the process of handling a call.
- **`utils/`**: Contains utility classes, such as `HttpClient`, for making HTTP requests.
- **`tests/`**: Contains unit tests for the providers and the pipeline service.
- **`main.py`**: The entry point for the FastAPI application, providing endpoints for processing calls and health checks.

## Core Functions

### Speech-to-Text (STT)

- **DeepGramSTT**: Implements the `BaseSTTProvider` interface to transcribe audio data using the DeepGram API.

### Language Model (LLM)

- **OpenAILLM**: Implements the `BaseLLMProvider` interface to generate text responses using the OpenAI API.

### Text-to-Speech (TTS)

- **ElevenLabsTTS**: Implements the `BaseTTSProvider` interface to synthesize text into speech using the ElevenLabs API.

### Call Pipeline Service

- **CallPipelineService**: Orchestrates the process of handling a call by transcribing audio to text, generating a response using a language model, and synthesizing the response back to audio.

## Setup Instructions

1. **Clone the Repository**:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**:
   Use the `requirements.txt` file to install the necessary Python packages.

   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Variables**:
   Create a `.env` file in the root directory and add your API keys for DeepGram, OpenAI, and ElevenLabs.

   ```plaintext
   DEEPGRAM_API_KEY=your_deepgram_api_key
   OPENAI_API_KEY=your_openai_api_key
   ELEVENLABS_API_KEY=your_elevenlabs_api_key
   ```

4. **Run the Application**:
   Use Uvicorn to run the FastAPI application.

   ```bash
   uvicorn main:app --reload
   ```

5. **Access the API**:
   The API will be available at `http://localhost:8000`. You can use the `/call` endpoint to process audio files and the `/health` endpoint to check the health of all providers.

## Meeting Project Objectives

- **Consistent API**: The library provides a unified interface for interacting with different providers, making it easy to switch between them without changing the core logic.
- **Abstraction**: By not using client libraries, the project demonstrates how to directly interact with provider APIs, offering flexibility and control.
- **Documentation**: The code is well-documented, with clear docstrings explaining the purpose and usage of each class and method.
- **Testing**: Comprehensive tests ensure the reliability and correctness of the library's functionality.

This library is designed to be a robust and flexible solution for integrating AI capabilities into phone call applications, with the ability to easily adapt to different provider APIs.
