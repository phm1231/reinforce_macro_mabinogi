import pyautogui as m
import time
import keyboard

try:
    while True:
        if(keyboard.is_pressed('F3')):
            break
        x, y = m.position()
        print('x : {}, y : {}'.format(x, y), end='\r')

except:
    print('quit')
