
import pyautogui
for i in range(5):
      pyautogui.moveTo(100, 100, duration=0.25)
      pyautogui.moveTo(200, 100, duration=1)
      pyautogui.moveTo(900, 200, duration=0.25)
      pyautogui.moveTo(100, 800, duration=0.25)
      


""" The pyautogui.moveTo() function will instantly move the mouse cursor to a specified position on the screen   X and y are the coordinates  and time is optional parameter """
