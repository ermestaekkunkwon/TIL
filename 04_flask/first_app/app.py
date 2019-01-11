import random

from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/')
def root():
    return 'Hi'

@app.route('/ssafy')
def ssafy():
    return 'sssaffy'

@app.route('/hi/<string:name>')
def hi(name):
    return(f'hi {name}!')


@app.route('/pick_lotto')
def pick_lotto():
    numbers = random.sample(range(1, 45 +1), 6)
    return jsonify(numbers)


# @app.route('/keyword/<string:word>')
# def keyword(word):
#     search_results = DB.find(word)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


a = 1
