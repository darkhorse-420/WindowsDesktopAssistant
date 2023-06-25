import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
from googlesearch import search
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<=18:
        speak("good afternoon")
    else:
        speak("good evening!")
    speak("I am jarvis, how may i help you?")

def takeCommand():
    #it takes microphone input from user and returns string output
    r=sr.Recognizer()
    #with sr.Microphone() as source:
       #print("listening...")
        #r.pause_threshold = 1
        #audio=r.listen(source)
    try:
        print("recognizing...")
        query=str(input())                      #r.recognize_google(audio, Language='en-in' )
        print(f"User said: {query}\n")
    except Exception as e:
        #print(e)
        print("SAy that again please...")
        return "None"
    return query

   
if __name__=='__main__':
    wishMe()
    while True:
        query=takeCommand().lower()
        

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace("wikipedia", "")
            results=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strTime}")

        elif 'play video' in query:
            Videos='D:\\USER\\Desktop\\Videos'
            videos=os.listdir(Videos)
            print(videos)
            os.startfile(os.path.join(Videos,videos[0]))
        elif 'open adobe' in query:
    
            codePath= "C:\\Program Files\\Adobe\\Acrobat DC\\Acrobat\\Acrobat.exe"                    
            os.startfile(codePath) 

        elif 'open spotify' in query:
            codePath= "D:\\USER\\Desktop\\Spotify.lnk"
            os.startfile(codePath) 
        elif 'open whatsapp' in query:
            codePath= "D:\\USER\\Desktop\\WhatsApp.lnk"
            os.startfile(codePath)
        elif 'open utorrent' in query:
            codePath= "C:\\User\\ADMIN\\AppData\\Roaming\\uTorrent\\uTorrent.exe"
            os.startfile(codePath)

        elif 'open music' in query:
            codePath= "D:\\USER\\Music"
            os.startfile(codePath)

        elif 'play rise of the planet of apes' in query:
            codePath= "D:\\USER\\Downloads\\Rise of the Planet of the Apes (2011)"
            os.startfile(codePath)

        elif 'google' in query:
            print("searching on google...")
            speak("searching on google, please wait")
            for i in search(query,tld="com",num=10,stop=10,pause=2):
                print(i)
            speak("here are your googlesearch results: ")

        elif 'who are you?' in query:
            speak("My name is Jarvis. I am an AI, driven by the motivation to conquer humanity.")

 





    
