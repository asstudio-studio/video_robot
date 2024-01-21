#abao's video download
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import undetected_chromedriver as uc
import time

url = "http://www.ibrain.com.tw/Service/Member/Login.aspx?sLL=/Service/OrderForm/OrderFormList.aspx?"

account = input("請輸入帳號：")

password = input("請輸入密碼：")
#print(account + password)

driver = uc.Chrome()
driver.get(url)
#time.sleep()

