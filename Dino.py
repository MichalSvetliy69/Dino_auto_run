import numpy as np
import pyautogui
import win32com.client as comclt
import cv2
import imutils
from PIL import Image
obj = (1,1,1)

while (obj) != (55, 55, 55):
    image = pyautogui.screenshot(region=(760,225, 6, 1))
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite("iii.png", image)
    img = Image.open("iii.png")
     
    if (img.getpixel((0,0)) == (172, 172, 172)) or \
       (img.getpixel((1,0)) == (172, 172, 172)) or \
       (img.getpixel((2,0)) == (172, 172, 172)) or \
       (img.getpixel((3,0)) == (172, 172, 172)) or \
       (img.getpixel((4,0)) == (172, 172, 172)) or \
       (img.getpixel((5,0)) == (172, 172, 172)):
        wsh = comclt.Dispatch('WScript.Shell')
        wsh.AppActivate("Google Chrome")
        wsh.SendKeys("{Up}")  