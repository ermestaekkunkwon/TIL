1. # 'http:// ide.c9.io / eduyu/startcamp'
          # domain   #route

# _*_ coding: utf-8 _*_



from flask import Flask, jsonify, render_template, request
import random # from random import sample
import requests
from bs4 import BeautifulSoup



app = Flask(__name__)

@app.route('/ide/<string:username>/<string:workspace>') # variable route -> 변수로 걸어둔다 (<>로 되있으면 전부 변수 처리)
def username_workspace(username, workspace):
    # return "{}'s hot {}!" .format(username, workspace)
    return render_template('ide.html', name = username, space = workspace)


@app.route("/")
def index():
    lunch = random.choice(['20층', 'Diet'])
    return render_template('index.html', lunch=lunch)
    
@app.route("/hi")
def hi():
    return 'Hello SSAFY'
    
    
# @app.route("/get_lotto/<int:draw_no>")
# def get_lotto():
#     data = {
#         'numbers' : [1, 2, 3, 4, 5, 6],
#         'bonus' : 7
#     }
#     return jsonify(data)

@app.route("/login")
def login():
    return render_template('input.html')

@app.route("/get_lotto/<int:draw_no>")

def get_lotto_draw_no(draw_no): # -> 다만 이것으로는 837회 밖에 조회를 못함 get_lotto(num=???) -> 값이 계속 들어온다 # 빈칸에는 아무것도 요구사항없이 결과를 내었으나, 이제는 뭔가를 주어야 결과를 냄.
    lotto_data = requests.get('https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=' + str(draw_no)).json()
    numbers = []
    for key, value in lotto_data.items():
        if 'drwtNo' in key:
            numbers.append(value)
    
    numbers.sort()
    bonus_number = lotto_data['bnusNo']

    data = jsonify({'real_numbers' : numbers, 'bonus_numbers' : bonus_number }) # final_dict { 'numbers' : numbers, 'bonus' : bonus_number} -> return final_dict
    return data
    
    

    
@app.route("/selection")
def selection():
    return render_template('selection.html')

@app.route("/manual")
def manual():
    return render_template('manual_selection.html')

@app.route("/automatic")
def automatic():
    return jsonify(random.sample(range(1,46), 6))

@app.route("/lotto_result")
def lotto_result():
    DrawNo = request.args.get('drawno')
    Number1 = request.args.get('Lottery_Number1')
    Number2 = request.args.get('Lottery_Number2')
    Number3 = request.args.get('Lottery_Number3')
    Number4 = request.args.get('Lottery_Number4')
    Number5 = request.args.get('Lottery_Number5')
    Number6 = request.args.get('Lottery_Number6')
    my_numbers = [Number1, Number2, Number3, Number4, Number5, Number6]

    lotto_data = requests.get('https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=' + str(drawno)).json()
    numbers = []
    for key, value in lotto_data.items():
        if 'drwtNo' in key:
            numbers.append(value)
    
    real_numbers.sort()
    real_numbers = set(real_numbers)
    bonus_number = lotto_data['bnusNo']
    
    return render_template('manual_result.html', your_number=my_numbers, real_number=numbers)

@app.route("/am_i_lucky")
def am_i_lucky():
    
    lotto_data = requests.get('https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837', verify=False).json()

    real_numbers = []
    for key, value in lotto_data.items():
            if 'drwtNo' in key:
                real_numbers.append(value)

    real_numbers.sort()
    real_numbers = set(real_numbers)
    bonus_number = lotto_data['bnusNo']



    my_numbers = random.sample(list(range(1,46)), 6)
    my_numbers.sort()
    my_numbers = set(my_numbers)
    


    count = 0 # 카운트를  제로부터 시작  ex) n=0
    for my_number in my_numbers:
            for real_number in real_numbers:
                 if my_number == real_number:
                    count +=1

    match_count = jsonify("당신의 등수는", len(my_numbers & real_numbers))

    if match_count == 6:
        return('축하합니다! 1등입니다!')
    elif match_count == 5 and bonus_number in my_numbers:
        return('뭐, 운이 좋으시군요! 2등입니다.')
    elif match_count == 5:
        return('더 나은 날이 오겠죠! 3등입니다.')
    elif match_count == 4:
        return('행복한 미래가 기다립니다! 4등입니다.')
    elif match_count == 3:
        return('Fifth rank is better than the worst. 5등입니다.')
    else:
        return('그냥 포기하세요. 꽝입니다.')
        
    return match_count


