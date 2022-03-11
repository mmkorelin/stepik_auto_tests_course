from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)
x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)
input = browser.find_element_by_id("answer").send_keys(y)
check_box = browser.find_element_by_id("robotCheckbox").click()
opt_box = browser.find_element_by_id("robotsRule").click()
btn = browser.find_element_by_class_name("btn").click()
time.sleep(5)
browser.quit()
