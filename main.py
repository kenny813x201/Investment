from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv


def save_csv(element):
    companies = element.find_elements_by_xpath('./tbody/tr/td[2]/a')

    Path("output").mkdir(parents=True, exist_ok=True)
    file_name = 'output/companies.csv'

    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for company in companies:
            name = company.text
            url = company.get_attribute('href')
            writer.writerow([name, url])


if __name__ == "__main__":

    driver = webdriver.Chrome()
    driver.get("https://au.investing.com/equities/australia")

    all_stocks = driver.find_element_by_xpath(
        '//select[@id="stocksFilter"]/option[@id="all"]')
    all_stocks.click()
    try:
        element = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(
                (By.ID, "cross_rate_markets_stocks_1"))
        )
        save_csv(element)
        print('Create companies.csv')
    finally:
        driver.quit()
    driver.quit()