@app.route('/kospi')
def kospi():

    kospi = BeautifulSoup(requests.get('https://finance.naver.com/sise/').text, 'html.parser').select_one('#KOSPI_now').text
    return kospi



@app.route('/president')
def president():
    from random import choice
    row = ['a','b','d','e','g','h']
    col = list(range(2, 7))

    coord = [choice(row), choice(col)]
    return jsonify(coord)
    
@app.route("/ping")
def ping():
    return render_template('ping.html')

@app.route("/pong")
def pong():
    phone = request.args.get('phone_number')
    color = request.args.get('color')
    
    return render_template('pong.html', mobile_number=phone, color=color)




# python3 app.py

# @app.route("/send_message")
# def send_message():
#     telgram.send('msg')
#     return telgram




#1
    # (master) $ export FLASK_ENV='development'
    # flask run -h 0.0.0.0 -p 8080 잊지말자
    
#2 # if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8080)
# python3 app.py

# 1번과 2번이 똑같은 효과를 가져옴




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)


    2. 궁합 챗봇/ 서버

    전반적인 상황!

Dear Proffesor

안녕하십니까
생도 권택건이라고 합니다.

수업을 하실 때는 개념이 이해가 되지만, 직접 제가 작성해나갈 시기에는 제가 아무것도 만들지 못하는 상황이 발생합니다.
이를 통해, 제가 수업에 대한 이해가 아주 부족한건지. 혹은 경험 미달로 인한, 미숙함인지 아직은 판가름할 수 없으나 재능이 없다는 것은 익히 알 수 있습니다.

또한, 간략화를 통해, 순서에 맞는 짜임새를 구상해볼 수 있으나 제 머리속에 있는 이 개념을 코딩으로서 구현화시키는 것이 제일 어렵습니다.
무엇보다도, indentation error, definition 에러 등 제가 디버깅할 때 어떤식으로 해야할지 참으로 난해하더군요.
더군다나 html까지 완벽히 모르는 상황에서 오늘 구현을 하는 통에, 로또를 완성해낼 수 없었습니다.
이런 제가 크롤링을 시도하려고했다는 점에서 어리석었다는 것을 증명해내었고. 이를 개선하여 좀 더 이해를 높이는 것이 올 12월의 목표입니다.

마지막으로 제가 로또 챗봇 을 완성하려고했으나 자체도 불가능하였기에 제가 하고자했던 일을 말씀드리고자합니다.
우선, 로그인 화면을 통해서 자신을 증명하고자 하는 것이 첫 걸음이었습니다.
두번째, 자동 그리고 수동으로 자신의 번호를 정해서 실제 회차수들의 번호를 구현화하고자했으나
837번째 로또번호만 가져올 수 있었던 저의 미숙함에 시간을 버렸습니다. 특히 이 과정에서 오류만 떠서 결국 이과정은 미완성으로 남았습니다.

세번째, 자동완성은 과거의 기록으로 어느정도 가져올 수 있었으나, 좀 더 보기좋게 ... 예를들면

"xxxx회차" n1, n2, n3, n4, n5, n6 가 선택되었습니다. (혹은 보너스넘버도)
"xxx 님의 번호는" a1, a2, a3, a4, a5, a6 이며

최종적으로 귀하는 xx등 하셨습니다.

-> 여기서 등수에 따라 다르게 멘트들이 나오는... (가령 면접합격자에게는 축하드립니다. 탈락자에게는 안타깝습니다. 이런식으로 나오듯이) 구현화하는 것이 제 최종목표였고

