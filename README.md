# Application Architecture

Below is an overview of the architecture for an AI audio-to-audio application leveraging OpenAI Whisper and ElevenLabs’ text-to-speech (TTS) API:

![Copy of Solution Diagram (1)](https://github.com/AjayBidyarthy/AI-Bot-Audio-to-audio/assets/29508011/aaf528fb-530b-489e-a92a-e3348ddd867d)


1. **Physical Input (Voice Recording):**
   - The user provides a spoken input through a microphone.
   - PyAudio library is used to record the audio input, saving it as a .wav file.

2. **Transcribe:**
   - The recorded .wav file is fed into OpenAI Whisper for speech-to-text transcription.

3. **GPT-3.5 Turbo:**
   - The transcribed text is passed to GPT-3.5 Turbo, a large language model fine-tuned for various tasks.
   - GPT-3.5 Turbo generates a response text based on the input.

4. **Display Response:**
   - The generated response text is displayed for the user to read.

5. **Speech Synthesis:**
   - The response text is sent to ElevenLabs TTS API for text-to-speech synthesis.
   - The API synthesizes the text into an audio file, which can be in .wav or .mp3 format.

6. **Play the Response Audio:**
   - The synthesized audio file is played back for the user to hear.





# Installation

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

    If you're using Python 3.x and the `python` command doesn't work, try `python3` instead. 

4. **Activate the virtual environment:**

    On Windows:

    ```bash
    venv\Scripts\activate
    ```

    On macOS and Linux:

    ```bash
    source venv/bin/activate
    ```

    Activating the virtual environment ensures that all subsequent Python commands are isolated within this environment.

5. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    This command will install all the necessary dependencies for the project.




# Running the Project

Follow these steps to run the project:

1. **Create a .env file:**

    Copy the content from the `.env.example` file and create a new `.env` file in the project directory. Populate the `.env` file with the necessary API keys and configuration variables.

2. **Run the frontend:**

    ```bash
    python display.py
    ```

    This command will start the frontend of the application. Ensure that all necessary dependencies are installed before running this command.

3. **Run the backend application:**

    ```bash
    python main.py
    ```

    This command will start the backend of the application. Make sure you've activated the virtual environment if you created one earlier.

4. **Start the conversation:**

    Once both the frontend and backend are running, you can start speaking into the microphone. The conversation will be displayed on the frontend interface.

5. **Clear conversation and start afresh:**

    If you want to clear the conversation and start a new one, simply click the "New Conversation" button on the frontend interface.

6. **Enjoy your conversation!**

    You're all set to interact with the project. Have fun chatting!


