from selenium import webdriver
from  selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path=Service( r"\GitHub\Sazman\Codes\Bakhtiari\udemy\chromedriver.exe")
driver=webdriver.Chrome(service=chrome_driver_path)
driver.get("https://www.python.org/")
event_times=driver.find_elements(By.CSS_SELECTOR,".event-widget time")
event_times=driver.find_elements(By.CSS_SELECTOR,".event-widget li a")
a=[event_times[n].text for n in range(len(event_times))]
# a={"time":event_times[n].text for n in range(len(event_times)) for time in [time.text for time in event_times]}
# list_time=[time.text for time in event_times]
a = {"time":[time.text for time in event_times][n] for n in range(len([time.text for time in event_times])) for time in [time.text for time in event_times]}
print(a)