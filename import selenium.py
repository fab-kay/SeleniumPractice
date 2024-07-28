from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Return to index"))
    )
    link = driver.find_element(by=By.LINK_TEXT, value="Return to index")
    link.click()
except:
    print(element.tag_name)



#search = driver.find_element(by=By.ID, value="my-text-id")
#see = driver.find_element(by=By.CSS_SELECTOR, value=)
#search.clear()
#search.send_keys("test")
#search.send_keys(Keys.RETURN)
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "alerts.html"))
    )
    link = element.find_element(by=By.LINK_TEXT, value="alerts.html")
    link.click()

    #makeups = element.find_elements(by=By.TAG_NAME, "input")
    #for makeup in makeups
     #   header = element.find_elements(by=By.CLASS_NAME("see"))
      #  print(header.text)
except:
   print(element.id)

#print(driver.page_source)

#driver.back()
#driver.forward()
print(search.text)

print(driver.title)




