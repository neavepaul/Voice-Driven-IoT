import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 170)
voices = engine.getProperty('voices')


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_initial_command():
    try:
        with sr.Microphone() as source:
            
            print('listening for watch word...')
            voice = listener.listen(source)
            watch = listener.recognize_google(voice)
            watch = watch.lower()
            print(watch)
    except Exception as ex:
        print(ex)
    return watch

def take_command():
    try:

        with sr.Microphone() as source:

            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'neptune' in command:
                command = command.replace('neptune', '')
                print(command)
    except Exception as ex:
        print(ex)
    return command        

    


def run_neptune():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.partition('play')[2]
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'what is' in command:
        person = command.replace('what is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'bye' in command:
        talk("Until we meet again")
        watch_for_call()
    else:
        talk('Please say the command again.')

def watch_for_call():
    while True:
        watch_word = take_initial_command()

        if watch_word == 'hello neptune':
            talk("Hello!! I am neptune your personal A I")
            talk("how can i help you?")
            while True:
                run_neptune()

watch_for_call()