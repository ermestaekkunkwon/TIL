import requests
import os

  # 환경변수로 옮기자!
kobiskey = os.getenv('')

date = ['20190113', '20190106', '20181230', '20181223', '20181216', '20181209', '20181202', '20181125', '20181118', '20181111']
rank = []
for j in date:
    URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={kobiskey}&targetDt={j}&weekGb=0'
    data_set = requests.get(URL).json()['boxOfficeResult']['weeklyBoxOfficeList']
    for i in range(10):
        ranks = [data_set[i]['movieNm'], data_set[i]['movieCd'], data_set[i]['audiAcc'], date[i]]
        for k in range(len(rank)):
            if ranks[0] == rank[k][0]:
                break
        else:
            rank.append(ranks)

print(rank)

import csv

f_w = open('ss3.csv', 'a+', encoding='utf-8', newline='')
         
writer = csv.writer(f_w)

for movie_info in rank:
    writer.writerow(movie_info)

f_w.close()