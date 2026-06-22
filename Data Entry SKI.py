import pyautogui
import pandas as pd
import time
import os

pyautogui.FAILSAFE = True

username = os.getlogin()
path = fr"C:\Users\{username}\OneDrive\Desktop\Sample.xlsx"

df = pd.read_excel(path, header=None)
df.columns = ["FirstName", "LastName", "DOB", "GroupName"]

# 👇 REPLACE THESE WITH YOUR REAL COORDINATES
PLUS_BTN   = (191, 62)
FIRST_NAME = (819, 428)
LAST_NAME  = (1092, 425)
DOB = (804,454)
GROUP_NAME = (796, 620)
Privacy_Policy = (1189, 369)
Drop_Down = (1248, 425)
Click_yes = (1135, 526)
Click_OK = (1068, 798)
print("Starting in 5 seconds. DO NOT touch mouse/keyboard.")
time.sleep(5)

for i, row in df.iterrows():
    # Click +
    pyautogui.click(PLUS_BTN)
    time.sleep(3)

    # First Name (SPECIAL HANDLING)
    pyautogui.click(FIRST_NAME)
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    pyautogui.write(str(row["FirstName"]))

    # Last Name
    pyautogui.click(LAST_NAME)
    pyautogui.write(str(row["LastName"]))

    #DOB
    pyautogui.click(DOB)
    pyautogui.write(str(row["DOB"]))

    # Group / Street
    pyautogui.click(GROUP_NAME)
    pyautogui.write(str(row["GroupName"]))


    # Dropdown
    pyautogui.click(Privacy_Policy)
    time.sleep(1)
    pyautogui.click(Drop_Down)
    time.sleep(.5)
    pyautogui.click(Click_yes)
    pyautogui.click(Click_OK)

    time.sleep(3)

print("ALL ROWS COMPLETED")
