
import pyautogui, time
time.sleep(5)
pyautogui.click()    # click to put drawing program in focus

distance = 200
while distance > 0:
            pyautogui.dragRel(distance, 0, duration=0.2)   # move right
            distance = distance - 5
            pyautogui.dragRel(0, distance, duration=0.2)   # move down
            pyautogui.dragRon(0.2)  # move left
            distance = distance - 5
            pyautogui.dragRel(0,duration=0.2)  # move up"""
            
            
"""  pyautogui.dragRel() functions to drag th -distance, de mouel(-distance, 0, duratise cursor to a new location or a location relative to its current one. """
