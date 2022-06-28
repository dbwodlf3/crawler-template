# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))


driver.get("https://twitter.com/?lang=ko")
