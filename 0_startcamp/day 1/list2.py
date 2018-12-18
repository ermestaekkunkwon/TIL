team = [
    'john',
    10000,
    'neo',
    100,
    'tak',
    40500
]

team[2:4]
# len (team) ==6
new_member = ['js', 10]

team = team + new_member #리스트와 리스트끼리 연산 가능 -> 그냥 합쳐진다.
team += new_member
# len(team) == 8
n=0
n= n+1
n += 1 # 서로 같은 의미. 윗줄과. 무조건 equal sign은 뒤에다 붙음

del (team[2]) # 동시에 지우고 싶을 땐 [] 이용해라
# len (team) == 6


del(team[2:4])
# len (team) == 4