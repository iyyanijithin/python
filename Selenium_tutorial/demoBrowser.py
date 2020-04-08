from selenium import webdriver

#ID
#Name
#CSS
#XPath


driver = webdriver.Chrome(executable_path="C:\Work\selenium\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
#What are locators
#ID - findElementById
#Name - find
#Find element by name
driver.find_element_by_name('name').send_keys('roger')
#Find element by id
driver.find_element_by_id('exampleCheck1').click()
driver.find_element_by_name('email').send_keys('roger@gmail.com')
#Xpath and CSS selector will always be there

#CSS selector  tagname[attribute='value'}
# check this in  browser console $("input[name='name']")
driver.find_element_by_css_selector("input[name='name'").send_keys('roger12')
#By default selenium will start from top to bottom


#Xpath
#//tagname[@attribute=value]
# check this in  browser console $x("//input[@type='submit']")
driver.find_element_by_xpath("//input[@type='submit']").submit()

print(driver.find_element_by_class_name("alert-success").text)


#find_element_by_link_text



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
