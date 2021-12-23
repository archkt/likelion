import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

movies = soup.select('#old_content > table > tbody > tr')
for movie in movies:
    # movie 안에 a 가 있으면,

    rank = movie.select_one("td.ac > img['alt']")
    title = movie.select_one("td.title > div > a")
    print(rank)
    '''if title is not None:
        # a의 text를 찍어본다.
        print (a_tag.text)'''
