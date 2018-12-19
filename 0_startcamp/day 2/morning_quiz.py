# from statistics import mean


# # def Average(your_score): 
# #     return mean(your_score)

# #     print ('your_average')


# 1. 평균을 구하시오
my_score = [79, 84, 66, 93]
# my_average = mean(my_score)
my_average = sum(my_score) / len(my_score)
print(my_average)

# # def Average(my_score): 
# #     return mean(my_score)

# #     print (my_average)


your_score = {
    '수학': 87,
    '국어': 83,
    '영어': 76,
    '도덕': 100
}



your_average = sum(your_score.values()) / len(your_score)
print (your_average)
# # your_average = Average (your_score) # float

your_total = sum(your_score.values())
your_average = your_total / len (your_score)
print (your_average)


cities_temp = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -5, 10],
    '구미': [2, -2, 9]
}

# # 3 : 도시별 온도 평균
# # 서울 :?
# # 대전 :?
# # 광주: ?
# # 구미 : ?

# for key, value in cities.items():
#     print (key, round(sum(cities (value))/len (cities(value)), 2))


# for city, temperatures in cities_temp.items():
#     print (city + ': ' + ((sum(temperatures)) / len (temperatures)))

for city in cities_temp: # 왼손으로 키만 꺼낸다
    temperatures = cities_temp[city]
    avg_temperature = round(sum(temperatures) / len(temperatures), 2)
    print(city, avg_temperature)
    print(city + ': ' + str(avg_temperature))
    print ('{}: {}'. format(city, avg_temperature))
  


for key, value in cities_temp.items(): # 양손으로 둘다 꺼내요
    avg_temperature = round(sum(value)/len(value),2)
    print (key, avg_temperature)
    print(key + ': ' + str(avg_temperature))


# temperature_seoul = round(sum (cities ['서울']) / len (cities['서울']), 2)
# print ('서울:', temperature_seoul)

# temperature_daeseon = round(sum (cities ['대전']) / len (cities['대전']), 2)
# print ('대전:', temperature_daeseon)

# temperature_gwangju = round(sum (cities ['광주']) / len (cities['광주']), 2)
# print ('광주:', temperature_gwangju)

# temperature_koomi = round(sum (cities ['구미']) / len (cities['구미']), 2)
# print ('구미:',temperature_koomi)

# max_s = max(cities['서울'])
# print (max_s)

# # 4: 도시중에 최근 3일간 가장 추웠던 곳, 가장 더웠던 곳,
# # hottest :??, coldest :??

# all_temp 모든 기온을 모은다
all_temp = []
for key, value in cities_temp.items():
    all_temp += value

print(all_temp)
# all_temp 에서 highest/lowest를 찾는다

highest = max(all_temp)
lowest = min(all_temp)
print (highest, lowest)

# cities_temp에서 highest/lowest가 속한 도시를 찾는다.

for key, value in cities_temp.items():
    if highest in value:
        print('도시 중 가장 더운', key, max(value))
    if lowest in value:
        print('소지 중 가장 추운', key, min(value))


hottest = []
coldest = []
for key, value in cities_temp.items():
    if highest in value:
        hottest.append(key)

    if lowest in value:
        coldest.append(key)

print (hottest, coldest)

# # for key, value in cities.items() :
# #     print (key, value)

# # max(zip(cities.values(), cities.keys()))

# cities_value = cities.values()
# cities_key = cities.keys()
# list_value = list(cities)
# list_key = list(cities)

# max_S = [max(cities['서울'])] 
# max_D = [max(cities['대전'])]
# max_G = [max(cities['광주'])]
# max_K = [max(cities['구미'])]

# for i in cities:
#     max_all.append[i]

# max_all = max_S+max_D+max_G+max_K
# max = max(max_all)
# print ("도시:" ,max)

# min_S = [min(cities['서울'])] 
# min_D = [min(cities['대전'])]
# min_G = [min(cities['광주'])]
# min_K = [min(cities['구미'])]

# min_all = min_S+min_D+min_G+min_K
# min = min(min_all)
# print ("도시:" ,min)


# # for i, va in cities
# #     if max

# # hottest = max(cities.values())
# # print (hottest)
# # coldest = min(cities.values())
# # print (coldest)

# git add .
# git commit -m asdasdf
# git push