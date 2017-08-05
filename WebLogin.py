from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

# setup -- requires chromedriver.exe
chrome_path = "C:/Users/Mathias/Documents/DTU/Programmering/chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
action = ActionChains(driver)


# website choice
driver.get("https://www.somewebsite.com")
# a little pause to be able to see what's going on.
time.sleep(1)

# login details via xpaths etc.
driver.find_element_by_xpath("""//*[@id="userID"]""").send_keys("user name")
driver.find_element_by_xpath("""//*[@id="userPW"]""").send_keys("password")
driver.find_element_by_xpath("""//*[@id="frmLogin"]/div/button""").click()

# Additional stuff
time.sleep(1)
driver.find_element_by_xpath("""//*[@id="page-content"]/div[2]/div[1]/table/tbody/tr[4]/td/span[2]/a""").click()

################# Magnus stuff #################

# #Booking site
# time.sleep(0.3)
# funktioner = driver.find_element_by_link_text("Funktioner")
# driver.execute_script("arguments[0].click();",funktioner)
#
# booking = driver.find_element_by_link_text("Booking af lejlighed")
# driver.execute_script("arguments[0].click();",booking)
#
#
# #Choices
#
# #Year
# driver.implicitly_wait(3)
# driver.find_element_by_xpath("""//select[@name='oYearCmb']/option[@value="2018"]""").click()
#
# #Apartment
# time.sleep(3)
# driver.find_element_by_xpath("""//select[@name='oLejCmb']/option[@value="099 "]""").click()