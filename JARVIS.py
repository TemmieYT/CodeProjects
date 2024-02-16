# Created by Temmie Amodo.
def greet_user():
    """Greets the user according to the time"""
    
    hour = datetime.now().hour

    if (hour >= 6) and (hour < 12):
        speak(f"Good Morning {USERNAME}")

    elif (hour >= 12) and (hour < 16):
        speak(f"Good afternoon {USERNAME}")

    elif (hour >= 16) and (hour < 19):
        speak(f"Good Evening {USERNAME}")

    else:
        speak(f"Welcome back! {USERNAME}")

    speak(f"I am {BOTNAME}. How may I assist you?")

import speech_recognition as sr
from random import choice
import utils

opening_text = [
    "Cool, I'm on it sir.",
    "Okay sir, I'm working on it.",
    "Just a second sir.",
]

from JARVISFunctions import *
import requests
from pprint import pprint


if __name__ == '__main__':
    greet_user()
    
    while True:
        query = take_user_input().lower()
        if 'open command prompt' in query or 'open cmd' in query:
            open_cmd()
        
        elif 'open notepad' in query:
            open_notepad()

        elif 'open camera' in query:
            open_camera()

        elif 'open calculator' in query:
            open_calculator()

        elif "open discord" in query:
            open_discord()

        elif "open youtube" in query:
            open_youtube()

        elif 'ip address' in query:
            ip_address = find_my_ip()
            speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
            print(f'Your IP Address is {ip_address}')

        elif 'wikipedia' in query:
            speak('What do you want to search on Wikipedia, sir?')
            search_query = take_user_input().lower()
            results = search_on_wikipedia(search_query)
            speak(f"According to Wikipedia, {results}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(results)

        elif 'play on youtube' in query:
            speak('What do you want to play on Youtube, sir?')
            video = take_user_input().lower()
            play_on_youtube(video)

        elif 'search on google' in query:
            speak('What do you want to search on Google, sir?')
            query = take_user_input().lower()
            search_on_google(query)

        elif 'joke' in query:
            speak(f"Hope you like this one sir")
            joke = get_random_joke()
            speak(joke)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(joke)

        elif "advice" in query:
            speak(f"Here's an advice for you, sir")
            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(advice)

        elif "goodbye" in query:
            speak(f"It was nice talking to you, {USERNAME}")
            speak("Quitting...")
            exit()

        elif "time" in query:
            current_time = tell_time()
            speak(current_time)
            speak("for your convenience sir, I am printing it on the screen")
            display_time()

        elif "kill power" in query:
            speak("Shutting down all systems... Goodbye, Sir.")
            kill_power()

        elif "face" in query:
            speak("Here is you, sir")
            display_you()

        elif "news" in query:
            speak("the first five headlines are ")
            speak(News())
            speak("For your convenience sir, I will print it on the screen")
            print(str(News()).replace("[","").replace("]","").replace(",","\n"))

        elif "anime" in query:
            speak("what anime do you want to watch?: ")
            anime = take_user_input().lower().replace(" ","-")
            Anime_play(anime)
