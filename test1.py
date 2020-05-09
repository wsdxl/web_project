"""
============================
Author  : XiaoLei.Du
Time    : 2020/2/7 12:12
E-mail  : 506615839@qq.com
File    : test1.py
============================
"""
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.get('http://www.baidu.com')
# # time.sleep(2)
# driver.implicitly_wait(30)


# #第一步：初始化等待器
# # 定时器，等待器，poll_frequency（轮询时间，频率）
# wait=WebDriverWait(driver,30,0.2)
#
# # 第二步：初始化定位器
# locator = ('xpath', "//input[@id='kw']")
#
# # 第三步：将定位器加入条件当中
# # 元素被看见,可视
# condition1=EC.visibility_of_element_located(locator)
#
# # 元素被加载
# condition=EC.presence_of_element_located(locator)
#
# # 元素被点击
# condition2=EC.element_to_be_clickable(locator)
#
# # 第四步：将条件加到等待器中
# wait.until(condition)
# wait.until(condition1)
# wait.until(condition2)

# # 整合到一起
# e=WebDriverWait(driver,30,0.2).until(
#     EC.visibility_of_element_located((By.XPATH,'//input[@id="kw"]')))
# print(e)


# 自己封装一个显示等待的方法
# 偷懒的方法,弄懂显示等待的原理
# def wait_element(driver, timeout, poll_frequency, locator):
#     used_time = 0
#     while used_time < timeout:
#         try:
#             e = driver.find_element(*locator)
#             return e
#         except:
#             time.sleep(poll_frequency)
#             used_time += poll_frequency
#     # 超时了
#     raise TimeoutError('元素定位超时')
#
# e=wait_element(driver,30,0.2,('id','kw'))
# e.send_keys('柠檬班')
import random
f=open("num.txt","w")
list1=[]
for i in range(10):
    num=random.randint(0,1000)
    list1.append(str(num))

f.write(",".join(list1))
f.close()