from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.implicitly_wait(30)
#maximize's browser window
driver.maximize_window()
#navigate to given url
driver.get("http://www.amazon.com")
#prints title on to console
print (driver.title)

textBox = driver.find_element_by_id("twotabsearchtextbox").send_keys("phone")

search = driver.find_element_by_xpath("//input[@class='nav-input']").click()

#quits the browser
driver.quit()