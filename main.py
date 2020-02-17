from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import pickle


def save_csv(companies):
    """Save top 500 stocks in base on volumn to a csv file"""
    print("Saving companies.csv...")

    Path("output").mkdir(parents=True, exist_ok=True)
    file_name = 'output/companies.csv'

    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        i = 0
        while i < 500:
            company = companies[i]
            name = company.text
            url = company.get_attribute('href')
            writer.writerow([name, url])
            i = i + 1
    
    print('companies.csv created')

def save_pickle(companies):
    """Save top 500 stocks in base on volumn to pickle file"""
    print("Saving companies.pickle...")

    Path("output").mkdir(parents=True, exist_ok=True)
    file_name = 'output/companies.pickle'

    companies_dict = {}
    i = 0
    while i < 500:
        company = companies[i]
        companies_dict[company.text] = {
            "name": company.text,
            "url": company.get_attribute('href'),
        }
        i += 1

    with open(file_name, 'wb') as handle:
        pickle.dump(companies_dict, handle)

    print('companies.pickle created')
       

if __name__ == "__main__":

    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    driver = webdriver.Chrome(options=options)

    driver.get("https://au.investing.com/equities/australia")

    driver.implicitly_wait(5)
    all_stocks = driver.find_element_by_xpath(
        '//select[@id="stocksFilter"]/option[@id="all"]')
    all_stocks.click()
    try:
        element = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(
                (By.ID, "cross_rate_markets_stocks_1"))
        )
        driver.find_element_by_xpath('//th[@data-col-caption="Vol"]')
        driver.implicitly_wait(5)
        driver.find_element_by_xpath('//th[@data-col-caption="Vol"]')
        driver.implicitly_wait(5)
        companies = element.find_elements_by_xpath('./tbody/tr/td[2]/a')
        # save_csv(companies)
        save_pickle(companies)
    finally:
        driver.quit()
    driver.quit()
