from selenium.webdriver import ActionChains
from selenium import webdriver
import time
'''
1.鼠标悬停到设置
2.点击高级设置
'''
driver=webdriver.Chrome()
driver.implicitly_wait(20)
driver.maximize_window()
driver.get('https://www.baidu.com')
# 鼠标悬停到设置
# 第一步：初始化actionchains
action=ActionChains(driver)
# 第二步： 定位要操作的元素
ele=driver.find_element_by_xpath('//span[@name="tj_settingicon"]')
# 第三步：执行对应的操作，右击
action.move_to_element(ele).perform()
# 第四步：操作完以后要释放动作
# action.perform()
# time.sleep(2)

# 点击高级搜索
ele1=driver.find_element_by_xpath('//a[text()="高级搜索"]')
action.click(ele1).perform()
# action.perform()