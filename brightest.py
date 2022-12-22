from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import csv
import requests

brightest_star_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("C:/Users/khanf/Downloads/chromedriver_win32/chromedriver.exe")
browser.get(brightest_star_URL)
time.sleep(10)

header = ["Proper name", "Distance(ly)", "Mass", "Radius"]
star_data = []

