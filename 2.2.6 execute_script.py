from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"
browser.get(link)

x_value = browser.find_element_by_id("input_value").text

x = calc(x_value)

button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button) #прокрутка экрана до кнопки
button.click()
browser.find_element_by_id("answer").send_keys(x)
browser.find_element_by_id("robotCheckbox").click()
browser.find_element_by_id("robotsRule").click()
browser.find_element_by_css_selector(".btn").click()
time.sleep(5)
browser.quit()