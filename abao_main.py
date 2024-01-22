#abao's video download
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import undetected_chromedriver as uc
import time
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.remote.webdriver import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

url = "http://www.ibrain.com.tw/Service/Member/Login.aspx?sLL=/Service/OrderForm/OrderFormList.aspx?"

username = input("請輸入帳號：")
password = input("請輸入密碼：")

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_experimental_option("detach", True)
driver = uc.Chrome(options=chrome_options)
#driver = webdriver.Chrome(options=chrome_options)
driver.get(url)
#time.sleep()

# 定位帳號輸入框並輸入帳號
username_input = driver.find_element(By.ID, "sAccount")  # 使用元素的 name 屬性進行定位
username_input.send_keys(username)

# 定位密碼輸入框並輸入密碼
password_input = driver.find_element(By.ID, "sPassword")  # 使用元素的 name 屬性進行定位
password_input.send_keys(password)

try:
    WebDriverWait(driver, timeout=False).until(
        EC.presence_of_element_located((By.CLASS_NAME, "btn login_out"))
    )
    print("元素已經出現！")
except TimeoutException:
    print("timeout")


"""
測試requests
response = requests.get(url)

if response.status_code == 200:
    # 使用 BeautifulSoup 解析 HTML 內容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 查找擁有特定id屬性的元素
    account_with_id = soup.find(id='sAccount')
    password_with_id = soup.find(id='sPassword')

    if account_with_id:
        # 獲取id屬性的值
        id_value = account_with_id.get('id')
        print(f'找到id為 "{id_value}" 的元素。')
    else:
        print('未找到指定id的元素。')
    
    if password_with_id:
        # 獲取id屬性的值
        id_value = password_with_id.get('id')
        print(f'找到id為 "{id_value}" 的元素。')
    else:
        print('未找到指定id的元素。')

else:
    print('無法獲取網頁內容，狀態碼:', response.status_code)

"""