import json

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def home():
    data = request.json.get('string') # 데이터 받아오기 (body값)
    print(data) # 출력 잘 되는지 확인

    # -- 필터링 로직 --

    #  @#$%^&*&^%$#@$%^&

    # -- 필터링 로직 --


    # 필터링된 데이터
    response = {

        "terSfr": "",

        "terSto": "철원",

        "date": "",

        "time": "",

        "arrTime": ""

    }
    return jsonify({"response": response})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)
