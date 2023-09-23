from bs4 import BeautifulSoup
import requests
import pandas as pd

# ------------------VARIABLES-----------------
WEB_TO_SCRAP = "https://editorial.rottentomatoes.com/guide/popular-movies/"

scrap_data = requests.get(WEB_TO_SCRAP)

web_scraped = scrap_data.text

soup = BeautifulSoup(web_scraped, "html.parser")
movies = soup.find_all(name="div", class_="article_movie_title")
movie_names = []
df = pd.DataFrame()

for movie in movies:
    movie_name = movie.get_text()
    list = movie_name.strip("\n")
    movie_scraped = list.split("(", 1)
    year_score = movie_scraped[1].split(")")
    name = movie_scraped[0]
    year = year_score[0]
    score = year_score[1]
    movie_list = [name, {"year": year, "score": score}]
    df = df._append(movie_list, ignore_index=True)

df.to_csv("movie_data.csv", sep='\t', encoding='utf-8', index=False)
