from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

chromedriver = 'C:/dev_python/Webdriver/chromedriver.exe'
driver = webdriver.Chrome(chromedriver)
driver.get("http://pythonscraping.com/pages/files/form.html")


firstnameField = driver.find_element_by_name("firstname")
lastnameField = driver.find_element_by_name("lastname")
submitButton = driver.find_element_by_id("submit")

firstnameField.send_keys("Doky")
lastnameField.send_keys("Kim")
submitButton.click()
print(driver.find_element_by_tag_name("body").text)
driver.close()
