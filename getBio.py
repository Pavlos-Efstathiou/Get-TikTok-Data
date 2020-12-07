from selenium import webdriver
from time import sleep

def getBio():
    tiktok_user = input("Enter a TikTok user\n")
    PATH = "chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://tiktok.com/@{}".format(tiktok_user))
    sleep(1.5)
    if driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/main/div/p[1]").text != "Couldn't find this account":
        bio = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/header/h2[2]")
        print("{}'s bio:\n".format(tiktok_user, bio.get_attribute('innerHTML')))
        driver.close()
    elif driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/main/div/p[1]").text == "Couldn't find this account":
        print("User not found!")
        driver.close()