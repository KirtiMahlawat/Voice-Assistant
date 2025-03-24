import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
import pyautogui
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning Mam")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon Mam !")   
  
    else:
        speak("Good Evening Mam !")  
  
    assname =("Kiki 1 point o")
    speak("I am your Assistant")
    speak(assname)
     
 
def username():
    speak("What should i call you Mam")
    uname = takeCommand()
    speak("Welcome Miss")
    speak(uname)
    columns = shutil.get_terminal_size().columns
     
    print("#####################".center(columns))
    print("Welcome Miss.", uname.center(columns))
    print("#####################".center(columns))
     
    speak("How can i Help you, Sir")
 
def takeCommand():
     
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
         
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
  
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
  
    except Exception as e:
        print(e)    
        print("Unable to Recognize your voice.")  
        return "None"
     
    return query
  
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
     
    # Enable low security in gmail
    server.login('your email id', 'your email password')
    server.sendmail('your email id', to, content)
    server.close()

def defineWord():
    speak("What word would you like me to define?")
    word_to_define = takeCommand()
    speak(f"The definition of {word_to_define} is not available at the moment.")

def recommendTravelDestination():
    speak("What type of travel destination are you interested in?")
    destination_type = takeCommand()
    speak(f"I'm sorry, I'm not configured to recommend {destination_type} destinations yet.")

def playGame():
    speak("Great! Let's play a game. What type of game would you like to play?")
    game_choice = takeCommand()
    if 'guess the number' in game_choice:
        speak("Sure! I'm thinking of a number between 1 and 10. Try to guess it.")

def translatePhrase():
    speak("What phrase would you like me to translate?")
    phrase_to_translate = takeCommand()
    speak("In which language would you like to translate it?")
    target_language = takeCommand()
    speak(f"I'm sorry, I'm not configured to translate phrases yet.")

def tellRiddle():
    speak("Sure! Here's a riddle for you: I speak without a mouth and hear without ears. What am I?")

def recommendLearningPlatform():
    speak("What subject or skill would you like to learn?")
    learning_topic = takeCommand()
    speak(f"I'm sorry, I'm not configured to recommend learning platforms for {learning_topic} yet.")
 

