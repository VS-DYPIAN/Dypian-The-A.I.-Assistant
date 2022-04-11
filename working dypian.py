import speech_recognition as sr
import random
import tkinter    
from tkinter import *
import datetime
import pyttsx3
import pyautogui
import os
import sys
import time
import requests
import subprocess
import webbrowser
import pywhatkit
import smtplib
import psutil, pyttsx3, math 
import ctypes
from tkinter import _tkinter
from PIL import ImageTk,Image
from torch import take
import wolframalpha
app_id="GQ8PHQ-V7R6WA3EKU"
app = wolframalpha.Client(app_id)

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty('voices',voices[0].id)
Assistant.setProperty('rate',170)

GREETINGS = ['hello ', 'DYPIAN', 'wake up', 'you there DYPIAN', 'time to work DYPIAN', 'hey DYPIAN',
             'ok DYPIAN', 'are you there']
GREETINGS_RES = ['always there for you sir', 'i am ready sir',
                 'your wish my command', 'how can i help you sir?', 'i am online and ready sir']
global query

def speak(audio):
    Assistant.say(audio)
    a=print(f":{audio}")
    Assistant.runAndWait()

def computational_intelligence(question):
    try:
        client = wolframalpha.Client(app_id)
        answer = client.query(question)
        answer = next(answer.results).text
        print(answer)
        return answer
    except:
        speak("Sorry sir I couldn't fetch your question's answer. Please try again ")
        return None
"""def location(self, location): # non working 
        current_loc, target_loc, distance = loc.loc(location)
        return current_loc, target_loc, distance

def my_location(self):
        city, state, country = loc.my_location()
        return city, state, country"""
def startup():
    speak("Initializing DYPIAN")
    speak("Starting all systems applications")
    speak("Installing and checking all drivers")
    speak("Caliberating and examining all the core processors")
    speak("Checking the internet connection")
    speak("Wait a moment sir")
    speak("All drivers are up and running")
    speak("All systems have been activated")
    speak("Now I am online")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning SIR !")

    elif hour>=12 and hour<18:
        speak("Good Afternoon SIR !")   

    else:
        speak("Good Evening SIR !")  

    speak("I am D.Y.P.I.A.N. the student A.I. assistant! Sir. Please tell me how may I help you")


def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        command.pause_threshold = 1
        audio = command.listen(source,0,5)

        try:
            print("Recognizing....")
            query = command.recognize_google(audio,language='en-in')
            print(f"you said : {query}")

        except Exception as Error:
            return "none"
        query =str(query)
        return query.lower()

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('harshadsawantdada@gmail.com', 'V@142002')
    server.sendmail('harshadsawantdada@gmail.com', to, content)
    server.close()

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   print("%s %s" % (s, size_name[i]))
   return "%s %s" % (s, size_name[i])


def system_stats():
    cpu_stats = str(psutil.cpu_percent())
    battery_percent = psutil.sensors_battery().percent
    memory_in_use = convert_size(psutil.virtual_memory().used)
    total_memory = convert_size(psutil.virtual_memory().total)
    final_res = f"Currently {cpu_stats} percent of CPU, {memory_in_use} of RAM out of total {total_memory}  is being used and battery level is at {battery_percent} percent"
    print(final_res) 

