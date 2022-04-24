from typing_extensions import Self
import speech_recognition as sr
import random
import requests
import datetime
import pyttsx3
import pyautogui
import os
import sys
import time
import subprocess
import webbrowser
import pywhatkit
import smtplib
import psutil, pyttsx3, math 
import wikipedia
import re

#user interface
from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtGui import QMovie
import sys
import time
from imageio import imopen
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType

flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)
FROM_MAIN,_ = loadUiType(os.path.join(os.path.dirname(__file__),"./scifi.ui"))

#button
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

#computational intelligence
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
        #speak("Give me command sir ")
        print("Listening.......")
        command.pause_threshold = 1
        audio = command.listen(source,0,5)

        try:
            #speak("Please wait sir")
            print("Recognizing....")
            query = command.recognize_google(audio,language='en-in')
            print(f"you said : {query}")

        except Exception as Error:
            return "none"
        query =str(query)
        return query.lower()



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



def tell_me_about(topic):
    try:
        
        res = wikipedia.summary(topic, sentences=3)

        return res 
    except Exception as e:
        print(e)
        return False

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
        
        #college information
        elif "Admission" in query or 'Admission process' in query:
            speak("ok sir ,this is found for your query")
            webbrowser.open("https://engg.dypvp.edu.in/ugadmissions.aspx")
            
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
        
        elif 'open stack overflow' in query or 'stack overflow' in query:
            speak("ok sir i will open the stack over flow website")
            webbrowser.open("https://www.stackoverflow.com")
        
        elif 'open vs code' in query or 'vs code' in query:
            codePath = "C:\\Users\\harsh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak("done sir,now start coding ")
        
        elif 'open dev c plus plus  ' in query or 'dev editor' in query:
            codePath = "C:\\Program Files (x86)\\Dev-Cpp\\devcpp.exe"
            os.startfile(codePath)
            speak("done sir,now start coding ")

        elif 'open python idle' in query or 'python editor' in query:
            codePath = "C:\\Python39\\pythonw.exe"
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
        
       

        #computational intelligence using wolfram
        elif "calculate" in query:
                question = query
                answer = computational_intelligence(question)
                speak(answer)
            
        elif "what is" in query or "who is" in query:
                question = query
                answer = computational_intelligence(question)
                speak(answer)

        elif "which is" in query or "which" in query:
                question = query
                answer = computational_intelligence(question)
                speak(answer)
        
        elif re.search('tell me about', query):
                topic = query.split(' ')[-1]
                if topic:
                    wiki_res = tell_me_about(topic)
                    print(wiki_res)
                    speak(wiki_res)
                else:
                    speak("Sorry sir. I couldn't load your query from my database. Please try again")
    #college information
        elif "Admission" in query or 'Admission process' in query:
            speak("ok sir ,this is found for your query")
            webbrowser.open("https://engg.dypvp.edu.in/ugadmissions.aspx")

        elif "college" in query or 'Profile' in query or 'college profile' in query:
            speak("ok sir ,this is found for your query")
            webbrowser.open("https://engg.dypvp.edu.in/college-profile.aspx")

        elif "computer engineering" in query or 'computer branch' in query:
            speak("ok sir ,this is found for your query")
            webbrowser.open("https://engg.dypvp.edu.in/computer-engineering.aspx")

        elif "Academics" in query :
            speak("ok sir ,this is found for your query")
            webbrowser.open("https://engg.dypvp.edu.in/Acadmic-Calender.aspx")

        elif " Training and placement" in query or 'placement' in query:
            speak("ok sir ,this is found for your query")
            webbrowser.open("https://engg.dypvp.edu.in/from-the-desk-of-tpo.aspx")

        elif "University rankers" in query or 'Toppers' in query:
            speak("ok sir ,this is found for your query")
            webbrowser.open("https://engg.dypvp.edu.in/university-rankers.aspx")

        elif "University rankers" in query or 'Toppers' in query:
            speak("ok sir ,this is found for your query")
            webbrowser.open("https://engg.dypvp.edu.in/vision-mission.aspx")
        
        
        
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
        
        elif "ip address" in query:
                ip = requests.get('https://api.ipify.org').text
                print(ip)
                speak(f"Your ip address is {ip}")

        else:
            speak("Command not found, Please speak again !")
            print("command not found")

#user interface functions
def dpu():
    speak("ok sir i will open the dpu website")
    webbrowser.open("https://engg.dypvp.edu.in/")

FROM_MAIN,_ = loadUiType(os.path.join(os.path.dirname(__file__),"./scifi.ui"))

class Main(QMainWindow,FROM_MAIN):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.setupUi(self)
        #self.setFixedSize(1920,1080)
        self.label_7 = QLabel
        self.setGeometry(0,0,1920,1080)
        self.setWindowFlags(flags)
        
        self.label_7 = QMovie("./lib/gifloader.gif", QByteArray(), self)
        self.label_7.setCacheMode(QMovie.CacheAll)
        self.label_4.setMovie(self.label_7)
        self.label_7.start()

        self.ts = time.strftime("%A, %d %B")

        
        self.label.setPixmap(QPixmap("./lib/tuse.png"))
        self.label_5.setText("<font size=8 color='white'>"+self.ts+"</font>")
        self.label_5.setFont(QFont(QFont('Acens',8)))
#ui button keys
        

        self.pushButton1 = QtWidgets.QPushButton(self)
        self.pushButton1.setText("Dpu_website")
        self.pushButton1.setFont(QFont('Arial', 30))
        self.pushButton1.setStyleSheet("color:white")
        self.pushButton1.setGeometry(QtCore.QRect(50,600,375,80))
        self.pushButton1.clicked.connect(Dpu_clicked)
        self.pushButton1.setStyleSheet('QPushButton { color: white;}')
        
        self.pushButton2 = QtWidgets.QPushButton(self)
        self.pushButton2.setText("Run")
        self.pushButton2.setFont(QFont('Arial', 30))
        self.pushButton2.setStyleSheet("color:white")
        self.pushButton2.setGeometry(QtCore.QRect(250,200,200,80))
        self.pushButton2.clicked.connect(Run_clicked)
        

        self.pushButton3 = QtWidgets.QPushButton(self)
        self.pushButton3.setText("Stop")
        self.pushButton3.setFont(QFont('Arial', 30))
        self.pushButton3.setStyleSheet("color:white")
        self.pushButton3.setGeometry(QtCore.QRect(50,400,375,80))
        self.pushButton3.clicked.connect(Stop_clicked)
        
 
        self.setStyleSheet("background-image : url(./lib/tus.png); border : 2px solid blue")

def Run_clicked():
   command()

def Stop_clicked():
   exit()

def Dpu_clicked():
    dpu()
convert_size(1)
system_stats()

app = QtWidgets.QApplication(sys.argv)
main = Main()
main.show()
exit(app.exec_())
