import requests
from bs4 import BeautifulSoup

def get_movie_info_naver(movie_name):
    r = requests.get(f"https://movie.naver.com/movie/search/result.naver?query={movie_name}")
    bs = BeautifulSoup(r.text,"html.parser")
    try:
        grade = bs.select_one("#old_content > ul:nth-child(4) > li:nth-child(1) > dl > dd.point > em.num").get_text()   
        movie_real_name= bs.select_one('#old_content > ul:nth-child(4) > li:nth-child(1) > dl > dt > a').get_text()
        movie_code_str = bs.select_one('#old_content > ul:nth-child(4) > li:nth-child(1) > dl > dt > a')['href'][-6:]
        img_request = requests.get("https://movie.naver.com/movie/bi/mi/photoViewPopup.naver?movieCode=192150")
        img_bs = BeautifulSoup(img_request.text,"html.parser")
        img_src = img_bs.select_one("#targetImage")['src']
    except:                            
        grade=0.0
        movie_real_name=""


    return {'grade':grade, 'movie_real_name':movie_real_name, 'movie_code':movie_code_str,'img_src' : img_src}    