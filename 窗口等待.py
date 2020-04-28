"""
============================
Author  : XiaoLei.Du
Time    : 2020/4/28 6:48
E-mail  : 506615839@qq.com
File    : 窗口等待.py
============================
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.implicitly_wait(30)
driver.get('http://www.baidu.com')
input_ele=driver.find_element_by_id('kw')
input_ele.send_keys('柠檬班')

driver.find_element_by_id('su').click()

ketang=driver.find_element_by_xpath('//*[contains(text(),"lemon.ke.qq.com")]')

# 点击前获取所有的页面句柄
old_handle=driver.window_handles

ketang.click()

#显示等待，知道新窗口打开
WebDriverWait(driver,20).until(EC.new_window_is_opened(old_handle))

# 切换到新页面句柄
driver.switch_to.window(driver.window_handles[-1])
# # 获取所有窗口句柄
# handle=driver.window_handles
# # print(handle)
# # 切换窗口
# driver.switch_to.window(handle[-1])

hua=driver.find_element_by_xpath('//*[contains(text(),"华华老师")]')
print(hua.text)