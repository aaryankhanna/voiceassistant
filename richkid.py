import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    print("RICH KID op in CHAT ")
    speak("I am Rich Kid Sir. Please tell me how may I help you")



def takeCommand():
    # It takes microphone input from the user and returns string output
    speak("Please give me the command or say  exit to stop using my services")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        q = r.recognize_google(audio, language='en-in')
        print(f"User said: {q}\n")
        speak(q)
        return q
    except Exception as e:
        print("Say that again please...")
        return "None"


if __name__ == "__main__":
    wishMe()
    while True:

        query = takeCommand()
        query = query.lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...Please wait for the results')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")

            print(results)
            speak(results)
            time.sleep(1)


        elif 'open youtube' in query:
            webbrowser.open_new("https://www.youtube.com/")

        elif 'open google' in query:
            webbrowser.open_new("https://www.google.com")

        elif 'open stack overflow' in query:
            webbrowser.open_new_tab("https://www.stackoverflow.com")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")
        elif 'date' in query:
            strdate = datetime.datetime.now().date()
            print(strdate)
            speak(f"Sir, the date is {strdate}")

        elif 'open pycharm' in query:
            codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3\\bin\\pycharm64.exe"
            os.startfile(codePath)

        elif 'bitcoin' in query:
            print("You still don't have it? Just buy it you fool")
            speak("You still don't have it? Just buy it you fool")

            webbrowser.open_new("https://wazirx.com/exchange/BTC-INR")


        elif 'exit' in query:
            speak("Thanks for using Rich Kid Voice Assistant. Have a nice day ahead")
            exit()
        else:
            speak("I am googling your stuff!")
            webbrowser.open_new(f"https://google.com/search?q={query}")
