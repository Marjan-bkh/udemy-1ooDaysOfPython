from selenium import webdriver
from  selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path=Service( r"\GitHub\Sazman\Codes\Bakhtiari\udemy\chromedriver.exe")
# driver=webdriver.Chrome(service=chrome_driver_path)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# article_count=driver.find_element(By.CSS_SELECTOR,"#articlecount a")
# print(article_count.text)

driver=webdriver.Chrome(service=chrome_driver_path)
driver.get("http://secure-retreat-92358.herokuapp.com/")
fname = driver.find_element(By.NAME,"fName")
fname.send_keys("Mar")
lname=driver.find_element(By.NAME,"lName")
lname.send_keys("Jan")
email=driver.find_element(By.NAME,"email")
email.send_keys("bakhtiari_marjan@yahoo.com")
singup=driver.find_element(By.TAG_NAME,"button")
singup.click()
