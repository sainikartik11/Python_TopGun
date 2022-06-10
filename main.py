import pyttsx3
import smtplib
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import urllib.request
import re
import os

#global variables
email_addr=os.environ.get('EMAIL_ADDR')
email_pass=os.environ.get('EMAIL_PASS')
contacts={"kartik":"kartik21928@gmail.com","anshu":"anshu@gmail.com","kumar":"kumar@gmail.com"}


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


#functions are defined here
def speak(audio1):
    engine.say(audio1)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good evening")

    speak("I am your assistant ")
    speak(" How can i help you ")
    speak(" try out the following commands")
    print("try out the following commands :")
    print("follwing commands are supported")
    print("1--- search on wikipedia\n 2 ---open youtube \n 3 ---open stackoverflow \n 4 ---preparing for placement? \n 5 ---play music \n 6 ---send email \n 7--- play news \n 8--- show time \n 9--- show weather ")

def takeCommand():
        # It takes microphone input from the user and returns string output

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
        print("Say that again please...")  # Say that again will be printed in case of improper voice
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(email_addr,email_pass)
    server.sendmail('sainikartik2019@gmail.com', to, content)
    server.close()

#main function

if __name__== "__main__":
    wishme()
    bol=True
    while bol:
        query = takeCommand().lower()
    #logic 4 executing tasks based on query
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
            speak("Do you want your alexa to sleep")
            query2=takeCommand().lower()
            if 'yes' in query2:
                bol=False
        elif 'youtube' in query:
            webbrowser.open("youtube.com")
            speak("Do you want your alexa to sleep")
            query2 = takeCommand().lower()
            if 'yes' in query2:
                bol = False
        elif 'stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            speak("Do you want your alexa to sleep")
            query2 = takeCommand().lower()
            if 'yes' in query2:
                bol = False
        elif 'placement' in query:
            url='https://www.geeksforgeeks.org/a-complete-step-by-step-guide-for-placement-preparation-by-geeksforgeeks/'
            webbrowser.open_new(url)
            speak("Do you want your alexa to sleep")
            query2 = takeCommand().lower()
            if 'yes' in query2:
                bol = False
        elif 'play music' in query:
            print('name the song')
            q1 = takeCommand().lower()
            q1=q1.replace(" ","+") #to play video having multiple words ytube changes the word string with +
            url='https://www.youtube.com/results?search_query='+ q1
            html = urllib.request.urlopen('https://www.youtube.com/results?search_query='+ q1)
            video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())  #using regex i.e regualr expr to find unique ids of list of all related videos
            url='https://www.youtube.com/watch?v='+video_ids[0]    #appending the first video's unique id
            webbrowser.open(url)
            speak("Do you want your alexa to sleep")
            query2 = takeCommand().lower()
            if 'yes' in query2:
                bol = False
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            speak("Do you want your alexa to sleep")
            query2 = takeCommand().lower()
            if 'yes' in query2:
                bol = False
        elif 'weather' in query:
            webbrowser.open("windy.com")
            speak("Do you want your alexa to sleep")
            query2 = takeCommand().lower()
            if 'yes' in query2:
                bol = False
        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("Do you want your alexa to sleep")
            query2 = takeCommand().lower()
            if 'yes' in query2:
                bol = False
        elif 'news' in query:
            url='https://www.youtube.com/watch?v=dp8PhLsUcFE&ab_channel=BloombergQuicktake%3AOriginals'
            speak("Do you want your alexa to sleep")
            query2 = takeCommand().lower()
            if 'yes' in query2:
                bol = False
            webbrowser.open(url)
        elif ' email' in query:
            try:
                speak("whoem do you want to send email")
                query3=takeCommand().lower()
                speak("what do you want to convey")
                content= takeCommand().lower()
                if query3 in contacts:
                    to=contacts[query3]
                    print("the email id is:" + to)
                    sendEmail(to,content)
                    speak("email has been sent to:"+to)
                    print(content)
                else:
                    speak("the email id is not present in your contacts kindly tell the email id")
                    query4=takeCommand()
                    query4.replace(" ","")
                    to=query4
                    print("the email id is:"+to)
                    sendEmail(to,content)
                    speak("email has been sent to:"+ to)
                    print(content)
            except Exception as e:
                print(e)
                speak("sorry something went wrong")
            speak("Do you want your alexa to sleep")
            query2 = takeCommand().lower()
            if 'yes' in query2:
                bol = False
        elif 'sleep' in query:
            bol=False













