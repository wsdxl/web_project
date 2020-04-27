"""
============================
Author  : XiaoLei.Du
Time    : 2020/4/26 23:04
E-mail  : 506615839@qq.com
File    : 窗口切换.py
============================
"""
from selenium import webdriver

driver=webdriver.Chrome()
driver.implicitly_wait(30)
driver.get('http://www.baidu.com')
input_ele=driver.find_element_by_id('kw')
input_ele.send_keys('柠檬班')

driver.find_element_by_id('su').click()

ketang=driver.find_element_by_xpath('//*[contains(text(),"lemon.ke.qq.com")]')
ketang.click()

# 获取所有窗口句柄
handle=driver.window_handles
# print(handle)
# 切换窗口
driver.switch_to.window(handle[-1])

hua=driver.find_element_by_xpath('//*[contains(text(),"华华老师")]')
print(hua.text)