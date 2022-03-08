import RPi.GPIO as GPIO
from time import sleep
import sys
sys.path.insert(0, '/home/pi/lcd')
import drivers

display = drivers.Lcd()
display.lcd_backlight(0)
R_LED = 18
Y_LED = 4
W_LED = 17
BUZZER = 27
B_LED = 22


def clean():
    GPIO.cleanup()
    print("cleaned")

def red_led_on():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(R_LED, GPIO.OUT)
    GPIO.output(R_LED, GPIO.HIGH)
def red_led_off():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(R_LED, GPIO.OUT)
    GPIO.output(R_LED, GPIO.LOW)
def red_led_blink():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(R_LED, GPIO.OUT)
    n=5
    #n = int(input("How many times?: "))
    
    for i in range(n):
        red_led_on()
        sleep(0.4)
        red_led_off()
        sleep(0.4)
    clean()
    

def yellow_led_on():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Y_LED, GPIO.OUT)
    GPIO.output(Y_LED, GPIO.HIGH)
def yellow_led_off():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Y_LED, GPIO.OUT)
    GPIO.output(Y_LED, GPIO.LOW)
def yellow_led_blink():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Y_LED, GPIO.OUT)
    
    n=5
    #n = int(input("How many times?: "))
    for i in range(n):
        yellow_led_on()
        sleep(0.4)
        yellow_led_off()
        sleep(0.4)
    clean()
    
def white_led_on():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(W_LED, GPIO.OUT)
    GPIO.output(W_LED, GPIO.HIGH)
def white_led_off():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(W_LED, GPIO.OUT)
    GPIO.output(W_LED, GPIO.LOW)
def white_led_blink():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(W_LED, GPIO.OUT)
    
    n=5
    #n = int(input("How many times?: "))
    for i in range(n):
        white_led_on()
        sleep(0.4)
        white_led_off()
        sleep(0.4)
    clean()
    
def buzzer_beep_five():
    for i in range(5):
        buzzer_beep()
    
def buzzer_beep():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUZZER, GPIO.OUT)
    
    n=1
    #n = int(input("How many times?: "))
    for i in range(n):
        GPIO.output(BUZZER, GPIO.HIGH)
        sleep(0.4)
        GPIO.output(BUZZER, GPIO.LOW)
        sleep(0.4)
    clean()
    
def blue_led_on():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(B_LED, GPIO.OUT)
    GPIO.output(B_LED, GPIO.HIGH)
def blue_led_off():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(B_LED, GPIO.OUT)
    GPIO.output(B_LED, GPIO.LOW)
def blue_led_blink():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(B_LED, GPIO.OUT)
    
    n=5
    #n = int(input("How many times?: "))
    for i in range(n):
        blue_led_on()
        sleep(0.4)
        blue_led_off()
        sleep(0.4)
    clean()
    
    
def long_string(display, text='', num_line=1, num_cols=16):
    """
    Parameters: (driver, string to print, number of line to print, number of columns of your display)
    Return: This function send to display your scrolling string.
    """
    if len(text) > num_cols:
        display.lcd_display_string(text[:num_cols], num_line)
        sleep(1)
        for i in range(len(text) - num_cols + 1):
            text_to_print = text[i:i+num_cols]
            display.lcd_display_string(text_to_print, num_line)
            sleep(0.5)
        sleep(1)
    else:
        display.lcd_display_string(text, num_line)
        
def display_message(text):
    msg = text
    display.lcd_backlight(1)
    long_string(display, "Message:", 1)
    sleep(0.2)
    long_string(display, msg, 2)
    sleep(3)
    display.lcd_clear()
    display.lcd_backlight(0)
    
if __name__ == "__main__":
    display_message("loooooong textttttttt")
    red_led_blink()
    yellow_led_blink()
    white_led_blink()
    blue_led_blink()
    
    buzzer_beep()
    clean()



    
