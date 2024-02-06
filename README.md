# Table of Contents
1. [Application Architecture](#application-architecture)
2. [Installation](#installation)
3. [Running the Project](#running-the-project)
4. [File Descriptions](#file-descriptions)

---

## Application Architecture

Below is the overview of the architecture for an AI audio-to-audio chatbot application leveraging OpenAI Whisper and ElevenLabs’ text-to-speech (TTS) API:

![Copy of Solution Diagram (1)](https://github.com/AjayBidyarthy/AI-Bot-Audio-to-audio/assets/29508011/2aa49ecb-5aa2-4db2-aac6-7c5d570bc1e2)

- **Physical Input (Voice Recording):**
    - The user provides a spoken input through a microphone.
    - PyAudio library is used to record the audio input, saving it as a .wav file.

- **Transcribe:**
    - The recorded .wav file is fed into OpenAI Whisper for speech-to-text transcription.

- **GPT-3.5 Turbo:**
    - The transcribed text is passed to GPT-3.5 Turbo, a large language model fine-tuned for various tasks.
    - GPT-3.5 Turbo generates a response text based on the input.

- **Display Response:**
    - The generated response text is displayed for the user to read.

- **Speech Synthesis:**
    - The response text is sent to ElevenLabs TTS API for text-to-speech synthesis.
    - The API synthesizes the text into an audio file, which can be in .wav or .mp3 format.

- **Play the Response Audio:**
    - The synthesized audio file is played back for the user to hear.

## Installation

Follow these steps to install and set up the project:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/AjayBidyarthy/AI-Bot-Audio-to-audio.git
    ```
2. **Navigate to the project directory:**
    ```bash
    cd AI-Bot-to-Audio
    ```
3. **Create a Python virtual environment:**
    ```bash
    python -m venv venv
    ```
    - If you're using Python 3.x and the python command doesn't work, try python3 instead.

4. **Activate the virtual environment:**
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```
5. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Running the Project

Follow these steps to run the project:

1. **Create a .env file:**
    - Copy the content from the .env.example file and create a new .env file in the project directory. Populate the .env file with the necessary API keys and configuration variables.

2. **Run the frontend:**
    ```bash
    python display.py
    ```
3. **Run the backend application:**
    ```bash
    python main.py
    ```

4. **Start the conversation:**
    - Once both the frontend and backend are running, you can start speaking into the microphone. The conversation will be displayed on the frontend interface.

5. **Clear conversation and start afresh:**
    - If you want to clear the conversation and start a new one, simply click the "New Conversation" button on the frontend interface.

6. **Enjoy your conversation!**
    - You're all set to interact with the project. Have fun chatting!

## File Descriptions

Here's a brief description of the files in the project:

- **record.py:**
    - This file contains functions to record audio input from the user through a microphone.

- **main.py:**
    - Contains functions for the main backend operations of the application.
    - Includes functions for transcribing audio to text using OpenAI Whisper base model (speech to text).
    - Also contains functions for generating response text from OpenAI GPT model.
    - Utilizes ElevenLabs API for text-to-speech synthesis and playback of the audio response.

- **display.py:**
    - Code for the taipy frontend of the application is implemented in this file.
    - It handles the user interface and interaction with the backend components.
