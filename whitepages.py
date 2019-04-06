from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
driver.get("https://www.whitepages.com/")
time.sleep(5)
driver.find_element_by_xpath("//*[@id='header']/div/ul/li[4]/div/span").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='key']").send_keys("Real Estate")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='where']").send_keys("New York")
driver.find_element_by_class_name("new-search").click()

driver.close()
