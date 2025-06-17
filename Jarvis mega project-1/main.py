import speech_recognition as sr
import pyttsx3
import webbrowser
import musicLibrary  # make sure this has a 'music' dictionary

# Initialize recognizer and speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(command):
    command = command.lower().strip()

    if "open google" in command:
        webbrowser.open("https://www.google.com")

    elif "open facebook" in command:
        webbrowser.open("https://www.facebook.com")
    
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
    
    elif command.startswith("play"):
        song = command.replace("play", "", 1).strip()
        if song in musicLibrary.music:
            link = musicLibrary.music[song]
            speak(f"Playing {song}")
            webbrowser.open(link)
        else:
            speak(f"Sorry, I couldn't find {song} in your music library.")
    
    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        exit()

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=2)
                word = recognizer.recognize_google(audio, language="en-in").lower()

                if word == "jarvis":
                    speak("Yes?")
                    with sr.Microphone() as source:
                        print("Listening for command...")
                        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                        command = recognizer.recognize_google(audio, language="en-in")
                        print(f"Command: {command}")
                        processCommand(command)

        except Exception as e:
            print(f"Error: {e}")
