"""
============================
Author  : XiaoLei.Du
Time    : 2020/1/12 16:59
E-mail  : 506615839@qq.com
File    : 0110.py
============================
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 新增浏览器
driver=webdriver.Chrome()
# 打开百度首页
driver.get('https://www.baidu.com')
# 窗口最大化
driver.maximize_window()
# 创建显示等待定时器
wait=WebDriverWait(driver,30,0.2)
wait.until(EC.visibility_of_element_located((By.ID,'kw')))
driver.find_element_by_id('kw').send_keys('柠檬班')
wait.until(EC.visibility_of_element_located((By.ID,'kw')))
driver.find_element_by_id('kw').submit()
wait.until(EC.visibility_of_element_located((By.XPATH,'(//h3[@class="t"]/a)[1]')))
driver.find_element_by_xpath('(//h3[@class="t"]/a)[1]').click()
# 获取窗口句柄
w=driver.window_handles
# 定位最新打开的窗口句柄
driver.switch_to.window(w[-1])
wait.until(EC.visibility_of_element_located((By.XPATH,'//h4[text()="小简"]')))
driver.find_element_by_xpath('//h4[text()="小简"]').click()

driver.quit()
