import requests
from bs4 import BeautifulSoup

def get_movie_info_daum(movie_name):
    
    r = requests.get(f"https://search.daum.net/search?w=tot&q={movie_name}")
    bs = BeautifulSoup(r.text,"html.parser")
    movie_link = bs.select_one("#movieTitle > a")['href']
    r = requests.get(movie_link)
    bs = BeautifulSoup(r.text,"html.parser")
    movie_grade = bs.select_one("#mainContent > div > div.box_basic > div.info_detail > div.detail_cont > div:nth-child(2) > dl:nth-child(1) > dd").get_text()
    movie_full_name = bs.find(class_='txt_tit').get_text()
    img_link = bs.select_one("#mainContent > div > div.box_basic > div.info_poster > a")['href']


    return {'grade': movie_grade,'movie_full_name':movie_full_name}