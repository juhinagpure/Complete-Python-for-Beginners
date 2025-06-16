import speech_recognition as sr
import pyttsx3

# Initialize recognizer and speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Initializing Jarvis...")

    while True:
        with sr.Microphone() as source:
            print("🎤 Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=1)  # reduce noise
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

        # Try speech recognition using Sphinx
        try:
            print("🔍 Recognizing...")
            command = recognizer.recognize_sphinx(audio)
            print(f"✅ Command recognized: {command}")
            speak(f"You said: {command}")

            if "stop" in command.lower():
                speak("Shutting down. Goodbye!")
                break

        except sr.UnknownValueError:
            print("❌ Could not understand the audio")
            speak("Sorry, I didn't catch that.")
        except sr.RequestError as e:
            print(f"❌ Sphinx error: {e}")
            speak("There was an error with speech recognition.")
