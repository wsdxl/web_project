"""
============================
Author  : XiaoLei.Du
Time    : 2020/4/28 7:43
E-mail  : 506615839@qq.com
File    : alert切换.py
============================
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.implicitly_wait(30)
driver.get(r'F:\web_project\switch_iframe.html')
driver.find_element_by_id('hello').click()

#切换到alert弹框对象
# al=driver.switch_to.alert
# # alert弹框确定
# al.accept()
#
# # alert弹框取消
# al.dismiss()

al=WebDriverWait(driver,20).until(EC.alert_is_present())
al.accept()
e=driver.find_element_by_id('hello')
print(e.text)
