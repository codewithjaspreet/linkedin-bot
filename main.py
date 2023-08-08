import csv
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chromedriver_path = "/Users/jaspreetSinghSodhi/downloads/chromedriver"

chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Maximize the browser window

driver = webdriver.Chrome( options=chrome_options)

load_dotenv()

def linkedin_search(query):
    


    try:
        # Open LinkedIn in Chrome
        driver.get("https://www.linkedin.com/feed/")


        signup = driver.find_element("xpath" , "//a[@data-tracking-control-name='cold_join_sign_in']")



        signup.click()


        # Find the username field

        email = driver.find_element("xpath" , "//input[@id='username']")

        # enter password

        password = driver.find_element("xpath" , "//input[@id='password']")

        email.send_keys(os.getenv("user_id"))
        password.send_keys(os.getenv("password"))

        # click on login button

        signin_btn = driver.find_element("xpath" , "//button[@aria-label = 'Sign in']")

        signin_btn.click()

        # Find the search box and enter the query
        search_box = driver.find_element("xpath" , "//input[@aria-label='Search']")
        search_box.send_keys(query)

        # Press Enter to initiate the search
        search_box.send_keys(Keys.RETURN)

        wait = WebDriverWait(driver, 5)
        buttons = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//button[@aria-pressed='false']")))

        print(len(buttons))
        # print(buttons)

        buttons[1].click()

        scrape_people_info()



    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the browser after the task is completed
       while True:
           pass
        #driver.close()


def scrape_people_info():


    wait  =    WebDriverWait(driver, 5)

    people_area = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//li[@class='reusable-search__result-container']//div[@class='mb1']//span[@dir='ltr']//span[@aria-hidden='true']")))

    positions =  wait.until(EC.presence_of_all_elements_located((By.XPATH, "//li[@class='reusable-search__result-container']//div[@class='mb1']//div[@class='entity-result__primary-subtitle t-14 t-black t-normal']")))

    profiles =  wait.until(EC.presence_of_all_elements_located((By.XPATH, "//li[@class='reusable-search__result-container']//div[@class='mb1']//a")))
    
    Names = []
    Positions = []
    Links =  []

    print(len(people_area))
    print(len(positions))

    for person in people_area:

        Names.append(person.text)
        print(person.text)

    
    print("--------------------")

    for position in positions:
            
        Positions.append(position.text)
        print(position.text)

    print("--------------------")

    for profile in profiles:
        Links.append(profile.get_attribute("href"))
        print(profile.get_attribute("href"))


    make_dataframe(Names , Positions , Links)
    
def make_dataframe(l1 , l2 , l3):

    
    rows = zip(l1, l2, l3)

    with open('Linkdin.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Header1', 'Header2', 'Header3'])  
        writer.writerows(rows)



if __name__ == "__main__":
    search_query = "Data Analyst"
    linkedin_search(search_query)
    while True:
        pass    
