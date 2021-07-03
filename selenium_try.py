# selenium_to_try_20210504AM1
import time

from selenium import webdriver

wd = webdriver.Chrome(r'F:\chromedriver_win32\chromedriver.exe')
wd.get('https://www.baidu.com')

element = wd.find_element_by_id('kw')
wd.implicitly_wait(3)
element.send_keys('python\n')
# wd.find_element_by_id('#form > span.bg.s_btn_wr').click()

time.sleep(15)
wd.quit()
