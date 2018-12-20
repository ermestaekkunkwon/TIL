import requests
import random

def pick_lotto():
    numbers = random.sample(range(1,46), 6)
    return numbers

my_numbers = pick_lotto()
print(my_numbers)


def get_lotto(num): # -> 다만 이것으로는 837회 밖에 조회를 못함
    lotto_data = requests.get('https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=' + num, verify=False).json()
    numbers = []
    for key, value in lotto_data.items():
        if 'drwtNo' in key:
            numbers.append(value)
    
    numbers.sort()
    bonus_number = lotto_data['bnusNo']

    return {'real_numbers' : numbers, 'bonus_numbers' : bonus_number } # final_dict { 'numbers' : numbers, 'bonus' : bonus_number} -> return final_dict

real_numbers = get_lotto()
print (real_numbers)


def am_i_lucky ():
    count = 0
    for my_number in my_numbers:
        for real_number in real_numbers:
            if my_number == real_number:
                count +=1

    match_count = len(my_numbers & real_numbers)
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

    return match_count

result = am_i_lucky()
print(result)



# count = 0 # 카운트를  제로부터 시작  ex) n=0
# for my_number in my_numbers:
#     for real_number in real_numbers:
#         if my_number == real_number:
#             count +=1

# print (count)


# match_count = len(my_numbers & real_numbers)
# print(match_count)

# if match_count == 6: # same meaning of if diff == 0:
#     print('1등')
# elif match_count == 5 and bonus_number in my_numbers:
#     print('2등')
# elif match_count == 5:
#     print('3등')
# elif match_count == 4:
#     print('4등')
# elif match_count == 3:
#     print('5등')
# else:
#     print('꽝')

# # my_numbers = [1, 2, 3, 4, 5, 6]
# # real_numbers = [1, 2, 3, 4, 5, 6]

# # bonus_number = 7

# # str = 'ssafy'
# # str()
# # sum= -> sum, str 은 쓰지말고 total을 써라
# # sum()



# # for expected_value in my_numbers():

# # for estimated_vale in real_numbers():

# # results =[]
# # if results: my_numbers == real_numbers
# #     print ('1st prize')
# # else:
# #     print ('failed')

# #shit