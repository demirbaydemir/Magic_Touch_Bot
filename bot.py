from pyautogui import *
from pynput.mouse import Button , Controller
import pyautogui
import time
import keyboard
import random 
import win32api, win32con 

time.sleep(1)

mouse = Controller()

detected_baloon = " "

def draw_z():
    pyautogui.moveTo(874, 600, duration = 0.05)
    pyautogui.dragRel(100, 0, duration = 0.05)
    pyautogui.dragRel(-100, 100, duration = 0.05)
    pyautogui.dragRel(100, 0, duration = 0.05)

def draw_horizontal():
    pyautogui.moveTo(874, 600, duration = 0.1)
    pyautogui.dragRel(150, 0, duration = 0.15)

def draw_vertical():
    pyautogui.moveTo(874, 600, duration = 0.01)
    pyautogui.dragRel(0, 150, duration = 0.15)    

def draw_up():
    pyautogui.moveTo(874, 600, duration = 0.001)
    pyautogui.mouseDown(874, 600, LEFT)
    pyautogui.moveRel(100, -100, duration = 0.1)
    pyautogui.moveRel(100, 100, duration = 0.11)
    pyautogui.mouseUp(1074, 600, LEFT)
   

    #pyautogui.moveTo(874, 600, duration = 0.07)
    #pyautogui.dragRel(100, -100, duration = 0.12)
    #pyautogui.dragRel(100, 100, duration = 0.12)

def draw_down():
    pyautogui.moveTo(874, 600, duration = 0.001)
    pyautogui.mouseDown(874, 600, LEFT)
    pyautogui.moveRel(100, 100, duration = 0.1)
    pyautogui.moveRel(100, -100, duration = 0.1)
    pyautogui.mouseUp(1074, 600, LEFT)
#pyautogui.moveTo(717, 803, duration = 0.2)




while keyboard.is_pressed('p') == False:

    if pyautogui.locateOnScreen('mt_up_baloon.png', confidence=0.8) != None:
        detected_baloon = "up"
    elif pyautogui.locateOnScreen('mt_down_baloon.png', confidence=0.8) != None:
        detected_baloon = "down"
    elif pyautogui.locateOnScreen('mt_horizontal_baloon.png', confidence=0.8) != None:
        detected_baloon = "horizontal"
    elif pyautogui.locateOnScreen('mt_vertical_baloon.png', confidence=0.8) != None:
        detected_baloon = "vertical"




 #########################################

    if detected_baloon == "horizontal":
        draw_horizontal()
        detected_baloon = " "
    elif detected_baloon == "vertical":
        draw_vertical()
        detected_baloon = " "
    elif detected_baloon == "up":
        draw_up()
        detected_baloon = " "
    elif detected_baloon == "down":
        draw_down()
        detected_baloon = " "
 




    


