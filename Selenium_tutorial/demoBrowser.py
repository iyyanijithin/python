from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Work\selenium\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)
print(driver.current_url)
driver.maximize_window()
#driver.back()
#driver.refresh()
#this is to close only current window
#driver.close()
#This is to close all windows

#Web locators and types of locators


driver.quit()