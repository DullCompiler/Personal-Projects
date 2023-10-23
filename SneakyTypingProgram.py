import time
import pyautogui

phrase = input("Enter the text to be typed: ")   # replace with your desired phrase
#delay = 0.001   # adjust as needed for typing speed

# move the mouse to the center of the screen to avoid interference
pyautogui.moveTo(pyautogui.size().width / 2, pyautogui.size().height / 2)

# click to focus on the active window
pyautogui.click()

# loop through each character in the phrase and type it
for char in phrase:
    pyautogui.typewrite(char)
#    time.sleep(delay)

# press the enter key to submit the text
pyautogui.press('enter')
