from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver= webdriver.Chrome("WebDriver location")
driver.get("Enter the Url here")


emailid=driver.find_element_by_id("identifierId")
emailid.send_keys("Your email Id")

passw=driver.find_element_by_name("password")
passw.send_keys("Your Password")


signin=driver.find_element_by_id("passwordNext")
signin.click()