def command():
    speak("Sir , please give me command")
    while True:
        query = takecommand()
        #Normal conversastion
        if 'hello' in query:
            speak("Hello sir,I am D y pian the student assistant .")
            speak("your Personal AI Assistant")
            speak("How may I Help you?")
        
        elif 'how are you' in query:
            speak("I am fine sir!")
            speak("Whats about you?")
        
        elif 'fine'  in query or 'nice'  in query :
            speak("Ok sir , great")
            speak("Whats can i do for you?")
        
        elif query  in GREETINGS  :
                speak(random.choice(GREETINGS_RES))
        
        #Information about project
        elif 'project' in query:
            speak("OK Sir")
            speak("Project name is A I assistant for DPU students")
            speak("Team members are Vaibhav ,krishna ,Ayush and Dhiraj")
            speak("""Features of Our project is that Our A I Assistant offers voice commands,voice searching, 
                  and voice-activated device control, letting you complete a number of tasks . 
                  It is designed to give you conversational interactions to solve your queries and 
                  doubt regarding college issues .""")
        
        # Automation of different function
        elif 'google search' in query:
            speak('this is I found for your search')
            query=query.replace('DYPIAN'," ")
            query=query.replace ('google search'," ")
            pywhatkit.search(query)
            speak('done sir')
        
        elif 'youtube search ' in query:
            query=query.replace('DYPIAN'," ")
            query=query.replace ('youtube search'," ")
            web = 'https://www.youtube.com/results?search_query='+ query
            webbrowser.open(web)
            speak("done sir!")
        
        elif 'open stack overflow' in query:
            speak("ok sir i will open the stack over flow website")
            webbrowser.open("https://www.stackoverflow.com")
        
        elif 'open vs code' in query:
            codePath = "C:\\Users\\harsh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak("done sir,now start coding ")

        elif 'the time' in query or 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        
        elif "switch the window" in query or "switch window" in query or "switch tab" in query:
                speak("Okay sir, Switching the window")
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")
        
        elif 'send email' in query:  # non working
            try:
                speak("What should I say?")
                content = takecommand()
                to = "harshadsawantdada@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Vaibhav bhai. I am not able to send this email")

        elif "ip address" in query:
                ip = requests.get('https://api.ipify.org').text
                print(ip)
                speak(f"Your ip address is {ip}")

        #computational intelligence using wolfram
        elif "calculate" in query:
                question = query
                answer = computational_intelligence(question)
                speak(answer)
            
        elif "what is" in query or "who is" in query:
                question = query
                answer = computational_intelligence(question)
                speak(answer)

        # system exit
        elif "goodbye" in query or "offline" in query or "bye" in query or "exit" in query:
                speak("Alright sir, going offline. It was nice working with you")
                sys.exit()
        
        elif 'shutdown' in query:
           speak("Do you wish to shutdown your computer ? (yes shut down / no): ")
  
           if 'Yes shutdown' in query:
              os.system("shutdown /s /t 1")
           else:
               exit() 
        
        else:
            print("command not found")

# user interface buttons keys
def win():
    
    speak("ok sir i will open the google")
    webbrowser.open("https://www.google.com")
 
def you():
    speak("ok sir open the youtube.com")
    webbrowser.open("https://www.youtube.com")

def Stop():
    speak("Alright sir, going offline. It was nice working with you")
    exit()

# user interface 
window = Tk()
window.configure(bg = "black")
SET_WIDTH = 1362
SET_HEIGHT = 609 



"""query = Entry(window,width=40,bg="black",fg="white",font = ('arial',18,'bold'))   
query.pack(padx = 10,pady = 20)"""   #STARTING ENTRY BOX FOR TYPING

def main():
    # screen

    bgImg = Image.open("C:\FOURTH SEMSTER\JARVIS\JARVIS AI\DYPIAN1.png")
    window.title("D.Y.PIAN")
    canvas = tkinter.Canvas(window,width = SET_WIDTH,height = SET_HEIGHT)

    image=ImageTk.PhotoImage(bgImg)
    canvas.create_image(0,0,anchor=NW,image=image)


    # entry


    btn = Button(text = "Run" ,bg = "black" ,fg="white",width=20,
    activeforeground = "grey",activebackground = "black",command = command)
    btn.pack(padx = 0,pady= 0)

    btn = Button(text = "Stop",bg = "black" ,fg = "white",width=20,activeforeground = "grey",activebackground = "black",
                 command=Stop).pack(side = TOP)
    
    canvas.configure(bg="black")

    
    
    shape = canvas.create_oval(10,10,60,60,fill = "yellow")
    xspeed = random.randrange(11,20)
    yspeed = random.randrange(11, 20)

    shape2 = canvas.create_oval(10,10,60,60,fill = "yellow")
    xspeed2 = random.randrange(5,20)
    yspeed2 = random.randrange(5,20)

    canvas.pack()
    
    while True:
        canvas.move(shape,xspeed,yspeed)
        pos = canvas.coords(shape)
        if pos[3]>= 609 or pos[1] <=0:
            yspeed = -yspeed
        if pos[2] >= 1362 or pos[0] <=0:
            xspeed= -xspeed

        canvas.move(shape2,xspeed2,yspeed2)
        pos = canvas.coords(shape2)
        if pos[3]>= 609 or pos[1] <=0:
            yspeed2 = -yspeed2
        if pos[2] >= 1362 or pos[0] <=0:
            xspeed2= -xspeed2                                
        window.update()
        time.sleep(0.01)
        
    
def ball():
    canvas = Canvas()
    


if __name__ == "__main__":
    #startup()
    wishMe()
    convert_size(1)
    system_stats()   
    main()

