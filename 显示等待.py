"""
============================
Author  : XiaoLei.Du
Time    : 2020/4/27 6:55
E-mail  : 506615839@qq.com
File    : 显示等待.py
============================
"""
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.implicitly_wait(30)
driver.get('http://www.baidu.com')

# #第一步：初始化等待器
# wait=WebDriverWait(driver,30,0.2)
#
# #第二步：初始化定位器
# locator= (By.XPATH,'//input[@id="kw"]')
#
# #第三步：将定位器加入到条件中
# condition=EC.visibility_of_element_located(locator)
#
# #第四步：将条件加入到等待器中
# e=wait.until(condition)
# e.send_keys('课堂派')

# # 整合起来
# e=WebDriverWait(driver,30,0.2).until(
#     EC.visibility_of_element_located((By.ID,'kw')))
# e.send_keys('课堂派')

# 自己封装一个显示等待函数
# def wait_element(driver,timeout,poll_frequency,locator):
# #     use_time=0
# #     while use_time<timeout:
# #         try:
# #             e=driver.find_element(*locator)
# #             return e
# #         except:
# #             time.sleep(poll_frequency)
# #             timeout+=poll_frequency
# #     raise TimeoutError
# #
# #
# #
# # ele=wait_element(driver,30,0.2,('id','kw'))
# # ele.send_keys('课堂派')
