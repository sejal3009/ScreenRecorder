import cv2
import numpy as np
import pyautogui
import time
import win32gui
import win32con

from os import mkdir
try:
    mkdir("recordings")
except FileExistsError:
    pass


def minimizeWindow():
    window = win32gui.FindWindow(None,"screen recorder")
    win32gui.ShowWindow(window,win32con.SW_MINIMIZE)
# display screen resolution
SCREEN_SIZE = (1920,1080)
# define codec
fourcc = cv2.VideoWriter_fourcc(*"XVID")
# create the video write object
output = cv2.VideoWriter("recordings/"+"ScreenRecording "+time.strftime("%H-%M-%S %d-%m-%y")+".mp4",fourcc, 20.0,(SCREEN_SIZE))
print("Recording started....\nWindow minimized in taskbar.\nPress q to exit")
minimized = False
while True:
    #make screenshot
    img = pyautogui.screenshot()
    #Convert these pixels to a proper numpy array to work
    frame = np.array(img)
    #convert colors from BRG to RGB
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    #show the frame
    cv2.imshow("Screen recorder", frame)
    if minimized == True:
        pass
    else:
        minimized = True
        minimizeWindow()
    #write the frame
    output.write(frame)
    #if user click q it exits
    if cv2.waitKey(1) == ord("q"):
        print("\rRecording Finished.")
        break

#make sure everything is closed when exited
output.release()
cv2.destroyAllWindows()