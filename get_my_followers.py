from bot import Bot
import argparse
from selenium.webdriver.chrome.service import Service as ChromeService  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def generate_my_followers_txt(my_followers):
    print(my_followers)
    my_followers_txt = open("my_followers.txt", 'w+')
    for follower in my_followers:
        my_followers_txt.write(follower + "\n")


def get_my_followers(config):
    username = config.username
    password = config.password
    b = Bot()

    b.setUp()
    b.go_to_page("https://www.instagram.com/accounts/login/")
    # Wait for the login page to load fully
    WebDriverWait(b.driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))

    b.login(username, password)

    my_followers = b.get_my_followers(username)
    generate_my_followers_txt(my_followers)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    chromedriver_path = 'C:\\Users\\Suma Marri\\Documents\\InstagramScrape\\chromedriver\\chromedriver.exe'
    chrome_service = ChromeService(executable_path=chromedriver_path)  # Create a ChromeService object

    # input parameters
    parser.add_argument('--username', type=str)
    parser.add_argument('--password', type=str)

    config = parser.parse_args()

    get_my_followers(config)