마지막으로 이를 제 챗봇에 받고 싶었으나, 챗봇도 작동이 안하는 기적에 우선 미완성으로 제출합니다.
다행히도 제 힘으로 타노스와의 마수를 이겨낼 수 있는 앱을 구현화한 것 부터가 5일간의 가르침으로 이정도 성장할 수 있었다는 안도감을 얻게되었고, 좀 더 열심히 할 기회를 얻고자 제가 원하는 코드를 작성할 수 있는 기회를 얻고싶습니다.
이렇게 평가가 올 줄은 꿈에도 몰랐으나, 어느정도 아슬아슬하게 합격점을 받아 1월부터 프로그래밍의 새로운 세계로 나아가고자하는 것이 저의 꿈입니다.
5일간의 가르침은 정말 의미깊은 시간이었고 좀 더 나아지는 모습을 보여준다고 확신할 수는 없지만 더욱 노력하겠습니다.

감사합니다.

3반 A-2 권택건 올림.

요약

1. 개념은 알겠는데 만들지를 못함.
2. 제일 중요한 디버깅에 대한 공포가 큼.
3. 열심히하고자해도 현실은 가혹함
4. 미완성이나 어떻게든 간단한 것은 완성.
5. 열심히 하겠습니다.





1. 궁합 챗봇 / 서버
이름: 권택건 (교수님과 같이 만들었지만...)

## 하는 일
자신이 좋아하는 연인, 혹은 연예인과 궁합이 어느정도 되는지 알아보는 앱입니다.

## 어려웠던 점
처음부터 만들기 어려웠습니다.
일단 수업을 따라갈 수는 있으나 그것을 직접 시도해보는 것은 너무나도 힘든 일이었고, 생문과였던 제가 5일만에 어느정도 따라잡지못하는 참회감도 들어갔습니다.

## 작동
사용자가 /ping으로 요청을 보내면
이를 입력받을  html로 보낸다
사용자가 이름을 입력하면
/pong에서 입력받은 이름을 telegram 메시지로 보냅니다.
사용자에게 궁합 점수를 보냅니다.

##보완하고자 하는 점.
우선, 추천하는 기능을 추가하고싶습니다.
모든 연예인을 추가할 수는 없겠지만..
미국사이트에서 연예인들의 사진, 프로필을 모아놓은 사이트들이 많은 만큼 이를 크롤링해서 좀 더 다채롭게 시작하고자하는 것이 제 욕심입니다.



2. 타노스 챗봇 / 서버
이름 : 권택건

## 하는 일
타노스가 쳐들어와서 죽여나갈 때, 자신은 살아남을까 ,죽을까 알아보는 앱입니다.

## 어려웠던 점.
현재, 제 실력으로는 도무지 어려운 맵을 만들어낼 수가 없기에, 우선 가장 유명했던 앱을 기반으로 만들었습니다.
한~두 줄의 간단한 코드라서 그런지, 아주 어려운 점은 없었으나... 나름 그래도 노력할 수 있었던 보람이 있었습니다.
다만, 제가 알아보고자하는 모든 친구, 가족들도 같이 추가시켜서 다들 어찌되는지 알아보고 싶었던 점이 아쉽습니다.

## 작동
사용자가 /ping으로 요청을 보내면
이를 입력받을  html로 보낸다
사용자가 이름을 입력하면
/pong에서 입력받은 이름을 telegram 메시지로 보냅니다.
사용자에게 죽었는지 살았는지의 여부를 보냅니다.


3. 로또 챗봇 / 서버 -> 실패해서 url 일단 삭제상태.
이름 : 권택건

## 하는 일
자신의 로또 번호를 입력하고 배정받아 자신이 얼마나 운이 좋은지 알아가는 앱입니다.

## 어려웠던 점.
우선, 전반적으로 html과 연관시키는 것이 어려웠습니다. 무엇보다도, 2단계까진 성공했으나
3단계부터 구현화할 수 없었던 점이 제일 무력하다고 느꼈었고 또한 챗봇도 실패하여 타노스문자만 주구장창 받고있습니다.
하지만, 자동번호만은 어찌 구현화해서 (not 문자) 이렇게라도 중간과정을 보고합니다.


## 작동
실패해서 작성불가