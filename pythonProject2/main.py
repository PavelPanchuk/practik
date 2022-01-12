# !/usr/bin/python
# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.lang import Builder
import threading
import time
import os.path
from kivy.config import Config
from kivy.core.window import Window
import math
import datetime
from datetime import date

Window.clearcolor = (1, 1, 1, 1)
Config.set('kivy', 'window_icon', 'work-time.png')
check_file = os.path.exists('practikDB.txt')  # создани фали техт который является базой данных активностей
if (check_file == False):
    my_file = open("practikDB.txt", "w+")

check_file = os.path.exists('textvalue.txt')  # создани фали техт который является базой данных активностей
if (check_file == False):
    my_file = open("textvalue.txt", "w+")

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
            color:0, 0, 0, 1
            font_size: 40

    Label:
        pos: 0,260
        size_hint_y: .1
        text:"выбор категории"
        size_hint: None, None
        size: self.texture_size
        color:0, 0, 0, 1
        font_size: 40

    Button:
        size_hint_y: .1
        text: 'история'
        on_release:
            app.do_print(x=1)
            self.text = 'закрыть историю' if app.is_printing else 'история'
        color:0, 0, 0, 1
        font_size: 30
    Button:
        pos: 0,60
        size_hint_y: .1
        text: 'старт'
        on_release:
            app.do_print(x=0)
            self.text = 'стоп' if app.is_printing else 'старт'
        color:0, 0, 0, 1
        font_size: 30

    Spinner:
        id: spinner_id
        pos: 0,160
        size_hint_y: .1
        text:"нет категории"
        values:["Работа","Сон","Прогулка","Завтрак","Обед","Ужин","Спорт","Магазин","Работа","Учеба","Проезд","Игры","Чтение книги","Физ Подготовка","Другое"]
        on_text: app.text(spinner_id.text)
        color:0, 0, 0, 1
        font_size: 40
'''

class MainApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.is_printing = False
        self.print_thread = None
        self.root_widget = Builder.load_string(kv)

    def build(self):
        self.icon = 'work-time.png'
        self.root_widget.ids['debugarea'].text = "выберете категорию"
        return self.root_widget

    def text(self,value):
        f = open('textvalue.txt', 'w')
        f.write(value)
        print(value)
        f.close()

    def test(self):
        i = 0
        ii=0
        currentTime = time.time()
        print(currentTime)
        with open("textvalue.txt", "r") as ff:
            valuetxt = ff.read()
        while self.is_printing:
            currentTimenow = time.time()
            i=currentTimenow-currentTime
            print(i)
            ii=math.ceil(i)
            print(ii)
            self.root_widget.ids['debugarea'].text = (valuetxt+ ":="+ str(datetime.timedelta(seconds=(ii)))+ '\n')
            i += 1
            time.sleep(1)
        with open("practikDB.txt", "r") as f:
            text = f.read()
        currentTimeend = time.time()
        curtime=currentTimeend-currentTime
        print(curtime)
        f = open('practikDB.txt', 'w')
        f.write(text + valuetxt+ ":=" + str(datetime.timedelta(seconds=ii)) + " ")
        current_date = date.today()
        f.write(str(current_date))
        f.write("\n")
        f.close()

    def his(self):
        while self.is_printing:
            with open("practikDB.txt", "r") as f:
                text = f.read()
            self.root_widget.ids['debugarea'].text =text
        self.root_widget.ids['debugarea'].text = "выберете категорию"

    def do_print(self,x):
        if not self.is_printing:
            self.is_printing = True
            if x==0:
                self.print_thread = threading.Thread(target=self.test)
            if x==1:
                self.print_thread = threading.Thread(target=self.his)
            self.print_thread.start()
        else:
            self.is_printing = False
            self.print_thread.join()
            self.print_thread = None

if __name__ == '__main__':
    MainApp().run()
