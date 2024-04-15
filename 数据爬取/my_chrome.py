# 导入Selenium库
import datetime
import http.client
import json
import os
import random
import re
import time

import pymysql
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from dianping.db.local_db import Store
from my_log import SingletonLogger

download_path = 'D:\\网易下载'
logger = SingletonLogger().get_logger()


# 实现登录获取cookies和上传等功能
class MyChrome:
    def __init__(self, isheadless=False, profile='Profile 1', disable_img=False, mobile_emulation=False):
        self.send_list = []
        chrome_options = Options()
        self.is_pacong_ing = False
        if isheadless == True:
            chrome_options.add_argument("--headless")
        service = Service(r"./chromedriver.exe")

        if disable_img:
            chrome_options.add_argument('blink-settings=imagesEnabled=false')

        if mobile_emulation:
            mobile_emulation = {
                "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
                "userAgent": "Mozilla/5.0 (Linux; Android 9; Pixel 3 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Mobile Safari/537.36"
            }
            chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        chrome_options.add_argument("--user-data-dir=D:\\User_Data")
        chrome_options.add_argument(f"--profile-directory={profile}")
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument("--disable-software-rasterizer")
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')  # 谷歌浏览器去掉访问痕迹
        chrome_options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")
        # chrome_options.add_argument("--window-size=1920,1050")  # 专门应对无头浏览器中不能最大化屏幕的方案
        chrome_options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])
        chrome_options.add_experimental_option('useAutomationExtension', False)

        chrome_options.add_argument('--download.prompt_for_download=false')
        chrome_options.add_argument('--safebrowsing.enabled=false')
        chrome_options.add_argument('--enable-javascript')
        chrome_options.add_argument('--enable-cookies')
        self.driver = webdriver.Chrome(options=chrome_options,
                                       service=service)
        # 修改 webdriver 值
        self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
        })
        self.driver.set_window_size(1200, 800)

        # options = webdriver.FirefoxOptions()
        # profile_directory = 'D:\\temp'
        #
        # profile = webdriver.FirefoxProfile(profile_directory)
        #
        # # options.add_argument('--headless')
        # self.driver = webdriver.Firefox(options=options, executable_path='./geckodriver.exe', firefox_profile=profile)

    def goto_url(self, url):
        self.driver.get(url)  # 打开网页

    def closeChrome(self):
        self.driver.quit()

    # 判断元素是否存在
    def ele_exist(self, by, select):
        try:
            self.driver.find_element(by, select)
            return True
        except Exception as e:
            return False

    def ele_exist_item(self, driver, by, select):
        try:
            driver.find_element(by, select)
            return True
        except Exception as e:
            return False

    def reload_ck(self):
        with open('./cookie.txt', 'r') as f:
            # 读取文件内容
            copied_cookie = f.read()
            cookie_list = [cookie.strip() for cookie in copied_cookie.split(';')]
            for cookie_str in cookie_list:
                cookie_parts = cookie_str.split('=')
                if len(cookie_parts) == 2:
                    cookie = {
                        'domain': '.dianping.com',
                        'name': cookie_parts[0],
                        'value': cookie_parts[1],
                        'path': '/',
                        'httpOnly': False,
                        'HostOnly': False,
                        'Secure': False
                    }
                    self.driver.add_cookie(cookie)
            time.sleep(2)
            self.driver.refresh()

    # 采集商品图片
    def collect_list(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR,
             '#shop-all-list > ul > li')))
        list_items = self.driver.find_elements(By.CSS_SELECTOR, '#shop-all-list > ul > li')
        while True:
            for item in list_items:
                print(item.text)
                href = item.find_element(By.CSS_SELECTOR, 'a').get_attribute("href")
                shopName = item.find_element(By.CSS_SELECTOR, ' div.tit > a > h4').text
                label = item.find_element(By.CSS_SELECTOR, '.tag-addr > a:nth-child(1) > span').text
                avg = '-'
                if self.ele_exist_item(item, By.CSS_SELECTOR, 'div.comment > a.mean-price > b'):
                    avg = item.find_element(By.CSS_SELECTOR, 'div.comment > a.mean-price > b').text
                image = item.find_element(By.CSS_SELECTOR, ' img').get_attribute("src")
                exists = Store.select().where(Store.url == href).exists()
                if not exists:
                    Store.create(
                        url=href,
                        shopName=shopName,
                        originalPrice=avg,
                        frontImg=image
                    )
                else:
                    row_num = Store.update(
                        areaName=label,
                    ).where(Store.url == href).execute()
                    print(f"update {row_num}")
            if not self.ele_exist(By.CSS_SELECTOR, 'body > div.section.Fix.J-shop-search div.page > a.next'):
                print("采集完成")
                break
            self.driver.find_element(By.CSS_SELECTOR,
                                     'body > div.section.Fix.J-shop-search div.page > a.next').click()
            time.sleep(random.randint(6, 10))
            list_items = self.driver.find_elements(By.CSS_SELECTOR, '#shop-all-list > ul > li')

    def collect_detail(self):
        storeList = Store.select().where(Store.addr.is_null())
        for store in storeList:
            url = store.url
            self.goto_url(url)
            wait = WebDriverWait(self.driver, 20)
            wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR,
                 '#basic-info > p')))
            addr = self.driver.find_element(By.CSS_SELECTOR, '#address').text
            scoreIntro = self.driver.find_element(By.CSS_SELECTOR,
                                                  '#basic-info > div.brief-info > div').text

            time.sleep(2)
            if not self.ele_exist(By.CSS_SELECTOR,'#basic-info > a'):
                continue
            self.driver.find_element(By.CSS_SELECTOR, '#basic-info > a').click()
            time.sleep(1)
            yinye_time = self.driver.find_element(By.CSS_SELECTOR,
                                                  '#basic-info > div.other.J-other > p:nth-child(1)').text
            comments = self.driver.find_elements(By.CSS_SELECTOR, '.comment-list.J-list .comment-item')
            posdescr_arr = []
            for item in comments:
                posdescr = {
                }
                try:
                    content = item.find_element(By.CSS_SELECTOR, '.content').text
                    posdescr['content'] = content
                    photos_arr = []
                    if self.ele_exist_item(item, By.CSS_SELECTOR, '.photos .item.J-photo img'):
                        photos = item.find_elements(By.CSS_SELECTOR, '.photos .item.J-photo img')
                        for photo in photos:
                            photos_arr.append(photo.get_attribute("src"))
                            print(photo.get_attribute("src"))
                    posdescr['photos_arr'] = photos_arr
                    posdescr_arr.append(posdescr)
                except Exception as e:
                    print(e)
            row_num = Store.update(
                addr=addr,
                scoreIntro=scoreIntro,
                poiStr='',
                hotelStar=yinye_time,
                posdescr=json.dumps(posdescr_arr, ensure_ascii=False),
            ).where(Store.url == url).execute()

            print(f"更新行{row_num}")
            time.sleep(7)
