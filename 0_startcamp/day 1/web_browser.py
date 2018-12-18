import webbrowser # import는 거의 무조건 앞에

keywords = [
    'wolverine',
    'captain america',
    'magneto',
    'juggernaut'
]

for keyword in keywords:
    url = 'https://www.google.com/search?q=' + keyword
    webbrowser.open_new(url)


# 조회수 조작은 while (true): 추가시켜라