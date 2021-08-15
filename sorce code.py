import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import os
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    print("Skynet: ", audio)
  
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if True:
        speak("Welcome Back sir!")
        speak("How may I help you sir!")

def takecommand():
    r = sr.Recognizer() #Speech recognition means that when humans are speaking, a machine understands it. Here we are using Google Speech API
                        # in Python to make it happen. We need to install the following packages for this − Pyaudio 
    with sr.Microphone()as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)  #adjust_for_ambient_noise(source, duration = 1) Adjusts the energy threshold dynamically using audio from source 
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You: {query}\n")
        
       
    except Exception as e:
        print(e)
        print("Sorry I didnt get that , Please say that again")
        speak("Sorry I didnt get that , Please say that again")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takecommand().lower()  #lower means here to take query in lower-case alphabets

        if 'wikipedia' in query:
            speak("Searching wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https:\\www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("https:\\www.google.com")

        elif 'play music' in query:
            music_dir ='C:\\Users\Sagar Solanki\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            
