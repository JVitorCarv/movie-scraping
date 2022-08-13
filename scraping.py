from selenium import webdriver

driver = webdriver.Chrome()

year = 2021
driver.get(f'https://www.metacritic.com/browse/movies/score/metascore/year/filtered?year_selected={year}&sort=desc')

driver.quit()
