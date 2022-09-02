import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:/Users/yanis/Downloads/chromedriver.exe")
driver.get("http://192.168.2.11:8111/")
usuario = driver.find_element(By.ID, "user")
usuario.clear()
usuario.send_keys("root")

password = driver.find_element(By.NAME, "pass")
password.clear()
password.send_keys("password")

driver.find_element(By.XPATH, "/html/body/div/div[2]/div/form/div[3]/div/input").click()

driver.get("http://192.168.2.11:8111/")

time.sleep(10)

driver.find_element(By.XPATH, "/html/body/div/div[1]/div[6]/form[2]/div[1]/input").click()

time.sleep(10)
driver.close()