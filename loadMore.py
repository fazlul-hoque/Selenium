

#Author: Md.Fazlul Hoque
#Source: Stackoverflow and answered by the author
#Source link: https://stackoverflow.com/questions/74417476/use-selenium-to-click-a-load-more-button-not-working/74419758#74419758


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import pandas as pd

s=Service('./chromedriver')
driver= webdriver.Chrome(service=s)
url='https://money.tmx.com/en/quote/AMK/news'
driver.get(url)
driver.maximize_window()
time.sleep(5)

data = []
for x in range(3):
    try:
        soup = BeautifulSoup(driver.page_source, 'lxml')
        cards = soup.select('ol.sc-ddCvFA.jCEzJs li')
        print(len(cards))
        for x in cards:
            h3 = x.h3.get_text(strip=True)
            data.append(h3)
            
        loadMoreButton = driver.find_element(By.XPATH, "//button[contains(text(),'Load more')]")
            
        if loadMoreButton:
            driver.execute_script("arguments[0].click();" ,loadMoreButton)
            #loadMoreButton.click()
            time.sleep(3)
    except Exception as e:
        print(e)
        break
print(set(data))

# df = pd.DataFrame(set(data))
# print(df)