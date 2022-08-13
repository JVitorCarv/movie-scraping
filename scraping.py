from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

class Movie:
    def __init__(self, title, score):
        self.title = title
        self.score = score

def get_max_page():
    driver.get('https://www.metacritic.com/browse/movies/score/metascore/all/filtered?sort=desc&page=0')
    last_page = driver.find_element(By.CLASS_NAME, 'last_page').find_element(By.CLASS_NAME, 'page_num')
    return int(last_page.text)

def get_movies_from(min_score, page = 0):
    movies = []
    max_page = get_max_page()
    
    score = 100
    while score >= min_score and page < max_page:
        driver.get(f'https://www.metacritic.com/browse/movies/score/metascore/all/filtered?sort=desc&page={page}')
        
        info_box = driver.find_elements(By.CLASS_NAME, 'clamp-summary-wrap')
        for movie in info_box:
            title = movie.find_element(By.TAG_NAME, 'h3').text
            score = movie.find_element(By.CLASS_NAME, 'metascore_w').text
            score = int(score)
            
            if score >= min_score:
                movies.append(Movie(title, score))
            else:
                return movies
        page += 1
        
    return movies

movies = get_movies_from(0, 148)
    
for movie in movies:
    print(movie.title, movie.score)
driver.quit()
