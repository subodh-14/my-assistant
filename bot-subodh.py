import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if(hour >= 0 and hour < 12):
        speak("GOOod MoorNing")
    elif(hour >= 12 and hour < 18):
        speak("good afternoon")
    else:
        speak("Good Evening")

    speak("hello, my name is ZORO..i am your assistant. Please tell me how may I help you")


def takeCommand():
   

    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User :{query}\n")

    except Exception as e:
        print("Sorry!! , Say it again")
        return "None"
    return query

if __name__ == "__main__":
    # speak("subodh you are very great person ")
    wishMe()
    speak("shivangi is a kuch buchiya gadi and she is a kauuwa")
    while True:
        query = takeCommand().lower()
        

        if 'wikipedia' in query:
            speak('Searching the wikipedia..')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open github' in query:
            webbrowser.open("github.com")

        elif 'play anime' in query:
            music_dir = 'D:\\Anime\\RoR'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif "the time" in query:
            timeNow = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"hello , Subodh the time is {timeNow}")

        elif 'open sublime' in query:
            codePath ="C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
            os.startfile(codePath)

        elif "say that" in query:
            speak(query[10:])
        


        elif 'quit' in query:
            exit()

