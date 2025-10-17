import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import sys
import time
import webbrowser

# Initialize recognizer and TTS engine once
listener = sr.Recognizer()
engine = pyttsx3.init()

# Choose your mic (change after testing)
MIC_DEVICE_INDEX = 1  # <-- Update this to correct mic index

def talk(text):
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print("TTS Error:", e)

def input_instruction():
    try:
        with sr.Microphone(device_index=MIC_DEVICE_INDEX) as source:
            print("Listening...")
            listener.adjust_for_ambient_noise(source, duration=0.5)
            audio = listener.listen(source, phrase_time_limit=5)
            print("Processing speech...")
            instruction = listener.recognize_google(audio).lower()
            print("Recognized:", instruction)
            return instruction
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError:
        print("Speech recognition service unavailable")
    except Exception as e:
        print("Error:", e)
    return ""  # Return empty if error

def play_pratham():
    while True:
        instruction = input_instruction()

        if not instruction:
            time.sleep(1)
            continue

        if "play" in instruction:
            song = instruction.replace("play", "").strip()
            talk("Searching for " + song)
            webbrowser.open(f"https://www.google.com/search?q={song}+song")

        elif "time" in instruction:
            talk("Current time is " + datetime.datetime.now().strftime('%I:%M %p'))

        elif "date" in instruction:
            talk("Today's date is " + datetime.datetime.now().strftime('%d/%m/%Y'))

        elif "how are you" in instruction:
            talk("I am fine, how about you")

        elif "what is your name" in instruction:
            talk("I am Pratham, what can I do for you?")

        elif "who is" in instruction:
            try:
                human = instruction.replace("who is", "").strip()
                info = wikipedia.summary(human, sentences=2)
                talk(info)
            except:
                talk("Sorry, I couldn't find information")

        elif "exit" in instruction or "stop" in instruction:
            talk("Goodbye!")
            sys.exit(0)

# Start the assistant
play_pratham()
