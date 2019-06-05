from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('http://www.gmail.com')
username = Select(browser.find_element_by_name('Username'))
password = Select(browser.find_element_by_name('Password'))
username.select_by_visible_text("text")
password.select_by_visible_text("text")
username = selenium.find_element_by_id("username")
password = selenium.find_element_by_id("password")

username.send_keys("laxman@arkenea.com")
password.send_keys("Cloud123#")

selenium.find_element_by_name("submit").click()