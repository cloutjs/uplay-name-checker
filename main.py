from selenium import webdriver
from colorama import Fore
from selenium.common.exceptions import NoSuchElementException
import time
import os
from os import system

if not os.path.exists("names.txt"):
    ee= open("names.txt", "w+")
if not os.path.exists("availables.txt"):
    eee= open("availables.txt", "w+")

hits = 0
count = 0

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--headless')
browser = webdriver.Chrome("chromedriver.exe", options=options)
content = browser.page_source

with open('names.txt') as e:
    usernames = e.read().splitlines()
    for name in usernames:
        count = count + 1
        try:
            browser.get("https://r6db.net/namecheck/")
            browser.find_element_by_xpath("//input[@class='InputField']").send_keys(name)
            time.sleep(1)
            browser.find_element_by_class_name("not-available")
            print(f"{Fore.RED}[-] {name}")
            system(f"title Uplay Name Checker by clout // Checked: {count}/{len(usernames)} - Hits: {hits}")
        except NoSuchElementException:
            print(f"{Fore.GREEN}[+] {name}")
            open('availables.txt','a+').write("{}\n".format(name))
            hits = hits + 1
            system(f"title Uplay Name Checker by clout // Checked: {count}/{len(usernames)} - Hits: {hits}")
        except:
            print(f"{Fore.RED}[!] You are rate limited")
            system(f"title Uplay Name Checker by clout // Checked: {count}/{len(usernames)} - Hits: {hits}")
print(f"{Fore.WHITE}\n\nDone Checking")
