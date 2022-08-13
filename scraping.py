from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

page = 0
driver.get(f'https://www.metacritic.com/browse/movies/score/metascore/all/filtered?sort=desc&page={page}')

info_box = driver.find_elements(By.CLASS_NAME, 'clamp-summary-wrap')

class Movie:
    def __init__(self, title, score):
        self.title = title
        self.score = score

movies = []

for box in info_box:
    title = box.find_element(By.TAG_NAME, 'h3').text
    score = box.find_element(By.CLASS_NAME, 'metascore_w').text
    score = int(score)
    
    if score < 100:
        break
    movies.append(Movie(title, score))
    
for movie in movies:
    print(movie.title, movie.score)
driver.quit()
