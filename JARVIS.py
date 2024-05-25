import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import sys
import requests
from bs4 import BeautifulSoup
import pyjokes
import pyttsx3
import PyPDF2
from tkinter.filedialog import *



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)




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

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=8)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak(f"opening youtube")
            webbrowser.open("youtube.com")
      
        elif 'read pdf' in query:

        

            book = askopenfilename()
            pdfreader = PyPDF2.PdfFileReader(book)
            pages = pdfreader.numPages

            for num in range(0, pages):
                page = pdfreader.getPage(num)
                text = page.extractText()
                player = pyttsx3.init()
                player.say(text)
                player.runAndWait()

            

          
        elif 'open google' in query:
            speak(f"opening google")
            webbrowser.open("google.com")

        elif 'play music' in query:
            speak(f"opening gaana website")
            webbrowser.open("gaana.com")   

        elif 'open email' in query:
            speak(f"opening gmail")
            webbrowser.open("mail.google.com") 
        elif 'temperature' in query:
           search="temperature in kolkata"
           url=f"https://www.google.com/search?q={search}"
           r=requests.get(url)
           data= BeautifulSoup(r.text,"html.parser")
           temperature = data.find("div",class_ ="BNeawe").text
           speak(f"The Temperature Outside Is {temperature} ")
        elif 'who created you' in query:
            speak(f"Group 102")
        elif 'shutdown'in query:
            os.system("shutdown /s /t 1")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        elif 'tell jokes' in query:
            my_joke=pyjokes.get_joke('en',category='neutral')
            print(my_joke)
            speak(my_joke)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif "no thanks"in query:
            speak("thanks for using sir Have a good day")
            sys.exit()

        

       
