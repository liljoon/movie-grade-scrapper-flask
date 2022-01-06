from flask import Flask,render_template,request
from movie_naver import get_movie_info_naver
from movie_daum import get_movie_info_daum

app = Flask("Movie Grade Scrapper")

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/search')
def search():
    movie = request.args.get('movie')
    get_movie_info_daum(movie)
    return render_template("search.html", movie_info_naver = get_movie_info_naver(movie),movie_info_daum=get_movie_info_daum(movie))


app.run()