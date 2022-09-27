import json
from linebot import LineBotApi
from linebot.models import TextSendMessage

file = open('info.json','r')
info = json.load(file)

CHANNEL_ACCESS_TOKEN = info['CHANNEL_ACCESS_TOKEN']
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
USER_ID = info['USER_ID']


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time  
    
if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')
    driver = webdriver.Chrome(options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    driver.get('https://secure.louisvuitton.com/jpn-jp/mylv/overview')
    driver.maximize_window()
    time.sleep(5)
    email = "cymilkga12@gmail.com"
    password = "Mis01aki10ra**"
    #メアド、パス入力、ログインボタン押下
    driver.find_element(By.CSS_SELECTOR,'#loginloginForm').send_keys(email)
    driver.find_element(By.CSS_SELECTOR,'#passwordloginForm').send_keys(password)
    driver.find_element(By.CSS_SELECTOR,'#loginSubmit_').click()
    #ほしい商品の入荷状況を確認
    url = "https://jp.louisvuitton.com/jpn-jp/products/pochette-voyage-epi-nvprod3660137v/M81326"
    driver.get(url)
    #指定した要素がクリックできる状態になるまで待機
    time.sleep(5)
    #不要なボップアップが出現することがあるのでそれを閉じる

    try:
        driver.find_elementdriver.find_element(By.CSS_SELECTOR,'.lv-modal__contents > button').click()
    except Exception:
        print('ボップアップは出現しませんでした')

    driver.find_element(By.CSS_SELECTOR,'.lv-product-purchase > button').click()

    time.sleep(3)
    try:
        driver.find_element(By.CSS_SELECTOR,'.line-app-container > img').click()
        print('入荷されていません')
    except Exception:
        messages= TextSendMessage(text='商品が入荷しました。\n https://jp.louisvuitton.com/jpn-jp/products/carryall-pm-monogram-nvprod3770016v/M46203')
        line_bot_api.push_message(USER_ID, messages=messages)   
