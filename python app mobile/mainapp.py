# -*- coding: utf-8 -*-
# Kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from mobile_driver import *

r1 = 0
b1 = 0
w1 = 0
y1 = 0
rb = 0
bb = 0
yb = 0
wb = 0
b1 = 0
b5 = 0
textmessage = ''


class HomeScreen(BoxLayout):
    def __init__(self, **kwargs):
        # Initiate Box Layout and change orientation to vertical
        super().__init__(**kwargs)
        self.orientation = "vertical"

        # Top Bar with Buttons "1", "2" & "3"
        self.top_bar = BoxLayout(orientation="horizontal", size_hint=(1, .1))
        self.top_bar.add_widget(Label(text="Neptune IoT", font_size= "50dp", color= [0.4, 0.8, 1, 1]))

        # Create the Gridlayout for the Scroll View and add height bounding
        self.contend_scroll_view = GridLayout(size_hint_y=None, row_default_height="100dp", cols=2, padding=[10,10,10,10], spacing = [10,10])
        self.contend_scroll_view.bind(minimum_height=self.contend_scroll_view.setter('height'))
    
        self.contend_scroll_view.add_widget(Button(text='Red LED', font_size= "20dp", on_press=r1_callback))
        self.contend_scroll_view.add_widget(Button(text='Blue LED', font_size= "20dp", on_press=b1_callback))
        self.contend_scroll_view.add_widget(Button(text='Yellow LED', font_size= "20dp", on_press=y1_callback))
        self.contend_scroll_view.add_widget(Button(text='White LED', font_size= "20dp", on_press=w1_callback))
        self.contend_scroll_view.add_widget(Button(text='Blink Red LED', font_size= "20dp"))
        self.contend_scroll_view.add_widget(Button(text='Blink Blue LED', font_size= "20dp"))
        self.contend_scroll_view.add_widget(Button(text='Blink Yellow LED', font_size= "20dp"))
        self.contend_scroll_view.add_widget(Button(text='Blink White LED', font_size= "20dp"))
        self.contend_scroll_view.add_widget(Button(text='Beep Buzzer', font_size= "20dp"))
        self.contend_scroll_view.add_widget(Button(text='Beep Buzzer 5 times', font_size= "20dp"))
        self.contend_scroll_view.add_widget(TextInput(hint_text='Message to display on LCD', font_size= "20dp"))
        self.contend_scroll_view.add_widget(Button(text='Display', font_size= "20dp", on_press=lcd_callback))


        # Add the contend to the Scroll View
        self.scroll_view = ScrollView()
        self.scroll_view.add_widget(self.contend_scroll_view)

        # Add the two Widgets to Home Screen
        self.add_widget(self.top_bar)
        self.add_widget(self.scroll_view)

def lcd_callback(self):
    print(textmessage)
    


def r1_callback(self):
    global r1
    if r1 == 0:
        self.background_color=[1,0,0,1]
    elif r1 == 1:
        r1 = 0
        self.background_color = [1,1,1,1]

def b1_callback(self):
    global b1
    if b1 == 0:
        self.background_color=[0,0,1,1]
    elif b1 == 1:
        b1 = 0
        self.background_color = [1,1,1,1]

def y1_callback(self):
    global y1
    if y1 == 0:
        self.background_color=[1,1,0,1]
    elif y1 == 1:
        y1 = 0
        self.background_color = [1,1,1,1]

def w1_callback(self):
    global w1
    if w1 == 0:
        self.background_color=[1,1,1,1]
    elif w1 == 1:
        w1 = 0
        self.background_color = [1,1,1,1]

class MyApp(App):
    def build(self):
        return HomeScreen()



if __name__ == '__main__':
    # Only runs if file is executed directly, but not if importet
    MyApp().run()