from flask import Flask

app = Flask(__name__)

@app.route('/dictionary/<string:word>')
def dictionary(word):
    a = {
        'apple' : '사과',
        'banana' : '바나나',
        'melone' : '멜론'
    }
    if word in a:
        return(f' {word}은(는) {a[word]}!')
    else:
        return(f' {word}은(는) 나만의 단어장에 없는 단어입니다!')

print(dictionary('apple'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)