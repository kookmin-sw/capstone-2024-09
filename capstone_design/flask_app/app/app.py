# hello world를 출력하는 앱
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/users')
def users():
	# users 데이터를 Json 형식으로 반환한다
    return {"members": ["M1", "M2", "M3"]}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)