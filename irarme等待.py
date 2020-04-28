"""
============================
Author  : XiaoLei.Du
Time    : 2020/4/28 6:59
E-mail  : 506615839@qq.com
File    : irarme等待.py
============================
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.implicitly_wait(30)
driver.get(r'F:\web_project\switch_iframe.html')
driver.find_element_by_id('hello')

# # 通过name切换iframe
# driver.switch_to.frame('baidu')
# driver.find_element_by_id('kw').send_keys('python')

# # 通过索引切换iframe
# driver.switch_to.frame(0)
# driver.find_element_by_id('kw').send_keys('python')

# # 通过元素切换iframe
# frame_ele=driver.find_element_by_xpath('//iframe[@name="baidu"]')
# driver.switch_to.frame(frame_ele)
# driver.find_element_by_id('kw').send_keys('python')

# iframe等待的4种参数方式
# #索引
# WebDriverWait(driver,20).until(EC.frame_to_be_available_and_switch_to_it(0))
# driver.find_element_by_id('kw').send_keys('python')

# # name
# WebDriverWait(driver,20).until(EC.frame_to_be_available_and_switch_to_it('baidu'))
# driver.find_element_by_id('kw').send_keys('python')

# # 元素
# frame_ele=driver.find_element_by_xpath('//iframe[@name="baidu"]')
# WebDriverWait(driver,20).until(EC.frame_to_be_available_and_switch_to_it(frame_ele))
# driver.find_element_by_id('kw').send_keys('python')

# 元祖
WebDriverWait(driver,20).until(EC.frame_to_be_available_and_switch_to_it((By.NAME,'baidu')))
driver.find_element_by_id('kw').send_keys('python')

# # 切换到主页
# driver.switch_to.default_content()
#
# ele=driver.find_element_by_id('hello')
# print(ele.text)

# 切换到父级iframe
driver.switch_to.parent_frame()
ele=driver.find_element_by_id('hello')
print(ele.text)