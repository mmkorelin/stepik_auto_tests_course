from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
url = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(url)
browser.find_element_by_class_name("btn").click()
browser.switch_to.window(browser.window_handles[1])
x = browser.find_element_by_id("input_value").text
y = calc(x)
browser.find_element_by_id("answer").send_keys(y)
browser.find_element_by_class_name("btn").click()


time.sleep(5)
browser.quit()