from PIL import ImageGrab, ImageOps
import time
import pyautogui
from numpy import *

class Wspolrzedne():
    replaybtn = (480,400)
    dino = (262,424)
    #box =((264,406),(315,441))

def restart():
    pyautogui.click(Wspolrzedne.replaybtn)
    pyautogui.keyDown("down")

def spacja():
    pyautogui.keyUp("down")
    pyautogui.keyDown("space")
    time.sleep(0.19)
    print("Jump")
    pyautogui.keyUp("space")
    pyautogui.keyDown("down")

def imagegrab():
    box = (Wspolrzedne.dino[0]+90,Wspolrzedne.dino[1],Wspolrzedne.dino[0]+140,Wspolrzedne.dino[1]+5)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    print(a.sum())
    return a.sum()

def main():
    restart()
    while True:
        if imagegrab()!=497:
            spacja()
            time.sleep(0.1)

main()
time.sleep(1)
spacja()