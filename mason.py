import requests
from bs4 import BeautifulSoup
import selenium
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc

#driver = webdriver.Chrome()  # Optional argument, if not specified will search path.

url = "https://sso.teachable.com/secure/877279/identity/login/password"

url1 = "https://mason-gre.teachable.com/courses/enrolled/1632884"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cache-Control": "max-age=0",
    "Cookie": "ahoy_visitor=06677690-661b-4d57-b027-0d16f03081f7; _afid=06677690-661b-4d57-b027-0d16f03081f7; aid=06677690-661b-4d57-b027-0d16f03081f7; _session_id=dcae0124082cd8191ea510d822a9e8f8; ajs_group_id=null; ajs_anonymous_id=%2293b34826-d31e-4111-8b03-7558b4ed294a%22; __ssid=aaa5e5a8c66781b0f8bfb9cb70375b3; ajs_user_id=%2295496460%22; __stripe_mid=8268a9ae-71f3-47d3-8cdb-e5c96dffac49cba98f; _fbp=fb.1.1690817982999.1641593796; _ga_RVBJ5CRSEF=GS1.1.1690817803.5.1.1690819368.24.0.0; _ga=GA1.2.1744537636.1690730247; _ga_G66Z5GE2F3=GS1.2.1690910444.4.0.1690910444.60.0.0; ahoy_visit=e0d8f66e-a1b8-42e5-9aff-a903c5f00a7d; ahoy_track=true; __cfruid=02e699f674f274adef6050e339167dcf231789dd-1697785963; _cfuvid=1oNdwBqVaZoLK4PVTWpGz3jCeyZgdy.lEUufTVKgo4Q-1697785963645-0-604800000; _gid=GA1.2.1438857744.1697785954; cf_clearance=ZoDZTGjSZs8hPJEp3zetS2rUh0.s3AN5ZXl9gzABHX4-1697785968-0-1-90bff035.4d2db4d8.fed90597-160.2.1697785964; sk_l737hxy2_access=eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJ1c2VyIiwiaWF0IjoxNjk3Nzg3OTk3LCJqdGkiOiJmOWJlYWI5MC1jOTNjLTQ1YTgtODBkNS1iOTM5MTI2OTcyZjEiLCJpc3MiOiJza19sNzM3aHh5MiIsInN1YiI6IjhmN2Q1ZmJlLWM1YzYtNDE3Zi1hOTcxLTJmNzE1MmRmZDk1YiJ9.MHzqGxwbbT-WNavVQFTixL6JHUnLsbRPTvJrt1kM2KI; sk_l737hxy2_remember_me=1; signed_in=true; site_preview=logged_in; _hp2_props.318805607=%7B%22template_name%22%3A%22%22%7D; __cf_bm=fxd9Z9g2ZNyO_eAVTEKCMMgFFGBk_4iscgWKSH1wXIo-1697790238-0-AUWLo9Pb+n0gp1WDtcCbdsoMKNzI2nRl6KXzKNN78CTACEaRUrHhKOtMScQ4Yhk+JR2rUd5iAgOZHOvdhfusJnA=; _hp2_ses_props.318805607=%7B%22r%22%3A%22https%3A%2F%2Fmason-gre.teachable.com%2Fcourses%2F1632884%2Flectures%2F49502001%22%2C%22ts%22%3A1697790228109%2C%22d%22%3A%22mason-gre.teachable.com%22%2C%22h%22%3A%22%2Fcourses%2Fenrolled%2F1632884%22%7D; __stripe_sid=21b77715-5b63-4a3a-bbd5-dd42008fc75ed28865; _hp2_id.318805607=%7B%22userId%22%3A%224829214670075662%22%2C%22pageviewId%22%3A%226697989797226107%22%2C%22sessionId%22%3A%227818999040135243%22%2C%22identity%22%3A%2295496460%22%2C%22trackerVersion%22%3A%224.0%22%2C%22identityField%22%3Anull%2C%22isIdentified%22%3A1%7D",
    "Referer": "https://mason-gre.teachable.com/courses/1632884/lectures/49502001",
    "Sec-Ch-Ua": '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
}

driver = uc.Chrome()
driver.get(url)

#driver.get(url)
time.sleep(10)
html = driver.page_source
print(html)

#print(driver.page_source)

#time.sleep(5) # Let the user actually see something!

#check_button = driver.find_element(By.CLASS_NAME, "ctp-checkbox-label")#.click()
#print(check_button)

#check_button = driver.find_element()

"""
search_box = driver.find_element_by_name('q')

search_box.send_keys('ChromeDriver')

search_box.submit()

time.sleep(5) # Let the user actually see something!

driver.quit()"""