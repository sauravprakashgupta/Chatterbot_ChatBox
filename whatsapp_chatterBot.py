from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
botdriver = webdriver.Firefox(executable_path='D:\\Firefox\\geckodriver')
botdriver.get("https://web.whatsapp.com/")
Chatname=input("Enter  Friend Name")
Chatmsg=input("Enter Message")
NoCount=int(input("Enter Count"))

input("Enter Anything after Scanning or Code")
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(Chatname))

user.click()
msg_box = driver.find_element_by_class_name('_2S1VP')
for i in range(NoCount):
       msg_box.send_keys(Chatmsg)
       button=driver.find_element_by_class_name('_35EW6')
       button.click()
