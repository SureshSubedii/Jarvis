import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[2].id)
engine.setProperty('voice',voices[1].id) 
def SendEmail(to,content):
    server=smtplib.SMPT('smtp.gmail.com',587)
    server.ehlo()
    server.login('<EmailAddressHere>','')
    server.sendmail('<EmailAddressHere>',to,content)
    server.close()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good evening sir")        
    speak("I'm Jarvis. How may I help you sir?")    
def takeCommand():
    '''Takes microphone input  from the user and returns string output'''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=0.5
        audio=r.listen(source)
    try:
         print("Recognizing...")
         query=r.recognize_google(audio,language='en-in')
         print(f"User said : {query}\n") 
    except Exception as e:
        speak("Say that again please....")
        return "None"
    return query           
if __name__=='__main__':
    wishMe()
    while True:
        query=takeCommand().lower()
    #Logic for excuting tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=4)
            print(results)
            speak(f"According to wikipedia {results}")
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'play music' in query:
            mus_dir="D:\\mus"
            songs=os.listdir(mus_dir)
            print(songs) 
            ran_number=random.randint(0,len(songs)-1)
            # print(ran_number)
            os.startfile(os.path.join(mus_dir,songs[ran_number]))   
        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'open vs code' in query:
            VScodepath="C:\\Users\\MSI\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(VScodepath)
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content=takeCommand()
                to="<Receiver'sEmailAddressHere>"
                SendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                speak("Sorry sir. Can't send email at the moment")

        elif 'stop' in query:
            break

    
