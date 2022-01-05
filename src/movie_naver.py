import requests
from bs4 import BeautifulSoup

def get_movie_info_naver(movie_name):
    r = requests.get(f"https://movie.naver.com/movie/search/result.naver?query={movie_name}")
    bs = BeautifulSoup(r.text,"html.parser")
    print(r.text)
    try:
        grade = bs.select_one("#old_content > ul:nth-child(4) > li:nth-child(1) > dl > dd.point > em.num").get_text()   
        movie_real_name= bs.select_one('#old_content > ul:nth-child(4) > li:nth-child(1) > dl > dt > a').get_text()
    except:                            
        grade=0.0
        movie_real_name=""


    return {'grade':grade, 'movie_real_name':movie_real_name}    