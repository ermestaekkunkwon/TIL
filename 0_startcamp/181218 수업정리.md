# 181218 수업정리

## 1. 개발환경 설정

* chocolatey
  * 윈도우 패키지 매니저
* python -v 3.6.7
* git
  * Version Control System
* vscode
  * Code Editor
* chrome
  * Browser

## 2. python list

### list creation

```python
mcu = [
    ['ironman', 'captain america', 'thor', 'hulk'],
    ['x-men', 'deadpool', 'fantastic four'],
    ['spider-man']
]
disney = mcu[0]
fox = mcu[1]
sony = mcu[2]
mcu [0] [2]
```

이때 `원하는 히어로`에 접근하려면 어떻게 해야할까?



리스트 안에 리스트가 있다



### list 추출하기

1. `[0]` 처럼 인덱스 접근하기
2. `[1:10]` 처럼 잘라내기



### list 연산

```python
team = [
    'john',
    10000,
    'neo',
    100,
    'tak',
    40500
]

team[2:4]

new_member = ['js', 10]

team = team + new_member #리스트와 리스트끼리 연산 가능 -> 그냥 합쳐진다.
team += new_member

n=0
n= n+1
n += 1 # 서로 같은 의미. 윗줄과. 무조건 equal sign은 뒤에다 붙음
```





## 3. dict

### dict 예시

```python
my_info = {
    'name':'neo', 
    'job':'hacker',
    'mobile': '01053596596',
    'email': 'excelsior@gmail.com'
}

my_info[email]

hphk = [
    {
    'name': 'john',
    'email': 'john@hphk.io'
},

{
    'name': 'neo',
    'email': 'neo@hphk.io'
},

{
    'name': 'tak',
    'email': 'tak@hphk.io',
    'married': False
}
]

type(hphk) # list
hphk[]


p = hphk[2]
print(type(p)) # dic

print(p['name'])

# p['name'] = hphk[2]['name']
```



`key, value` 가 정말 중요하다.





## 4. Function

```python
print ('hi')
len ('hi') #2
len ([1,2,3,4,5]) # 5
del()
type('a')

scores = [45, 60, 78, 88]
high_score = max(scores)
lowest_score = min(scores)
round (1.8) # 2
round (1.876, 2)

min (1,2,3) # 이것도 가능, 굳이 리스트만 할 필요 없다

first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

#  full 에 first 와 second 를 합쳐서 저장

full = first + second

# full_sorted 에 full을 오름차순으로 정렬해서 저장


full_sorted = sorted(full)

# *reverse_sorted에 full을 내림차순으로 정렬해서 저장.


reverse_sorted = sorted(full, reverse=True)
```

| str      | int   | list               | bool    |
| -------- | ----- | ------------------ | ------- |
| `python` | `100` | `['a', '3', True]` | `False` |



위에는 class, 아래는 object

## 5. Method

메서드는 함수다! 다만 [주어], [동사] 의 형식으로 이루어지며, [주어] 자리에 오는 object 들이 할 수 있는 행동 (함수)들이다.

```python
my_list = [4, 7, 9, 1, 3, 6]
#최댓값/최소
max(my_list)
min(my_list)
# 특정 요소의 인덱스??
my_list.index()
# 리스트를 뒤집으려면?/
my_list.reverse()

# . 뒤에 붙으면 메소드



dust = 100 # <class: int>
lang = 'python' # str
samsung = ['electornic', 'sds', 'insurance'] #list

lang.capitalize()
lang.replace('on', 'off')

# -> 이경우 안바꿈

samsung.index('sds')

samsung.append('bio') #원본 파괴
```





