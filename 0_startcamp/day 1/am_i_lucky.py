import requests
import random

url= 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837'

response = requests.get(url, verify=False)
lotto_data = response.json()

real_numbers = []

# for key in lotto_data:
#     if 'drwtNo' in key:
#         real_numbers.append(lotto_data[key])

for key, value in lotto_data.items():
    if 'drwtNo' in key:
        real_numbers.append(value)


real_numbers.sort()
real_numbers = set(real_numbers)
bonus_number = lotto_data['bnusNo']
print(real_numbers)



# real_numbers = [
#     lotto_data['drwtNo1'],
#     lotto_data['drwtNo2'],
#     lotto_data['drwtNo3'],
#     lotto_data['drwtNo4'],
#     lotto_data['drwtNo5'],
#     lotto_data['drwtNo6']
# ]
# print(response.text)

{
    "drwtNo1":2,
    "drwtNo2":25,
    "drwtNo3":28,
    "drwtNo4":30,
    "drwtNo5":33,
    "drwtNo6":45,
    "bnusNo":6,
}




numbers = list(range(1,46))

my_numbers = random.sample(numbers, 6)

my_numbers.sort()

my_numbers = set(my_numbers)

print(my_numbers)


# my_numbers, real_numbers, bonus_number
# 1 등: my_numbers == real_numbers
# 2 등: real과 my가 5개 같고. my의 나머지하나가 보너스 넘버
# 3 등: real과 my가 5개 같은것
# 4 등: real과 my가 4개 같은것
# 5 등: real과 my가 3개 같은것
# 꽝


count = 0 # 카운트를  제로부터 시작  ex) n=0
for my_number in my_numbers:
    for real_number in real_numbers:
        if my_number == real_number:
            count +=1

print (count)


match_count = len(my_numbers & real_numbers)
print(match_count)

if match_count == 6: # same meaning of if diff == 0:
    print('1등')
elif match_count == 5 and bonus_number in my_numbers:
    print('2등')
elif match_count == 5:
    print('3등')
elif match_count == 4:
    print('4등')
elif match_count == 3:
    print('5등')
else:
    print('꽝')

# my_numbers = [1, 2, 3, 4, 5, 6]
# real_numbers = [1, 2, 3, 4, 5, 6]

# bonus_number = 7

# str = 'ssafy'
# str()
# sum= -> sum, str 은 쓰지말고 total을 써라
# sum()



# for expected_value in my_numbers():

# for estimated_vale in real_numbers():

# results =[]
# if results: my_numbers == real_numbers
#     print ('1st prize')
# else:
#     print ('failed')

#shit