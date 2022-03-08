import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import socket
import sys


host = 'neave.hopto.org'
port = 7052 #random


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_initial_command():
    try:
        with sr.Microphone() as source:
            watch = 'empty'
            listener.adjust_for_ambient_noise(source)
            print('listening for watch word...')
            voice = listener.listen(source)
            watch = listener.recognize_google(voice)
            watch = watch.lower()
            print(watch)
    except KeyboardInterrupt:
        exit(0)
    except:
        pass
    return watch

def take_command():
    try:
        with sr.Microphone() as source:
            command = 'empty'
            listener.adjust_for_ambient_noise(source)
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'neptune' in command:
                command = command.replace('neptune', '')
                print(command)
    except KeyboardInterrupt:
        exit(0)
    except:
        pass
    return command        

    


def run_neptune():
    command = take_command()
    print('user: ' + command)
    if 'empty' == command:
        print('I did not catch that')
        talk('I did not catch that')
    elif 'display' in command:
        print("sending to LCD")
        talk("sending to LCD")
        send_to_server(command.upper())
    elif 'kill' in command:
        exit("SUCCESSFUL RUN OF PROGRAM")
    elif 'play' in command:
        song = command.partition('play')[2]
        print('playing ' + song)
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'led' in command:
        send_to_server("GPIO "+command)
    elif 'buzz' in command:
        send_to_server("GPIO "+command)
    elif 'buzz' and 'one time' in command:
        send_to_server("GPIO "+command)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('Current time is ' + time)
        talk('Current time is ' + time)
    elif 'what is' in command:
        person = command.replace('what is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'bye' in command:
        talk("Until we meet again")
        watch_for_call()
    else:
        talk('I did not catch that')

def watch_for_call():
    while True:
        watch_word = take_initial_command()

        if watch_word == 'hello neptune':
            talk("Hello...I am neptune your Personal Assistant")
            talk("how can i help you?")
            while True:
                run_neptune()




def send_to_server(command):
    if command == "EXIT":
        #send EXIT request to the server pi
        s.send(str.encode(command))
        s.close()
    elif command == "KILL":
        #send KILL request to server pi
        s.send(str.encode(command))
        s.close()
    s.send(str.encode(command))
    reply = s.recv(1024)
    print(reply.decode('utf-8'))



watch_for_call()
