from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

page = 0
driver.get(f'https://www.metacritic.com/browse/movies/score/metascore/all/filtered?sort=desc&page={page}')

info_box = driver.find_elements(By.CLASS_NAME, 'clamp-summary-wrap')

titles = []
for box in info_box:
    titles.append(box.find_element(By.TAG_NAME, 'h3'))
for title in titles:
    print(title.text)
driver.quit()
