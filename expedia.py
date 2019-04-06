from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
driver.get("https://www.expedia.com/")
# time.sleep(3)
driver.find_element_by_id('tab-flight-tab-hp').click()
time.sleep(2)
elem_1 = driver.find_element_by_xpath('//*[@id="flight-origin-hp-flight"]').send_keys("SFO")
time.sleep(2)
elem_2 = driver.find_element_by_id('flight-destination-hp-flight').send_keys("NYC")
time.sleep(2)
elem_3 = driver.find_element_by_id('flight-departing-hp-flight').send_keys("04/05/2019")
time.sleep(2)
driver.find_element_by_id('flight-returning-hp-flight').clear()
time.sleep(2)
elem_4 = driver.find_element_by_id('flight-returning-hp-flight').send_keys("04/06/2019")
time.sleep(2)
driver.find_element_by_xpath("/html/body/meso-native-marquee/section/div/div/div[1]/section/div/div[2]/div[2]/section[1]/form/div[7]/label/button").click()
