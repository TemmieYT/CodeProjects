# Created by Temmie Amodo
import os
import subprocess as sp
import webbrowser as wb

import pyttsx3
from decouple import config
from datetime import datetime
USERNAME = 'Temmie'
BOTNAME = 'Jarvis'

engine = pyttsx3.init('sapi5')

# Set Rate
engine.setProperty('rate', 190)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice (Female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

import speech_recognition as sr
from random import choice
import utils

def speak(text):
    """Used to speak whatever text is passed to it"""
    engine.say(text)
    engine.runAndWait()

def take_user_input():
    """Takes user input, recognizes it using Speech Recognition module and converts it into text"""
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')

        if not 'exit' in query or 'stop' in query:
            speak(choice(opening_text))

        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night sir, take care!")

            else:
                speak('Have a good day sir!')

            exit()

    except Exception:
        speak('Sorry, I could not understand. Could you please say that again?')
        query = 'None'
    return query

opening_text = [
    "Cool, I'm on it sir.",
    "Okay sir, I'm working on it.",
    "Just a second sir.",
    "Working on it.",
    "Alright, on it already!",
]

paths = {
    'notepad': "C:\\Windows\\system32\\notepad.exe",
    'discord': "https://discord.com/channels/@me",
    'calculator': "C:\\Windows\\System32\\calc.exe",
    'youtube': "https://www.youtube.com/"
}

def kill_power():
    os.system("shutdown -s -t 1")

def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)

def open_notepad():
    sp.Popen(paths['notepad'])

def open_cmd():
    os.system('start cmd')

def open_discord():
    wb.open_new_tab(paths["discord"])

def open_calculator():
    sp.Popen(paths['calculator'])

def open_youtube():
    wb.open_new_tab(paths['youtube'])

import requests
import wikipedia
import pywhatkit as kit
from decouple import config

def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address

def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences=1)
    return results

def play_on_youtube(video):\
    kit.playonyt(video)

def search_on_google(query):
    kit.search(query)

def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }

    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]

def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']

import time as t

def tell_time():
    current_time = t.strftime("%I:%M:%S")
    return current_time

from tkinter import *
import tkinter.font
import time

def display_time():
    root= Tk()
    root.geometry("400x100")
    root.config(bg='black')

    def update():
        clock.config(text=time.strftime("%I:%M:%S"))
        clock.after(1000,update)

    myfont = tkinter.font.Font(family = "Dosis Inconsolata", size = 40,weight =  "bold")
    clock = Label(root, background = 'black',foreground = 'white', font = myfont)
    clock.pack()
    update()
    root.title('clock')
    root.mainloop()

from JARVIS import USERNAME
	
# OpenCV program to detect face in real time 
def display_you():
	# import libraries of python OpenCV 
	# where its functionality resides 
	import cv2 
     
	face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml') 
	eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_eye.xml') 
	smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_smile.xml') 

	def detect(gray, frame): 
		faces = face_cascade.detectMultiScale(gray, 1.3, 5) 
          
		for (x, y, w, h) in faces: 
			cv2.rectangle(frame, (x, y), ((x + w), (y + h)), (0, 255, 0), 2) 
			roi_gray = gray[y:y + h, x:x + w] 
			roi_color = frame[y:y + h, x:x + w] 
			smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 20) 

			for (sx, sy, sw, sh) in smiles: 
				cv2.rectangle(roi_color, (sx, sy), ((sx + sw), (sy + sh)), (0, 255, 0), 2)  
                    
		# loop over the detected faces
		for (x,y,w,h) in faces:
			roi_gray = gray[y:y+h, x:x+w]
			roi_color = frame[y:y+h, x:x+w]
               
			# detects eyes of within the detected face area (roi)
			eyes = eye_cascade.detectMultiScale(roi_gray)
			
			# draw a rectangle around eyes
			for (ex,ey,ew,eh) in eyes:
				cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                    
		return frame


	video_capture = cv2.VideoCapture(0) 
	while video_capture.isOpened(): 
	# Captures video_capture frame by frame 
		_, frame = video_capture.read() 

		# To capture image in monochrome					 
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
		# calls the detect() function	 
		canvas = detect(gray, frame)

		# Displays the result on camera feed					 
		cv2.imshow(f'{USERNAME}', canvas) 

		# The control breaks once q key is pressed						 
		if cv2.waitKey(1) & 0xff == ord('q'):			 
			break

	# Release the capture once all the processing is done. 
	video_capture.release()								 
	cv2.destroyAllWindows() 

def News():
    import requests 
    from bs4 import BeautifulSoup 


    url = 'https://www.bbc.com/news'
    response = requests.get(url) 
    
    soup = BeautifulSoup(response.text, 'html.parser') 
    headlines = soup.find('body').find_all('h3') 
    unwanted = ['BBC World News TV', 'BBC World Service Radio', 
                'News daily newsletter', 'Mobile app', 'Get in touch'] 
    
    heads = []
    for x in list(dict.fromkeys(headlines)): 
        if x.text.strip() not in unwanted: 
            heads.append(x.text.strip())
    SpeakHead = []
    for i in range(5):
        SpeakHead.append(heads[i])
    return SpeakHead

def Anime_play(anime):
     wb.open_new("https://www.wcostream.tv/"+anime)

from GUITest import *
def GUI(x):
    RUNMAIN(x)
