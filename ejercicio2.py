from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:\\Users\\Maria\\workspaces\\test-lab\\chromedriver.exe")

driver.get("https://www3.animeflv.net/")

link = driver. find_element(By.CSS_SELECTOR)
assert ultimo_episodio == 1003
