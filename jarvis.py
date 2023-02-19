from ast import Break
import imp
from unittest import result
import weakref
import pyttsx3 
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser 
import os
import random
from googlesearch import *
from youtubesearchpython import VideosSearch

# this is used for voice assistant 0 for david and 1 for zara
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

#this function used for taking user voice as input
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Ayushi  ")

    elif hour>=12 and hour<=18:
        speak("Good Afternoon Ayushi  ")

    else:
        speak("Good Evening Ayushi ")    

    speak("I am jarvis here .  Please tell me how may i help you")    

def takecommand():
    #it take microform input from user and return string output
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query =r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")

    except Exception as e:
        print("Say that again please..") 
       # speak("Say that again please..")        
        return "None"
    return query    



#

if __name__ == "__main__":
    wishme()
    while True:
   
        query = takecommand().lower()

        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia ")
            print(result)
            speak(result)
        elif   'open youtube' in query:
            speak("opening youtub..")
            webbrowser.open("Youtube.com") 
        elif   'open google' in query:
            speak("opening google..")
            webbrowser.open("Google.com") 
        # elif   'open instagram' in query:
        #     speak("opening instagram..")
        #     webbrowser.open("Instagram.com") 
        elif   'open facebook' in query:
            speak("opening facebook..")
            webbrowser.open("Facebook.com") 
        elif   'open stackoverflow' in query:
            speak("opening stackoverflow..")
            webbrowser.open("stackoverflow.com")      

        elif 'play music' in query:
            music_dir = 'C:\\music'
            song = os.listdir(music_dir)
            speak("playing music..")
            print(song)
            songs = random.choice(song)
            os.startfile(os.path.join(music_dir,songs))               

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"ayushi , the time is  {strtime}")    

        elif 'open vs code' in query:
            codepath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("opeing vscode...")
            os.startfile(codepath)    

        # elif 'email to ayushi' in query:
        elif 'search' in query:
            var = query
            # for j in search(query, tld="co.in", num=10, stop=10, pause=2):
            #    print(j)
            chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe %s'
            for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
                webbrowser.open("https://google.com/search?q=%s" % query)
                     
                speak("here are some information relate to your search ")



        elif 'good bye'  in query:
             
            speak("thank you AYushi ..i hope  we will meet soon ")
            break      
        elif '' in query:
            speak("sorry i can't hear you")  


        

            
