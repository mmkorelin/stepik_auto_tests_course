import time
from selenium import webdriver

link = "https://archeage.ru/calculator"

browser = webdriver.Chrome()
browser.get(link)

napadenie = browser.find_element_by_css_selector(".tree_1 .type_choose [data-clid='1']").click()
troynoy = browser.find_elements_by_css_selector(".tree_1 .list [data-skill='18132']").click()
rivok = browser.find_elements_by_css_selector(".tree_1 .list [data-skill='11918']").click()
time.sleep(5)
browser.quit()
