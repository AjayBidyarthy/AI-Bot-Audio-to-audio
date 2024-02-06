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


