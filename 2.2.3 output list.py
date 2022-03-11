from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

num1 = browser.find_element_by_id("num1").text
num2 = browser.find_element_by_id("num2").text
Sum = str(int(num1) + int(num2))
select = Select(browser.find_element_by_id("dropdown"))
select.select_by_value(Sum)
browser.find_element_by_css_selector(".btn").click()

# browser.find_element_by_id("dropdown").click()
# browser.find_element_by_css_selector("[value=Sum]").click()
time.sleep(5)
browser.quit()