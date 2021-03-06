from pymongo.operations import UpdateMany
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient as mc

client = mc('localhost', 27017)     # set client
db = client.likelion                # db name

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
#data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
#soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
#movies = soup.select('#old_content > table > tbody > tr')

# movies (tr들) 의 반복문을 돌리기
'''for movie in movies:
    # movie 안에 a 가 있으면,
    a_tag = movie.select_one('td.title > div > a')
    if a_tag is not None:
        rank = movie.select_one('td:nth-child(1) > img')['alt'] # img 태그의 alt 속성값을 가져오기
        title = a_tag.text                                      # a 태그 사이의 텍스트를 가져오기
        star = movie.select_one('td.point').text                # td 태그 사이의 텍스트를 가져오기

        doc = {'rank': rank, 'title': title, 'star':star}
        #db.movies.insert_one(doc)

        #print(rank,title,star)'''

#Q1 영화제목 '매트릭스'의 평점을 가져오기
matrix_rate = db.movies.find_one({'title':'매트릭스'})['star']
print('매트릭스평점: ', matrix_rate)

#Q2 '매트릭스'의 평점과 같은 평점의 영화 제목들을 가져오기
for i in db.movies.find({'star':matrix_rate}):
    print(i['title'])

#Q3 '매트릭스'의 평점과 같은 평점의 영화 제목들의 평점을 0으로 만들기
db.movies.update_many({'star':matrix_rate}, {'$set':{'star':0}})