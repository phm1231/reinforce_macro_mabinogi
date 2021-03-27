import pyautogui as m
import random
import time
import keyboard
import pytesseract
import os
import cv2
import numpy as np

item = 'eiren2'


reinforce_button={
    'top_left' : {'x' : 1220, 'y' : 840},
    'bottom_right' : {'x' : 1340, 'y' : 880}
}

def getTextBasic(img): # large / 3,3 / close / bw
    large = cv2.pyrUp(img)
    gray = cv2.cvtColor(large, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((3, 3), np.uint8)
    grad = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
    _, bw = cv2.threshold(grad, 0.0, 255.0, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    text = pytesseract.image_to_string(bw, lang='kor')
    return text

def getTextException3(img): # large / 5,5 / open / grad
    large = cv2.pyrUp(img)
    gray = cv2.cvtColor(large, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((5, 5), np.uint8)
    grad = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
    text = pytesseract.image_to_string(grad, lang='kor')
    return text

def getTextException2(img): # large / 3,3 / open / bw
    large = cv2.pyrUp(img)
    gray = cv2.cvtColor(large, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((3, 3), np.uint8)
    grad = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
    _, bw = cv2.threshold(grad, 0.0, 255.0, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    text = pytesseract.image_to_string(bw, lang='kor')
    return text

def getTextException1(img): # large / 5,5 / close / grad
    large = cv2.pyrUp(img)
    gray = cv2.cvtColor(large, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((5, 5), np.uint8)
    grad = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
    text = pytesseract.image_to_string(grad, lang='kor')
    return text

def getTextException4(img): # 2,2 / close
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((2, 2), np.uint8)
    grad = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
    _, bw = cv2.threshold(grad, 0.0, 255.0, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    text = pytesseract.image_to_string(bw, lang='kor')
    return text

def getText(img):
    argv = np.array(img)
    text = getTextBasic(argv)
    if(text.find('레벨') == -1 or text.count('\n') != 1):
        text = getTextException1(argv)
        if(text.find('레벨') == -1 or text.count('\n') != 1):
            text = getTextException2(argv)
        if(text.find('레벨') == -1 or text.count('\n') != 1):
            text = getTextException3(argv)

    elif(len(text) == 5 and text.find('체력') == -1 and text.find('지력') == -1 and text.find('솜씨') == -1 and text.find('의지') == -1 and text.find('행운') == -1 and text.find('방어') == -1 and text.find('보호') == -1):
        text = getTextException4(argv)
    return text
s

def getLocation(bt):
    x = random.uniform(bt['top_left']['x'], bt['bottom_right']['x'])
    y = random.uniform(bt['top_left']['y'], bt['bottom_right']['y'])
    return x, y

def main():
    res = open('/data/%s.txt' % item, 'at', encoding='UTF8')
    cnt = 4909
    try:
        while (cnt!=5001):
            if(keyboard.is_pressed('F3')):
                break
            if(keyboard.is_pressed('F4')):
                input("입력 대기 : ")

            x, y = getLocation(reinforce_button)    
            m.moveTo(x, y)
            m.click()
            m.mouseDown()
            m.mouseUp()
            time.sleep(5)
            img1 = m.screenshot('/data/eiren2/%d_1.png' % cnt, region=(920, 1060, 1520-820, 44))
            img2 = m.screenshot('/data/eiren2/%d_2.png' % cnt, region=(920, 1100, 1520-820, 44))
            img3 = m.screenshot('/data/eiren2/%d_3.png' % cnt, region=(920, 1140, 1520-820, 44))
            img4 = m.screenshot('/data/eiren2/%d_4.png' % cnt, region=(920, 1180, 1520-820, 44))
            img5 = m.screenshot('/data/eiren2/%d_5.png' % cnt, region=(920, 1220, 1520-820, 46))
            img6 = m.screenshot('/data/eiren2/%d_6.png' % cnt, region=(920, 1260, 1520-820, 44))

            text = getText(img1)
            if(text.find('레벨') != -1 and text.count('\n') == 1) :
                print(text, file=res)
            text = getText(img2)
            if(text.find('레벨') != -1 and text.count('\n') == 1) :
                print(text, file=res)
            text = getText(img3)
            if(text.find('레벨') != -1 and text.count('\n') == 1) :
                print(text, file=res)
            text = getText(img4)
            if(text.find('레벨') != -1 and text.count('\n') == 1) :
                print(text, file=res)
            text = getText(img5)
            if(text.find('레벨') != -1 and text.count('\n') == 1) :
                print(text, file=res)
            text = getText(img6)
            if(text.find('레벨') != -1 and text.count('\n') == 1) :
                print(text, file=res)

            cnt += 1
            print(cnt)
    except Exception as ex:
        print(ex)

    res.close()
    #time.sleep(10)
    #os.system("shutdown -s -t 30")

if __name__ == '__main__' :
    main()