"""Main file for the project"""
import os
from os import PathLike
from time import time
import asyncio
from typing import Union
from openai import OpenAI
from dotenv import load_dotenv
import openai
import whisper
import pygame
from pygame import mixer
import elevenlabs
from elevenlabs import Voice, VoiceSettings, generate
from record import speech_to_text

# Load API keys
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
elevenlabs.set_api_key(os.getenv("ELEVENLABS_API_KEY"))

# Initialize APIs
gpt_client = openai.Client(api_key=OPENAI_API_KEY)
mixer.init()

# Change the context if you want to change Assistant's personality
context = "You are Alex, Blackcoffer's human assistant. You are witty and full of personality. Your answers should be limited to 1-2 short sentences."
conversation = {"Conversation": []}
RECORDING_PATH = "audio/recording.wav"


def request_gpt(prompt: str) -> str:
    """
    Send a prompt to the GPT-3 API and return the response.

    Args:
        - state: The current state of the app.
        - prompt: The prompt to send to the API.

    Returns:
        The response from the API.
    """
    response = gpt_client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"{prompt}",
            }
        ],
        model="gpt-3.5-turbo",
    )
    return response.choices[0].message.content
    
async def transcribe(file_name: Union[Union[str, bytes, PathLike[str], PathLike[bytes]], int]):
   """
   Transcribe audio using OpenAI Whisper.

   Args:
       - file_name: The name of the file to transcribe.

   Returns:
       The transcription text.
   """

   try:
       model = whisper.load_model("base")  # Load the base Whisper model
       result = model.transcribe(file_name)
       return result["text"]

   except Exception as e:
           return {"details": e}

def log(log: str):
    """
    Print and write to status.txt
    """
    print(log)
    with open("status.txt", "w") as f:
        f.write(log)


if __name__ == "__main__":
    while True:
        # Record audio
        log("Listening...")
        speech_to_text()
        log("Done listening")

        # Transcribe audio
        current_time = time()
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        string_words = loop.run_until_complete(transcribe(RECORDING_PATH))
        with open("conv.txt", "a") as f:
            f.write(f"{string_words}\n")
        transcription_time = time() - current_time
        log(f"Finished transcribing in {transcription_time:.2f} seconds.")

        # Get response from GPT-3
        current_time = time()
        context += f"\nAlex: {string_words}\nAssistant: "
        response = request_gpt(context)
        context += response
        gpt_time = time() - current_time
        log(f"Finished generating response in {gpt_time:.2f} seconds.")


        # Convert response to audio
        current_time = time()
        audio = elevenlabs.generate(
            text=response, model="eleven_multilingual_v2",
            voice = Voice(
                voice_id="29vD33N1CtxCmqQRPOHJ",
                settings=VoiceSettings(stability=0.71, similarity_boost=0.5, style=0.0, use_speaker_boost=True)
            )
        )
        elevenlabs.save(audio, "audio/response.wav")
        audio_time = time() - current_time
        log(f"Finished generating audio in {audio_time:.2f} seconds.")

        # Play response
        log("Speaking...")
        sound = mixer.Sound("audio/response.wav")
        # Add response as a new line to conv.txt
        with open("conv.txt", "a") as f:
            f.write(f"{response}\n")
        sound.play()
        pygame.time.wait(int(sound.get_length() * 1000))
        print(f"\n --- USER: {string_words}\n --- ALEX: {response}\n")
