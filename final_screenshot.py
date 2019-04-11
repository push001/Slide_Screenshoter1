import pyautogui
import time
import sys

print("Please go and open that particular  slide address in your browser.")

print("\nI hope your slides are ready !\n")
address = input('Enter_path_of_folder:')
total_slides = int(input("Total slides : "))

print("Now go to your browser and make the screen Fullscreen")
print("Your program will start within 5 seconds.")

time.sleep(6)
i = 1

try:
     xCord, yCord = pyautogui.locateCenterOnScreen("left_arrow.png")
except:
     print("\n\nProper left arrow not found !")
     sys.exit()
     
time.sleep(2)

try:
    while(i <= total_slides):
         pyautogui.screenshot("{}\image{}.png".format(address,i))
         i  +=1
         pyautogui.click(x=xCord, y=yCord)
         time.sleep(2)
finally:
     print('\nDone')
     

go = input('\nHit Enter key to exit! ')

#Test_Link = https://docs.google.com/presentation/d/12IEPCRFURNwAh1q2--HawunNRY2ushxCGKrNK4qA1i4/preview?usp=embed_googleplus
