import requests
import random

def pick_lotto():
    numbers = random.sample(range(1,46), 6)
    return numbers

my_numbers = pick_lotto()
print(my_numbers)


def get_lotto(draw_no): # -> 다만 이것으로는 837회 밖에 조회를 못함 get_lotto(num=???) -> 값이 계속 들어온다 # 빈칸에는 아무것도 요구사항없이 결과를 내었으나, 이제는 뭔가를 주어야 결과를 냄.
    lotto_data = requests.get('https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=' + str(draw_no)).json()
    numbers = []
    for key, value in lotto_data.items():
        if 'drwtNo' in key:
            numbers.append(value)
    
    numbers.sort()
    bonus_number = lotto_data['bnusNo']

    return {'real_numbers' : numbers, 'bonus_numbers' : bonus_number } # final_dict { 'numbers' : numbers, 'bonus' : bonus_number} -> return final_dict

real_numbers = get_lotto(837) # 가로안의 1은 인자. arguments. args
print (real_numbers)



def am_i_lucky(pick, draw):
    match = set (pick) & set (draw['real_numbers'])   
    if len (match) == 6 :
        return ('1등') #!!! -> 함수에는 print 안쓰는 것이 좋다.
    elif len (match) == 5 and draw['bonus_numbers'] in pick:    # 이미 list_1을 pick이라고 해서 pick이라고 쓰고, 함수 밖에서는  draw['bonus] in list_1
        return ('3등')
    elif len (match) == 4:
        return ('4등')
    elif len (match) == 3:
        return ('5등')
    else:
        return ('꽝')

result = am_i_lucky(pick_lotto(), get_lotto(837))
print(result)










# # str = 'ssafy'
# # str()
# # sum= -> sum, str 은 쓰지말고 total을 써라
# # sum()



# 예제 풀이!!

# 1단계 정답

# def am_i_lucky(pick, draw):
#     match = set (pick) & set (draw)
#     if len (match) == 6 :
#         return ('1등') #!!! -> 함수에는 print 안쓰는 것이 좋다.
#     elif len (match) == 5:
#         return ('3등')
#     elif len (match) == 4:
#         return ('4등')
#     elif len (match) == 3:
#         return ('5등')
#     else:
#         return ('꽝')

# print(am_i_lucky([1, 2, 3], [1, 2, 4]))

# 앞의 것이 string이면 뒤의 것도 string

print (int(True))


# 2단계 정답!



# am_i_lucky(list_1, dict_1)

# def am_i_lucky(pick, draw):
#     match = set (pick) & set (draw['numbers'])   
#     if len (match) == 6 :
#         return ('1등') #!!! -> 함수에는 print 안쓰는 것이 좋다.
#     elif len (match) == 5 and draw['bonus'] in pick:    # 이미 list_1을 pick이라고 해서 pick이라고 쓰고, 함수 밖에서는  draw['bonus] in list_1
#         return ('3등')
#     elif len (match) == 4:
#         return ('4등')
#     elif len (match) == 3:
#         return ('5등')
#     else:
#         return ('꽝')

# list_1 = [1, 2, 3, 4, 5, 6]
# dict_1 = {
#     'numbers' : [1, 2, 3, 4, 5, 7],
#     'bonus' : 6
# }


# !! dict_1['numbers'] #!! -> 딕셔너리에서 추출하는 법!!! 키를 통해 밸류를 추출