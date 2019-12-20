from flask import Flask, render_template, request
from decouple import config
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello"



token = config('TELEGRAM_BOT_TOKEN')
chat_id = config('CHAT_ID')

url = "https://api.telegram.org/bot"

@app.route('/write') #http 주소 /write에 요청
def write():
    return render_template('write.html') #write.html 내용이 불러와진다.


@app.route('/send')
def send():
    text = request.args.get('text')
    requests.get(f'{url}{token}/sendmessage?chat_id={chat_id}&text={text}') #데이터를 같이보내려면 ?를 사용
    return render_template('send.html')
if __name__==("__main__"):
    app.run(debug=True)
    
