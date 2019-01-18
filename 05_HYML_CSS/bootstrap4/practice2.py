import requests
import os

kobiskey = os.getenv('')


code = ['20184105', '20176251', '20189463', '20180290', '20183915', '20185485', '20184574', '20186281', '20170658', '20175547', '20183785', '20184187', '20182421', '20168773', '20183479', '20183238', '20177552', '20179230', '20183375', '20189843', '20182082', '20178825', '20183745', '20177538', '20184481', '20181905', '20176814', '20183073', '20181171', '20183007', '20182966', '20183050', '20182935', '20182669', '20186822', '20170513', '20189869', '20174981', '20010291', '20179006', '20181404', '20180523', '20182693']
rank = []
for j in code:
    URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={kobiskey}&movieCd={j}'
    data_set = requests.get(URL).json()['movieInfoResult']['movieInfo']
    for i in range(43):
        ranks = [data_set[i]['movieCd'], data_set[i]['movieNm'], data_set[i]['movieNmEn'], data_set[i]['movieNmOg'], data_set[i]['prdtYear'], data_set[i]['showTm'], data_set[i]['genres'][0], data_set[i]['directors'], data_set[i]['audits'][1], data_set[i]['actors'][0:3]]
    rank.append(ranks)

print(rank)