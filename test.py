"""
============================
Author  : XiaoLei.Du
Time    : 2019/12/25 21:41
E-mail  : 506615839@qq.com
File    : test.py
============================
"""
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.baidu.com')
# # 获取当前网页
# print(driver.current_url)
# # 获取当前网页标题
# print(driver.title)
# # 获取网页源代码
# print(driver.page_source)

# # 获取所有窗口，所有标签页
# # print(driver.window_handles)
# #
# # # 获取当前标签页
# # print(driver.current_window_handle)


driver.maximize_window()
# driver.minimize_window()
# driver.set_window_size('400','300')
# driver.find_element_by_xpath('//input[@class="s_ipt"]').send_keys('课堂派')
# driver.find_element_by_xpath('//input[@id="su"]').click()
# # driver.find_element_by_xpath('//div[@id="2"]/h3/a').click()
# driver.back()
# time.sleep(1)
# driver.forward()
# time.sleep(1)
# driver.refresh()
# time.sleep(1)
# driver.quit()
# ele=driver.find_element_by_xpath('(//a[contains(text(),"新")])[1]')
# print(ele)


# #父子关系
# ele=driver.find_element_by_xpath('//form[@id="form"]//input[@class="s_ipt"]')

driver.find_element_by_id('kw').send_keys('柠檬班')
driver.find_element_by_id('su').click()
ketang=driver.find_element_by_xpath('//*[contains(text(),"lemon.ke.qq.com")]')
ketang.click()
handler=driver.window_handles
driver.switch_to.window(handler[-1])
e=driver.find_element_by_xpath('//h4[text()="小简"]')
print(e.text)

