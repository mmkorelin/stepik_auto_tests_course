from selenium import webdriver
import time
import os

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)



browser.find_element_by_name("firstname").send_keys("Иван")
browser.find_element_by_name("lastname").send_keys("Иванов")
browser.find_element_by_name("email").send_keys("IvanovIvan@mail.ru")

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'text.txt')           # добавляем к этому пути имя файла
#element.send_keys(file_path)
browser.find_element_by_id("file").send_keys(file_path)
browser.find_element_by_class_name("btn").click()
time.sleep(5)
browser.quit()