import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)

web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

best_movies = soup.find_all("h3", class_="title")
best_movies_names = [movie.getText() for movie in best_movies]
best_movies_names.reverse()

with open("100_movies.txt", "w", encoding='utf-8') as f:

    for best_movies_name in best_movies_names:
    # print(best_movies_name)
        f.write(f"{best_movies_name}\n")
