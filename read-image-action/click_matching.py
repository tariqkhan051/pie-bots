import pyautogui
import time
import os
from os import listdir

images_to_click = "images/click"
images_to_esc = "images/esc"
images_to_double_esc = "images/dblesc"
all_images = {}

def read_images(images_path, read_images, action):
    for images in os.listdir(images_path):
        if (images.endswith(".png")):
            #print(images)
            read_images[images] = action

read_images(images_to_click, all_images, "click")
read_images(images_to_esc, all_images, "esc")
read_images(images_to_double_esc, all_images, "dblesc")

while True:
    for image in all_images:
        action = all_images[image]
        imageLocation = pyautogui.locateOnScreen("images/"+action+"/"+image)
        if imageLocation is not None:
            if (action == "click"):
                pyautogui.click(imageLocation)
            elif (action == "dblesc"):
                pyautogui.press('esc')
                pyautogui.press('esc')
            elif (action == "esc"):
                pyautogui.press('esc')
                pyautogui.press('esc')
            else:
                continue
            #set delay to avoid bot detection
            time.sleep(1)
            continue
        else:
            continue