from selenium import webdriver
from time import sleep


def getFollowers():
    tiktok_user = input("Enter a TikTok user\n")
    PATH = "chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://tiktok.com/@{}".format(tiktok_user))
    sleep(2)
    if driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/main/div/p[1]").text != "Couldn't find this account":
        followers = driver.find_element_by_xpath(
            "/html/body/div/div/div[2]/div[2]/div/header/h2[1]/div[3]/strong").text
        print("{} has {} followers".format(tiktok_user, followers))
        driver.close()
    elif driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/main/div/p[1]").text == "Couldn't find this account":
        print("User not found!")
        driver.close()
