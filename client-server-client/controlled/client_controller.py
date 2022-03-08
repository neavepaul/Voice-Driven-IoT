import socket
import pickle
from time import sleep
import RPi.GPIO as GPIO
import sys
sys.path.insert(0, '/home/pi/lcd')
import drivers
from neptuneExternals import *

HEADERSIZE = 10
client = {'R_LED': 0, 'Y_LED': 0, 'W_LED': 0, 'B_LED': 0, 'BUZZER_1': 0, 'BUZZER_5': 0, 'DISPLAY': ''}

host = 'neave.hopto.org'
port = 7052 #random

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

def update_devices(client):
    """UPDATE THE PHYSICAL STATES OF ALL DEVICES"""
    text = client.get("DISPLAY")
    if client.get('R_LED') == 1:
        red_led_on()
    if client.get('Y_LED') == 1:
        yellow_led_on()
    if client.get('B_LED') == 1:
        blue_led_on()
    if client.get('W_LED') == 1:
        white_led_on()
    if client.get('R_LED') == 0:
        red_led_off()
    if client.get('Y_LED') == 0:
        yellow_led_off()
    if client.get('B_LED') == 0:
        blue_led_off()
    if client.get('W_LED') == 0:
        white_led_off()
    if client.get('BUZZER_1') == 1:
        buzzer_beep()
        client.update({'BUZZER_1':0})
    if client.get('BUZZER_5') == 1:
        buzzer_beep_five()
        client.update({'BUZZER_5':0})
    if text != '':
        display_message(text)
        client.update({'DISPLAY':''})
    else:
        pass

while True:
    command = "UPDATE"
    msg = pickle.dumps(command, -1)
    msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+msg
    s.send(msg)

    full_msg = b''
    new_msg = True
    msg = s.recv(1024)

    if new_msg:
        msglen = int(msg[:HEADERSIZE])
        new_msg = False

    full_msg += msg

    if len(full_msg)-HEADERSIZE == msglen:
        incoming = pickle.loads(full_msg[HEADERSIZE:])
        if type(incoming) is dict:
            client.update(incoming)
            print("new client")
            print(client)
            update_devices(client)

        else:
            print("I GOT SOME UN-RECOGNIZED SHIT.")

        new_msg = True
        full_msg = b''
        sleep(1)
        
    if client.get('KILL') == 1:
        s.close()
        clean()
        break

