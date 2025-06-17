import speech_recognition as sr
import pyttsx3
import webbrowser

# Initialize recognizer and speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")

    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com")
    
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")

    
if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        r=sr.Recognizer()

        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio=r.listen(source,timeout=2,phrase_time_limit=1)
            word=r.recognize_google(audio,language="en-in")
            if(word.lower()== "jarvis"):
                speak("ya")

                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio, language="en-in")

                    processCommand(command)

        except Exception as e:
            print("Error;{0}".format(e))

