import pyautogui as pg
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from time import sleep

url_entry="https://youtube.com/"

s = Service("chromedriver.exe")
browser = Chrome(service=s)
browser.get(url_entry)
pg.moveTo(427,205, 1)
pg.click(button="left")
pg.write("Hello, World!", 0.5)
pg.press("Enter")
pg.moveTo(348, 444, 1)
pg.click(button="left")
sleep(5)