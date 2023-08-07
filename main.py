import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

def linkedin_search(query):
    chromedriver_path = "/Users/jaspreetSinghSodhi/downloads/chromedriver"

    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Maximize the browser window

    driver = webdriver.Chrome( options=chrome_options)

    load_dotenv()


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



       

        search_all_result = driver.find_elements("xpath" ,"//div[@class='search-results__cluster-bottom-banner artdeco-button artdeco-button--tertiary artdeco-button--muted']")

        search_all_result[2].click()

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the browser after the task is completed
       while True:
           pass
        #driver.close()

if __name__ == "__main__":
    search_query = "Data Analyst"
    linkedin_search(search_query)
    while True:
        pass    
