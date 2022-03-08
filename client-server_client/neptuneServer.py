import RPi.GPIO as GPIO
from time import sleep
import sys
sys.path.insert(0, '/home/pi/lcd')
import drivers
import socket
from neptuneExternals import *

display = drivers.Lcd()
display.lcd_backlight(0)
R_LED = 18
Y_LED = 4
W_LED = 17
BUZZER = 27
B_LED = 22

host = ''
port = 7052


stored_value = "Hey! I am the Neptune Server"

def setup_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created.")
    try:
        s.bind((host, port))
    except socket.error as error:
        print(error)
    print("Socket bind completed.")
    return s

def setup_connection():
    s.listen(1) #the other pi
    conn, addr = s.accept()
    print("Connected to:"+addr[0]+":"+str(addr[1]))
    return conn

def GET():
    return stored_value

def REPEAT(data_message):
    return data_message[1]

def DISPLAY(text):
    display_message(text)

def GPIO_commands(command):
    print(command)
    if 'led' in command:
        command.replace('led', '')

        if 'yellow' in command:
            command.replace('yellow','')
            if 'on' in command:
                yellow_led_on()
                return "Turned on Yellow LED."
            elif 'off' in command:
                yellow_led_off()
                return "Turned off Yellow LED."
            elif 'blink' in command:
                yellow_led_blink()
                return "Blinking Yellow LED 5 times..."
            else:
                return "I did not understand what to do with the Yellow LED."
        elif 'red' in command:
            command.replace('red','')
            if 'on' in command:
                red_led_on()
                return "Turned on Red LED."
            elif 'off' in command:
                red_led_off()
                return "Turned off Red LED."
            elif 'blink' in command:
                red_led_blink()
                return "Blinking Red LED 5 times..."
            else:
                return "I did not understand what to do with the Red LED."
        elif 'white' in command:
            command.replace('white','')
            if 'on' in command:
                white_led_on()
                return "Turned on White LED."
            elif 'off' in command:
                white_led_off()
                return "Turned off White LED."
            elif 'blink' in command:
                white_led_blink()
                return "Blinking White LED 5 times..."
            else:
                return "I did not understand what to do with the White LED."
        elif 'blue' in command:
            command.replace('blue','')
            if 'on' in command:
                blue_led_on()
                return "Turned on Blue LED."
            elif 'off' in command:
                blue_led_off()
                return "Turned off Blue LED."
            elif 'blink' in command:
                blue_led_blink()
                return "Blinking Blue LED 5 times..."
            else:
                return "I did not understand what to do with the Blue LED."
        elif 'warm' in command:
            command.replace('warm','')
            if 'on' in command:
                red_led_on()
                yellow_led_on()
                return "Turned on warm colours."
            elif 'off' in command:
                red_led_off()
                yellow_led_off()
                return "Turned off warm colours"
            else:
                return "Please specify an action"
        elif 'cool' in command:
            command.replace('cool','')
            if 'on' in command:
                blue_led_on()
                white_led_on()
                return "Turned on cool colours."
            elif 'off' in command:
                blue_led_off()
                white_led_off()
                return "Turned off cool colours"
            else:
                return "Please specify an action"
        elif 'all' in command:
            command.replace('all','')
            if 'on' in command:
                red_led_on()
                blue_led_on()
                yellow_led_on()
                white_led_on()
                return "Turned on LEDs"
            elif 'off' in command:
                red_led_off()
                blue_led_off()
                yellow_led_off()
                white_led_off()
                clean()
                return "Turned off LEDs"
            else:
                return "I'm not sure what you want all the LEDs to do."
        else:
            return "Did not understand which colour you want to perform action on."
    elif 'buzzer' in command:
        command.replace('buzzer','')
        if 'buzz' in command:
            command.replace('buzz','')
            if 'one time' in command:
                buzzer_beep()
                return "Beep"
            else:
               buzzer_beep_five()
               return "Beep Beep Beep Beep Beep"
        else:
            return "I'm sorry I don't understand what you want me to do with the buzzer."
    else:
        return "I'm not sure i can do that yet"
                
 

def data_transfer(conn):
    # send and receives data until told otherwise
    while True:
        # receive data
        data = conn.recv(1024)#buffer size
        data = data.decode('utf-8')
        data_message = data.split(' ',1)
        command_type = data_message[0]
        if command_type == "GET":
            reply = GET()
        elif command_type == "REPEAT":
            reply = REPEAT(data_message)
        elif command_type == "DISPLAY":
            DISPLAY(data_message[1])
            reply = "Displayed on LCD"
        elif command_type == "GPIO":
            reply = GPIO_commands(data_message[1].lower())
        elif command_type == "EXIT":
            print("Sad to see you leave :(")
            break
        elif command_type == "KILL":
            print("Shutting down Neptune Server")
            s.close()
            break
        else:
            reply = "Unknown command."
            print(reply)
        
        #send the data back to the client
        conn.sendall(str.encode(reply))
        print("Data has been sent to client")
    conn.close()

            
s = setup_server()

while True:
    try:
        conn = setup_connection()
        data_transfer(conn)
    except:
        clean()
        break
    


