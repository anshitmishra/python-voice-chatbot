import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
engin = pyttsx3.init('sapi5')
voices = engin.getProperty('voices')
engin.setProperty('voice', voices[0].id)


def speak(audio):
    engin.say(audio)
    engin.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning sir!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon sir!")
    else:
        speak("Good Evening sir!")
    takeCommand()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        r.energy_threshold = 500
        audio = r.listen(source)

    try:
        print("recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f'user said: {query}\n')

    except:
        print("say that again please")
        return "none"
    return query


if __name__ == '__main__':
    wishMe()
    

    while True:
        commands = takeCommand().lower()

        if 'sunday tell me about' in commands:
            speak('Sir Searching on Wikipedia...')
            commands = commands.replace("sunday tell me about", "")
            results = wikipedia.summary(commands, sentences=2)
            speak(f"Sir I found something About {commands} on wikipedia")
            speak(f'According to wikipedia {results}')
        elif 'sunday open chrome' in commands:
            speak('Sir Opening Chrome...')
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            urL = "https://github.com/anshitmishra"
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(urL)
        elif 'open chrome' in commands:
            speak('Sir Opening Chrome...')
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            urL = "https://github.com/anshitmishra"
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(urL)
        elif 'sunday search' in commands:
            speak('Sir Opening Chrome and searching...')
            commands = commands.replace("sunday search", "")
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            urL = str(f"https://www.google.com/search?q={commands}")
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(urL)
        elif 'sunday sleep' in commands:
            break
        
        
