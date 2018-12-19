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

print(my_numbers)


# my_numbers, real_numbers, bonus_number
# 1 등: my_numbers == real_numbers
# 2 등: real과 my가 5개 같고. my의 나머지하나가 보너스 넘버
# 3 등: real과 my가 5개 같은것
# 4 등: real과 my가 4개 같은것
# 5 등: real과 my가 3개 같은것
# 꽝

for expected_value in my_numbers():

for estimated_vale in real_numbers():

results =[]
if results: my_numbers == real_numbers
    print ('1st prize')
else:
    print ('failed')
