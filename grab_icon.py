'''
Grab the screenshot and then manually crop the image to icon. Since main program is not able to detect the icon in those screenshots which were taken with "prt sc" or "snipping tool 
'''

import pyautogui
import time

time.sleep(5)
pyautogui.screenshot("right_arrowTest.png")
