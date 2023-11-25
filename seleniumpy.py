
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#Success login         
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID,"user-name").send_keys("standard_user")   
driver.find_element(By.ID,"password").send_keys("secret_sauce") 
driver.find_element(By.ID,"login-button").click()  
time.sleep(2)


#failed login         
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID,"user-name").send_keys("lala")   
driver.find_element(By.ID,"password").send_keys("secret_sauce") 
driver.find_element(By.ID,"login-button").click()  
time.sleep(2)

#Test logout button        
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID,"user-name").send_keys("standard_user")   
driver.find_element(By.ID,"password").send_keys("secret_sauce") 
driver.find_element(By.ID,"login-button").click()  
driver.find_element(By.ID,"react-burger-menu-btn").click()
time.sleep(1)
driver.find_element(By.ID,"logout_sidebar_link").click()    
time.sleep(2)


#Add one product to chart
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID,"user-name").send_keys("standard_user")   
driver.find_element(By.ID,"password").send_keys("secret_sauce") 
driver.find_element(By.ID,"login-button").click()
time.sleep(1)
driver.find_element(By.ID,"add-to-cart-sauce-labs-bike-light").click()
time.sleep(1)
driver.find_element(By.ID,"shopping_cart_container").click()    
time.sleep(2)


#Remove product from chart         
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID,"user-name").send_keys("standard_user")   
driver.find_element(By.ID,"password").send_keys("secret_sauce") 
driver.find_element(By.ID,"login-button").click()
time.sleep(1)
driver.find_element(By.ID,"add-to-cart-sauce-labs-bike-light").click()
time.sleep(1)
driver.find_element(By.ID,"shopping_cart_container").click()    
time.sleep(2)
driver.find_element(By.ID,"remove-sauce-labs-bike-light").click()    
time.sleep(1)