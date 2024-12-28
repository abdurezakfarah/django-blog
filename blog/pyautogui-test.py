import time

import pyautogui as p

time.sleep(5)

for i in range(501):
    p.typewrite(f"{ i } - message badan dhakhso usoo dir kkk")
    p.press("enter")
