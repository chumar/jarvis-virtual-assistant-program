import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
# import pyaudio


engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') #getting details of current voice
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):

    engine.say(audio) 
    engine.runAndWait() #Without this command, speech will not be audible to us.

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=5 and hour<12:
        speak("Good Morning Sir! And best wishes for today.")

    elif hour>=12 and hour<17:
        speak("Good Afternoon Sir! and Hopefully you are doing good.")   

    elif hour>=17 and hour<21:
        speak("Good Evening Sir! And Hopefully you are well") 
    else:
        speak("Good Night Sir! And best wishes for tomorrow")   

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
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('umarsaleem9966@gmail.com', 'eknlhibasphujtdo')
    server.sendmail('umarsaleem9966@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    # takeCommand()
    while True:
    # if 1:
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak('youtube has been opened sir')
        elif 'open google' in query:
            webbrowser.open("google.com")
            speak('google has been opened sir')
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
            speak('stackoverflow has been opened sir')
        elif 'open gmail' in query:
            webbrowser.open("gmail.com")
            speak('gmail has been opened sir')
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
            speak('webbrowser has been opened sir')
        elif 'play music'  in query:
            music_dir = 'F:\\download songs'
            songs = os.listdir(music_dir)
            print(songs)     
            os.startfile(os.path.join(music_dir, songs[0]))
            speak('music is opened and enjoying sir.')
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in query:
            codePath ="C:\\Users\\Lap Tech\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak('headache is opened Sir')

        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "umarsaleem963@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email") 
        elif 'good working' in query:  
            speak(f"Thank you sir for appreciation. You are also good")  
        elif 'thank you' in query:  
            speak(f"Most welcome sir") 
        elif 'quit' in query:  
            speak(f"Okay sure Sir, I am quiting now. Please take care") 
            break  
 
 