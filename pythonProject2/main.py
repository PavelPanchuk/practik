#!/usr/bin/python
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.lang import Builder
import threading
import time
import os.path
from kivy.config import Config
import datetime


Config.set('kivy','window_icon','work-time.png')

#android.minapi = 25


check_file = os.path.exists('practikDB.txt') # создани фали техт который является базой данных активностей
if (check_file ==False):
    my_file = open("practikDB.txt", "w+")

#Window.clearcolor = (0,75,0,130)

kv = '''
FloatLayout:
    

    ScrollView:
    
        pos_hint: {'left': 1, 'top': 1}
        size_hint_y: 0.5
        do_scroll_x: 1
        
        Label:
            id: debugarea
            size_hint: None, None
            size: self.texture_size
            
            
    Button:
        pos: 0,0
        size_hint_y: .1
        size_hint_x: .3
        text: 'отдых'
        on_release:
            app.do_print(x=1)
            self.text = 'остановить' if app.is_printing else 'отдых'

    Button:
        pos:0,100
        size_hint_y: .1
        size_hint_x: .3

        text: 'работа'
        on_release:
            app.do_print(x=2)
            self.text = 'остановить' if app.is_printing else 'работа'


    Button:
        pos:300,0
        size_hint_y: .1
        size_hint_x: .3

        text: 'учеба'
        on_release:
            app.do_print(x=3)
            self.text = 'остановить' if app.is_printing else 'учеба'
    Button:
        pos:0,200
        size_hint_y: .1
        size_hint_x: .3

        text: 'сон'
        on_release:
            app.do_print(x=4)
            self.text = 'остановить' if app.is_printing else 'сон'
    Button:
        pos:300,100
        size_hint_y: .1
        size_hint_x: .3

        text: 'спорт'
        on_release:
            app.do_print(x=5)
            self.text = 'остановить' if app.is_printing else 'спорт'
    Button:
        pos:300,200
        size_hint_y: .1
        size_hint_x: .3

        text: 'история'
        on_release:
            app.do_print(x=6)

'''

class MainApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.is_printing = False
        self.print_thread = None
        self.root_widget = Builder.load_string(kv)

    def build(self):
        self.icon = 'work-time.png'
        return self.root_widget

    def relax(self):

        i = 0

        while self.is_printing:
            self.root_widget.ids['debugarea'].text = f'вы отдыхаете {str(datetime.timedelta(seconds=i))}' + '\n'
            i += 1
            time.sleep(1)
        with open("practikDB.txt", "r") as f:
            text = f.read()
        f = open('practikDB.txt', 'w')
        f.write(text + "вы отдыхали:=" + str(datetime.timedelta(seconds=i))+" ")
        f.write(str(datetime.datetime.now()))
        f.write("\n")
        f.close()




    def work(self):
        i = 0

        while self.is_printing:
            self.root_widget.ids['debugarea'].text = f'вы работаете {str(datetime.timedelta(seconds=i))}' + '\n'
            i += 1
            time.sleep(1)
        with open("practikDB.txt", "r") as f:
            text = f.read()

        f = open('practikDB.txt', 'w')
        f.write(text + "вы работали:=" +str(datetime.timedelta(seconds=i))+" ")
        f.write(str(datetime.datetime.now()))
        f.close()



    def teach(self):
        i = 0

        while self.is_printing:
            self.root_widget.ids['debugarea'].text = f'вы учитесь {str(datetime.timedelta(seconds=i))}' + '\n'
            i += 1
            time.sleep(1)
        with open("practikDB.txt", "r") as f:
            text = f.read()

        f = open('practikDB.txt', 'w')
        f.write(text + "вы учились:=" + str(datetime.timedelta(seconds=i))+" ")
        f.write(str(datetime.datetime.now()))
        f.write("\n")
        f.close()


    def sleep(self):
        i = 0

        while self.is_printing:
            self.root_widget.ids['debugarea'].text = f'вы спите {str(datetime.timedelta(seconds=i))}' + '\n'
            i += 1
            time.sleep(1)
        with open("practikDB.txt", "r") as f:
            text = f.read()

        f = open('practikDB.txt', 'w')
        f.write(text + "вы спали:=" + str(datetime.timedelta(seconds=i))+" ")
        f.write(str(datetime.datetime.now()))
        f.write("\n")
        f.close()


    def sport(self):
        i = 0

        while self.is_printing:
            self.root_widget.ids['debugarea'].text = f'вы занимаетесь спортом {str(datetime.timedelta(seconds=i))}' + '\n'
            i += 1
            time.sleep(1)
        with open("practikDB.txt", "r") as f:
            text = f.read()

        f = open('practikDB.txt', 'w')
        f.write(text + "вы занимались спортом:=" + str(datetime.timedelta(seconds=i))+" ")
        f.write(str(datetime.datetime.now()))
        f.write("\n")
        f.close()




    def his(self):
        i = 0
        while self.is_printing:
            with open("practikDB.txt", "r") as f:
                text = f.read()
            self.root_widget.ids['debugarea'].text = text


    def do_print(self,x):
        if not self.is_printing:
            self.is_printing = True
            if x == 1:
                self.print_thread = threading.Thread(target=self.relax)
            elif x==2:
                self.print_thread = threading.Thread(target=self.work)
            elif x==3:
                self.print_thread = threading.Thread(target=self.teach)
            elif x==4:
                self.print_thread = threading.Thread(target=self.sleep)
            elif x==5:
                self.print_thread = threading.Thread(target=self.sport)
            elif x==6:
                self.print_thread = threading.Thread(target=self.his)
            self.print_thread.start()

        else:
            self.is_printing = False
            self.print_thread.join()
            self.print_thread = None

MainApp().run()