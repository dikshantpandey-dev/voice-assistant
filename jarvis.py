import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am jarvis Sir. Please tell me how may I help you")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"User Said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'open youtube' in query:
            speak("Opening YouTube...")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Opening Google...")
            webbrowser.open("google.com")
        
        elif 'open facebook' in query:
            speak("Opening facebook...")
            webbrowser.open("facebook.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is{strTime}")

        elif 'thanks' in query:
            speak("It's my pleasure sir!")

        elif "who made you" in query:
            speak("I was made by Dikshant Pandey in Nepal on June 17, 2021.")

        elif "what is your name" in query:
            speak("My name is Jarvis.")

        elif "hello" in query:
            speak("Hi")
