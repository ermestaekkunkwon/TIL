# 'http:// ide.c9.io / eduyu/startcamp'
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