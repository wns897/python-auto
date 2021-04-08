import pyautogui
#print(pyautogui.position())
#pyautogui.moveTo(190, 159)
#pyautogui.click(190, 159)
num7= pyautogui.locateCenterOnScreen('7.png')
#pyautogui.click(num7)
#pyautogui.screenshot('filename', location)
#print(pyautogui.position())

pyautogui.screenshot('1.png', region=(1553, 794, 30, 30))

num1= pyautogui.locateCenterOnScreen('1.png')
pyautogui.click(num1)
pyautogui.click(num7)
pyautogui.click(num1)
pyautogui.click(num7)
pyautogui.click(num1)
pyautogui.click(num7)
