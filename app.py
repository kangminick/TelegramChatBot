from flask import Flask, render_template, request
from decouple import config #token, id 값과 같은 공개하면 안되는 정보를 가져오기 위해 사용. (.env 파일에 들어있다.)
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
    requests.get(f'{url}{token}/sendmessage?chat_id={chat_id}&text={text}') #데이터를 같이 보내려면 ?를 사용
    return render_template('send.html')

@app.route(f'/{token}', methods=["post"]) #post 방식만 접근가능, 내 token을 알아야만 접근가능
def telegram(): #telegram 함수 실행
    # chat_id = request.get_json[][][]
    # if text == "로또" :
    #     # text
    
    return "ok", 200 # ok라는 문자와 200 (제대로 성공했다고 응답)를 리턴해준다.

if __name__==("__main__"):
    app.run(debug=True)
    
#ngrok 은 로컬웹사이트를 다른사람이 접근 가능하게 해준다.