if __name__ == '__main__':
    clear = lambda: os.system('cls')
     
    # This Function will clean any
    # command before execution of this python file
    clear()
    wishMe()
    username()
     
    while True:
         
        query = takeCommand().lower()
         
        # All the commands said by user will be 
        # stored here in 'query' and will be
        # converted to lower case for easily 
        # recognition of command
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
 
        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")
 
        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")
 
        elif 'open stackoverflow' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")  
            
        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")
            speak("Opening WhatsApp. Please scan the QR code to log in.") 
            
        elif 'open chatgpt' in query:
            webbrowser.open("https://www.openai.com/chatgpt/")
            speak("Opening ChatGPT website.")
    
        elif 'play music' in query or "play song" in query:
            speak("Here you go with music")
            add = "Music"
            listsong = os.listdis(add)
            print(listsong)  
            os.startfile(os.path.join(add,listsong[1]))  
         
 
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("% H:% M:% S")    
            speak(f"Sir, the time is {strTime}")
            
        elif 'web' in query:
            webbrowser.open("https://svsu.ac.in/") 
 
        elif 'open opera' in query:
            codePath = r"C:\\Users\\KIRTI\\AppData\\Local\\Programs\\Opera\\launcher.exe"
            os.startfile(codePath)
 
        elif 'email to kirti' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "Receiver email address"   
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")
 
        elif 'send a mail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("whome should i send")
                to = input()    
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")
 
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Mam")
 
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
 
        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            assname = query
 
        elif "change name" in query:
            speak("What would you like to call me, Mam ")
            assname = takeCommand()
            speak("Thanks for naming me")
 
        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak(assname)
            print("My friends call me", assname)
 
        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()
 
        elif "who made you" in query or "who created you" in query: 
            speak("I have been created by Kirti.")
             
        elif 'joke' in query:
            speak(pyjokes.get_joke())
             
        elif "calculate" in query: 
             
            app_id = "Wolframalpha api id"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate') 
            query = query.split()[indx + 1:] 
            res = client.query(' '.join(query)) 
            answer = next(res.results).text
            print("The answer is " + answer) 
            speak("The answer is " + answer) 
 
        elif 'search' in query or 'play' in query:
             
            query = query.replace("search", "") 
            query = query.replace("play", "")          
            webbrowser.open(query) 
 
        elif "who i am" in query:
            speak("If you talk then definitely your human.")
 
        elif "why you came to world" in query:
            speak("Thanks to Kirti. further It's a secret")
 
        elif 'power point presentation' in query:
            speak("opening Power Point presentation")
            power = r"C:\\Users\\GAURAV\\Desktop\\Minor Project\\Presentation\\Voice Assistant.pptx"
            os.startfile(power)
 
        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")
 
        elif "who are you" in query:
            speak("I am your virtual assistant created by Kirti")
 
        elif 'reason for you' in query:
            speak("I was created as a Minor project by Miss Kirti ")
 
        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20, 
                                                       0, 
                                                       "Location of wallpaper",
                                                       0)
            speak("Background changed successfully")
 
        elif 'open bluestack' in query:
            appli = r"C:\\ProgramData\\BlueStacks\\Client\\Bluestacks.exe"
            os.startfile(appli)
 
        elif 'news' in query:
             
            try: 
                jsonObj = urlopen('''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''')
                data = json.load(jsonObj)
                i = 1
                 
                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============'''+ '\n')
                 
                for item in data['articles']:
                     
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:
                 
                print(str(e))
 
         
        elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()
 
        elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')
                 
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")
 
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop Kiki 1 point O from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)
 
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")
 
        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Kiki 1 point O Camera ", "img.jpg")
 
        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])
             
        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")
 
        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])
 
        elif "write a note" in query:
            speak("What should i write, mam")
            note = takeCommand()
            file = open('Kiki 1 point O.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
         
        elif "show note" in query:
            speak("Showing Notes")
            file = open("Kiki 1 point O.txt", "r") 
            print(file.read())
            speak(file.read(6))
            
        elif 'take a screenshot' in query:
            screenshot = pyautogui.screenshot()
            screenshot.save('screenshot.png')
            speak("Screenshot taken")
        
        elif 'find a coding tutorial' in query:
            speak("What programming language or topic are you interested in?")
            tutorial_query = takeCommand()
            webbrowser.open(f"https://www.youtube.com/results?search_query={tutorial_query}+tutorial")
            
        elif'tell me a programming joke' in query:
            joke = pyjokes.get_joke(language="en", category="programming")
            speak(joke)

        elif 'open calendar' in query:
            os.system("start outlookcal:")

        elif 'take a note' in query:
            speak("What should I note down?")
            note_content = takeCommand()
            with open("notes.txt", "a") as file:
                file.write(f"{datetime.datetime.now()}: {note_content}\n")
            speak("Note taken and saved.")

        elif 'read my notes' in query:
            try:
                with open("notes.txt", "r") as file:
                    notes = file.read()
                    speak("Here are your notes:")
                    speak(notes)
            except FileNotFoundError:
                speak("You don't have any notes yet.")

        elif 'take a screenshot' in query:
            screenshot = pyautogui.screenshot()
            screenshot.save('screenshot.png')
            speak("Screenshot taken.")

        elif 'check my emails' in query:
            speak("Sorry, I'm not configured to check your emails yet.")

        elif 'play a random song' in query:
            music_folder = "Path to your music folder"
            songs = os.listdir(music_folder)
            random_song = random.choice(songs)
            os.startfile(os.path.join(music_folder, random_song))
            speak("Playing a random song for you.")

        elif 'tell me a fun fact' in query:
            speak("I'm sorry, I'm not configured to provide fun facts yet.")

        elif 'open notepad' in query:
            os.startfile("notepad.exe")

        elif 'check my calendar' in query:
            speak("Sorry, I'm not configured to check your calendar yet.")

        elif 'translate' in query:
            speak("Sorry, I'm not configured to translate languages yet.")

        elif 'tell me a quote' in query:
            quote = "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt"
            speak(quote)

        elif 'open file explorer' in query:
            os.startfile("explorer.exe")
            
        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke(language="en", category="neutral")
            print(joke)
            speak(joke)
            
        elif 'reminder' in query:
            speak("Sorry, I'm not configured to set reminders yet.")
            
        elif "update assistant" in query:
            speak("After downloading file please replace this file with the downloaded one")
            url = '# url after uploading file'
            r = requests.get(url, stream = True)
             
            with open("Voice.py", "wb") as Pypdf:
                 
                total_length = int(r.headers.get('content-length'))
                 
                for ch in progress.bar(r.iter_content(chunk_size = 2391975),
                                       expected_size =(total_length / 1024) + 1):
                    if ch:
                      Pypdf.write(ch)
        
        elif 'compose an email' in query:
            speak("Who is the recipient?")
            recipient = takeCommand()
            speak("What should be the subject?")
            subject = takeCommand()
            speak("What would you like to say?")
            body = takeCommand()
            try:
                sendEmail(recipient, f"Subject: {subject}\n\n{body}")
                speak("Email sent successfully.")
            except Exception as e:
                print(e)
                speak("Sorry, I'm unable to send the email.")

        elif 'search for a recipe' in query:
            speak("What recipe would you like to search for?")
            recipe_query = takeCommand()
            webbrowser.open(f"https://www.allrecipes.com/search/results/?wt={recipe_query}")

        elif 'tell me the latest technology news' in query:
            speak("I'm sorry, I'm not configured to provide technology news yet.")

        elif 'set a timer' in query:
            speak("For how many minutes should I set the timer?")
            try:
                timer_minutes = int(takeCommand())
                timer_seconds = timer_minutes * 60
                time.sleep(timer_seconds)
                speak(f"Timer for {timer_minutes} minutes is complete.")
            except ValueError:
                speak("Invalid input. Please provide a valid number.")

        elif 'find a nearby restaurant' in query:
            speak("What type of cuisine are you interested in?")
            cuisine_type = takeCommand()
            webbrowser.open(f"https://www.google.com/maps/search/{cuisine_type}+restaurants")

        elif 'tell me a science fact' in query:
            speak("I'm sorry, I'm not configured to provide science facts yet.")
                
        elif 'play a game' in query:
            speak("Sure! Let's play a game. What type of game would you like to play?")
            game_choice = takeCommand()
            if 'guess the number' in game_choice:
                speak("Great! I'm thinking of a number between 1 and 10. Try to guess it.")
        
        elif 'translate a phrase' in query:
            speak("Sure! What phrase would you like me to translate?")
            phrase_to_translate = takeCommand()
            speak("In which language would you like to translate it?")
            target_language = takeCommand()
            speak(f"I'm sorry, I'm not configured to translate phrases yet.")

        elif 'tell me a riddle' in query:
            speak("Sure! Here's a riddle for you: I speak without a mouth and hear without ears. What am I?")

        elif 'recommend a learning platform' in query:
            speak("What subject or skill would you like to learn?")
            learning_topic = takeCommand()
            
        # NPPR9-FWDCX-D2C8J-H872K-2YT43
        elif "jarvis" in query:
             
            wishMe()
            speak("Kiki 1 point o in your service Miss")
            speak(assname)
 
        elif "weather" in query:
             
            # Google Open weather website
            # to get API of Open weather 
            api_key = "Api key"
            base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
            speak(" City name ")
            print("City name : ")
            city_name = takeCommand()
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            response = requests.get(complete_url) 
            x = response.json() 
             
            if x["code"] != "404": 
                y = x["main"] 
                current_temperature = y["temp"] 
                current_pressure = y["pressure"] 
                current_humidiy = y["humidity"] 
                z = x["weather"] 
                weather_description = z[0]["description"] 
                print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) gy="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description)) 
             
            else: 
                speak(" City Not Found ")
             
        elif "send message " in query:
                # You need to create an account on Twilio to use this service
                account_sid = 'Account Sid key'
                auth_token = 'Auth token'
                client = Client(account_sid, auth_token)
 
                message = client.messages \
                                .create(
                                    body = takeCommand(),
                                    from_='Sender No',
                                    to ='Receiver No'
                                )
 
                print(message.sid)
 
        elif "wikipedia" in query:
            webbrowser.open("wikipedia.com")
 
        elif "Good Morning" in query:
            speak("A warm" +query)
            speak("How are you Miss")
            speak(assname)
 
        # most asked question from google Assistant
        elif "will you be my gf" in query or "will you be my bf" in query:   
            speak("I'm not sure about, may be you should give me some time")
 
        elif "how are you" in query:
            speak("I'm fine, glad you me that")
 
        elif "i love you" in query:
            speak("It's hard to understand")
 
        elif "what is" in query or "who is" in query:
             
            # Use the same API key 
            # that we have generated earlier
            client = wolframalpha.Client("API_ID")
            res = client.query(query)
             
            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print ("No results")

        elif 'exit' in query:
            speak("Goodbye!")
            exit()
         
        # elif "" in query:
            # Command go here
            # For adding more commands