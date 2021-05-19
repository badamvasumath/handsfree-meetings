import webbrowser
from pynput.keyboard import Key,Controller
import datetime
import time

#schedule for meetings
timetable={
    1:['AI','LP','ADB'],
    2:['LP','AI','IOT'],
    3:['DMDW','AI','LP'],
    4:['DMDW','IOT','SC'],
    5:['SS','DMDW','IOT'],
    6:['SC','SS','ADB']
}

#paste the URL's from the new tab after opening email after clicking "click here to join"

#meeting links 
zoomlinks={
    'ADB' : '<zoomlink>',
    'LP'  : '<zoomlink>',
    'IOT' : '<zoomlink>',
    'DMDW': '<zoomlink>',
    'SC'  : '<zoomlink>',
    'SS'  : '<zoomlink>',
    'AI'  : '<zoomlink>',
}

def open_class(url):
    webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))
    webbrowser.get('chrome').open_new(url)
    time.sleep(5)
    keyboard=Controller()               

    for _ in range(5):
        time.sleep(1)
        keyboard.press(Key.tab)
    keyboard.press(Key.enter)

x = datetime.datetime.now()

day=int(x.strftime("%w"))
hour=int(x.strftime("%I"))-1

open_class(zoomlinks[timetable[day][hour]])
