from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv


def save_csv(element):
    """Save top 500 stocks in base on volumn"""
    print("Saving companies.csv...")
    companies = element.find_elements_by_xpath('./tbody/tr/td[2]/a')

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


if __name__ == "__main__":

    options = webdriver.ChromeOptions()
    # options.add_argument("headless")
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
        save_csv(element)
        print('companies.csv created')
    finally:
        driver.quit()
    driver.quit()
