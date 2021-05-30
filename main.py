import os
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir={}\driver_data".format(os.getcwd()))

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver.get("https://linkedin.com")
while "1" != input("press 1 when signed in: "):
    pass
driver.get("https://linkedin.com/mynetwork/")
sleep(2)
buttons = driver.find_elements_by_class_name("invitation-cgiard__action-btn")
for button in buttons:
    label = button.get_attribute("aria-label");
    word = label.split(' ')[0];
    if word == 'Accept':
        print("Accepting...")
        button.click()
        print("Accepted")
print("Done!")
driver.close()
