from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

chromedriver = 'C:/dev_python/Webdriver/chromedriver.exe'
driver = webdriver.Chrome(chromedriver)
driver.get("http://v.media.daum.net/v/20170922175202762")
print("[" + driver.find_element_by_tag_name('title').get_attribute('text') + "]")

loop, count = True, 0

while loop and count < 10:
    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, '#alex-area > div > div > div > div.cmt_box > div.alex_more > button'))
        )
        more_button = driver.find_element_by_css_selector(
            "#alex-area > div > div > div > div.cmt_box > div.alex_more > button")
        webdriver.ActionChains(driver).click(more_button).perform()
        count += 1
        time.sleep(2)
    except TimeoutException:
        loop = False
try:
    element = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.ID, "alex-area"))
    )
except:
    print("댓글 관련 태그가 없습니다.")
else:
    loop = True
    comment_box = driver.find_element_by_css_selector(
        "#alex-area > div > div > div > div.cmt_box > ul.list_comment")
    print(comment_box)
    comment_list = comment_box.find_elements_by_css_selector("li")
    for num, comment_item in enumerate(comment_list):
        print('['+str(num+1)+']',
              comment_item.find_element_by_css_selector("div p").text)
driver.quit()
