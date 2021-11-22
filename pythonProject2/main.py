#!/usr/bin/python
# -*- coding: utf-8 -*-
from kivy.core.window import Window

from kivy.app import App
from kivy.lang import Builder
import threading
import time
import os.path
from kivy.config import Config

Config.set('kivy','window_icon','work-time.png')

#android.minapi = 25


check_file = os.path.exists('text.txt') # создани фали техт который является базой данных активностей
if (check_file ==False):
    my_file = open("text.txt", "w+")

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
            app.do_print()
            self.text = 'остановить' if app.is_printing else 'отдых'

    Button:
        pos:0,100
        size_hint_y: .1
        size_hint_x: .3

        text: 'работа'
        on_release:
            app.do_print2()
            self.text = 'остановить' if app.is_printing else 'работа'


    Button:
        pos:300,0
        size_hint_y: .1
        size_hint_x: .3

        text: 'учеба'
        on_release:
            app.do_print3()
            self.text = 'остановить' if app.is_printing else 'учеба?'
    Button:
        pos:0,200
        size_hint_y: .1
        size_hint_x: .3

        text: 'сон'
        on_release:
            app.do_print4()
            self.text = 'остановить' if app.is_printing else 'сон'
    Button:
        pos:300,100
        size_hint_y: .1
        size_hint_x: .3

        text: 'спорт'
        on_release:
            app.do_print5()
            self.text = 'остановить' if app.is_printing else 'спорт'
    Button:
        pos:300,200
        size_hint_y: .1
        size_hint_x: .3

        text: 'история'
        on_release:
            app.history()






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

    def printer(self):
        i = 0

        while self.is_printing:
            self.root_widget.ids['debugarea'].text = f'вы отдыхаете {i}' + '\n'
            i += 1
            time.sleep(1)
        with open("text.txt", "r") as f:
            text = f.read()

        f = open('text.txt', 'w')
        f.write(text + "вы отдыхали:cek=" + str(i))
        f.write("\n")
        f.close()

    def do_print(self):
        if not self.is_printing:
            self.is_printing = True
            self.print_thread = threading.Thread(target=self.printer)
            self.print_thread.start()

        else:
            self.is_printing = False
            self.print_thread.join()
            self.print_thread = None

    def do_print2(self):
        if not self.is_printing:
            self.is_printing = True
            self.print_thread = threading.Thread(target=self.printer2)
            self.print_thread.start()

        else:
            self.is_printing = False
            self.print_thread.join()
            self.print_thread = None

    def printer2(self):
        i = 0

        while self.is_printing:
            self.root_widget.ids['debugarea'].text = f'вы работаете {i}' + '\n'
            i += 1
            time.sleep(1)
        with open("text.txt", "r") as f:
            text = f.read()

        f = open('text.txt', 'w')
        f.write(text + "вы работали:cek=" + str(i))
        f.write("\n")
        f.close()

    def do_print3(self):
        if not self.is_printing:
            self.is_printing = True
            self.print_thread = threading.Thread(target=self.printer3)
            self.print_thread.start()

        else:
            self.is_printing = False
            self.print_thread.join()
            self.print_thread = None

    def printer3(self):
        i = 0

        while self.is_printing:
            self.root_widget.ids['debugarea'].text = f'вы учитесь {i}' + '\n'
            i += 1
            time.sleep(1)
        with open("text.txt", "r") as f:
            text = f.read()

        f = open('text.txt', 'w')
        f.write(text + "вы учились:cek=" + str(i))
        f.write("\n")
        f.close()

    def do_print4(self):
        if not self.is_printing:
            self.is_printing = True
            self.print_thread = threading.Thread(target=self.printer4)
            self.print_thread.start()

        else:
            self.is_printing = False
            self.print_thread.join()
            self.print_thread = None

    def printer4(self):
        i = 0

        while self.is_printing:
            self.root_widget.ids['debugarea'].text = f'вы спите {i}' + '\n'
            i += 1
            time.sleep(1)
        with open("text.txt", "r") as f:
            text = f.read()

        f = open('text.txt', 'w')
        f.write(text + "вы спали:cek=" + str(i))
        f.write("\n")
        f.close()

    def do_print5(self):
        if not self.is_printing:
            self.is_printing = True
            self.print_thread = threading.Thread(target=self.printer5)
            self.print_thread.start()

        else:
            self.is_printing = False
            self.print_thread.join()
            self.print_thread = None

    def printer5(self):
        i = 0

        while self.is_printing:
            self.root_widget.ids['debugarea'].text = f'вы занимаетесь спортом {i}' + '\n'
            i += 1
            time.sleep(1)
        with open("text.txt", "r") as f:
            text = f.read()

        f = open('text.txt', 'w')
        f.write(text + "вы занимались спортом:cek=" + str(i))
        f.write("\n")
        f.close()

    def history(self):
        if not self.is_printing:
            self.is_printing = True
            self.print_thread = threading.Thread(target=self.his)
            self.print_thread.start()

        else:
            self.is_printing = False
            self.print_thread.join()
            self.print_thread = None

    def his(self):
        i = 0

        while self.is_printing:
            with open("text.txt", "r") as f:
                text = f.read()
            self.root_widget.ids['debugarea'].text = text
            i += 1
            time.sleep(1)


MainApp().run()