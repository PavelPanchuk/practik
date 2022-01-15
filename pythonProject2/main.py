# !/usr/bin/python
# -*- coding: utf-8 -*-
import json
from kivy.app import App
from kivy.lang import Builder
import threading
import time
import os.path
from kivy.config import Config
import math
from kivy.core.window import Window
from datetime import date
Window.clearcolor = (1, 1, 1, 1)
Config.set('kivy', 'window_icon', 'work-time.png')
check_file = os.path.exists('practikDB.txt')  # создани фали техт который является базой данных активностей
if (check_file == False):
    my_file = open("practikDB.txt", "w+")

check_file = os.path.exists('textvalue.txt')  # создани фали техт который является базой данных активностей
if (check_file == False):
    my_file = open("textvalue.txt", "w+")

check_file = os.path.exists('my_data.json')  # создани фали техт который является базой данных активностей
if (check_file == False):
    my_file = open("my_data.json", "w+")
    j = {"Работа":0,"Сон":0,"Прогулка":0,"Завтрак":0,"Обед":0,"Ужин":0,"Спорт":0,"Магазин":0,"Развлечения":0,"Учеба":0,"Проезд":0,"Игры":0,"Чтение":0,"Физра":0,"Другое":0}
    d = json.dumps(j)
    with open('my_data.json', 'w+') as f:
        f.write(d)

check_file = os.path.exists('output.txt')  # создани фали техт который является базой данных активностей
if (check_file == False):
    my_file = open("output.txt", "w+")

kv = '''
FloatLayout:
    ScrollView:
        pos_hint: {'left': 1, 'top': 1}
        size_hint_y: .5
        do_scroll_x: 1

        Label:
            id: debugarea
            size_hint: None, None
            size: self.texture_size
            color:0, 0, 0, 1
            font_size: 40

    Label:
        pos: 0,480
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
        pos: 0,230
        size_hint_y: .1
        text: 'старт'
        on_release:
            app.do_print(x=0)
            self.text = 'стоп' if app.is_printing else 'старт'
        color:0, 0, 0, 1
        font_size: 30

    Button:
        pos: 0,120
        size_hint_y: .1
        text: 'итог'
        on_release:
            app.do_print(x=2)
            self.text = 'закрыть итог' if app.is_printing else 'итог'
        color:0, 0, 0, 1
        font_size: 30

    Spinner:
        id: spinner_id
        pos: 0,360
        size_hint_y: .1
        text:"нет категории"
        values:["Работа","Сон","Прогулка","Завтрак","Обед","Ужин","Спорт","Магазин","Развлечения","Учеба","Проезд","Игры","Чтение","Физра","Другое"]
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

    def text(self, value):
        f = open('textvalue.txt', 'w')
        f.write(value)
        f.close()

    def test(self):
        i = 0
        ii = 0
        t=0
        currentTime = time.time()
        with open("textvalue.txt", "r") as ff:
            valuetxt = ff.read()
        while self.is_printing:
            currentTimenow = time.time()
            i = currentTimenow - currentTime
            ii = math.ceil(i)
            t=ii
            self.root_widget.ids['debugarea'].text = (valuetxt + ":" + str(ms(t)) + '\n')
            i += 1
            time.sleep(1)
        with open("practikDB.txt", "r") as f:
            text = f.read()
        f = open('practikDB.txt', 'w')
        f.write(text + valuetxt + ":=" + str(ms(t))  + " ")
        current_date = date.today()
        f.write(str(current_date))
        f.write("\n")
        f.close()

        with open('my_data.json', encoding='raw_unicode_escape') as f:
            new_d = json.loads(f.read().encode('raw_unicode_escape').decode())
        if ("Спорт" == valuetxt):
            key=new_d['Спорт']
            new_d.update(Спорт=(ii + key))
        if ("Работа" == valuetxt):
            key=new_d['Работа']
            new_d.update(Работа=(ii + key))
        if ("Сон" == valuetxt):
            key=new_d['Сон']
            new_d.update(Сон=(ii + key))
        if ("Прогулка" == valuetxt):
            key=new_d['Прогулка']
            new_d.update(Прогулка=(ii + key))
        if ("Завтрак" == valuetxt):
            key=new_d['Завтрак']
            new_d.update(Завтрак=(ii + key))
        if ("Обед" == valuetxt):
            key=new_d['Обед']
            new_d.update(Обед=(ii + key))
        if ("Ужин" == valuetxt):
            key=new_d['Ужин']
            new_d.update(Ужин=(ii + key))
        if ("Развлечения" == valuetxt):
            key=new_d['Развлечения']
            new_d.update(Развлечения=(ii + key))
        if ("Магазин" == valuetxt):
            key=new_d['Магазин']
            new_d.update(Магазин=(ii + key))
        if ("Учеба" == valuetxt):
            key=new_d['Учеба']
            new_d.update(Учеба=(ii + key))
        if ("Проезд" == valuetxt):
            key=new_d['Проезд']
            new_d.update(Проезд=(ii + key))
        if ("Игры" == valuetxt):
            key=new_d['Игры']
            new_d.update(Игры=(ii + key))
        if ("Чтение" == valuetxt):
            key=new_d['Чтение']
            new_d.update(Чтение=(ii + key))
        if ("Физра" == valuetxt):
            key=new_d['Физра']
            new_d.update(Физра=(ii + key))
        if ("Другое" == valuetxt):
            key=new_d['Другое']
            new_d.update(Другое=(ii + key))
        j = json.dumps(new_d)
        with open('my_data.json', 'w') as f:
            f.write(j)

    def his(self):
        while self.is_printing:
            with open("practikDB.txt", "r") as f:
                text = f.read()
            self.root_widget.ids['debugarea'].text = text
        self.root_widget.ids['debugarea'].text = "выберете категорию"

    def total(self):
        with open('my_data.json', encoding='raw_unicode_escape') as f:
            txt = json.loads(f.read().encode('raw_unicode_escape').decode())
        for key in txt:
            with open("output.txt", "r") as ff:
                text = ff.read()
            f = open('output.txt', 'w')
            f.write(text+key + " " + ms(txt[key]))
            f.write("\n")
            f.close()


        while self.is_printing:
            with open("output.txt", "r") as ff:
                text = ff.read()
            self.root_widget.ids['debugarea'].text = text
        self.root_widget.ids['debugarea'].text = "выберете категорию"
        f = open('output.txt', 'w')
        f.write("")
        f.close()

    def do_print(self, x):
        if not self.is_printing:
            self.is_printing = True
            if x == 0:
                self.print_thread = threading.Thread(target=self.test)
            if x == 1:
                self.print_thread = threading.Thread(target=self.his)
            if x == 2:
                self.print_thread = threading.Thread(target=self.total)
            self.print_thread.start()
        else:
            self.is_printing = False
            self.print_thread.join()
            self.print_thread = None

def ms(t):
    H = t // 3600
    M = int(t / 60)
    S = int(10 * int(t - M * 60)) / 10
    strn =str(H)+"ч."+ str(M) + "м. " + str(S) + "с."
    return strn

if __name__ == '__main__':
    MainApp().run()
