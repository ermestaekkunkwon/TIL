import requests

key = ''  # 환경변수로 옮기자!

date = [20190113, 20190106, 20181230, 20181223, 20181216, 20181209, 20181202, 20181125, 20181118, 20181111]
rank = []
for j in date:
    URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt={date[j]}&weekGb=0'
    data_set = requests.get(URL).json()['boxOfficeResult']['weeklyBoxOfficeList']
    
    
    
for i in range(10):
    ranks = {}
    
    ranks['제목'] = data_set[i]['movieNm']
    ranks['코드'] = data_set[i]['movieCd']
    ranks['누적관객수'] = data_set[i]['audiAcc']
    ranks['해당일'] = date[i]
    rank.append(ranks)
