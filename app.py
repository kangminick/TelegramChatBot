from flask import Flask, render_template, request
from decouple import config #token, id 값과 같은 공개하면 안되는 정보를 가져오기 위해 사용. (.env 파일에 들어있다.)
import requests
import random
import json #카카오 번역의 api를 이용하기위해

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello"

token = config('TELEGRAM_BOT_TOKEN')
chat_id = config('CHAT_ID')
url = "https://api.telegram.org/bot"
KAKAO_KEY = config("KAKAO")
@app.route('/write') #http 주소 /write에 요청
def write():
    return render_template('write.html') #write.html 내용이 불러와진다.


@app.route('/send')
def send():
    text = request.args.get('text')
    requests.get(f'{url}{token}/sendmessage?chat_id={chat_id}&text={text}') #telegram으로 정보 전송
    return render_template('send.html')

@app.route(f'/{token}', methods=["post"]) #post 방식만 접근가능, 내 token을 알아야만 접근가능
def telegram(): #telegram 함수 실행
        
    data = request.get_json() # 챗봇에 입력한 데이터의 json
    text = (data['message']['text'])
    chat_id = (data['message']['chat']['id'])
    if text == "안녕" :
        return_text = "안녕하세요"
    elif text == "로또":
        numbers = range(1,46)
        return_text = sorted(random.sample(numbers, 6))
    else : 
        headers = {
            "Host": "kapi.kakao.com",
            "Authorization": f"KakaoAK {KAKAO_KEY}"
            
        }
        query= text
        response=requests.get(f'https://kapi.kakao.com/v1/translation/translate?src_lang=kr&target_lang=en&query={query}',headers=headers)
        response_text=response.json()['translated_text'][0][0]
        return_text = response_text
    requests.get(f'{url}{token}/sendmessage?chat_id={chat_id}&text={return_text}') #telegram에서 답장
    return "ok", 200 # ok라는 문자와 200 (제대로 성공했다고 응답)를 리턴해준다.

if __name__==("__main__"):
    app.run(debug=True)
    
#ngrok 은 로컬웹사이트를 다른사람이 접근 가능하게 해준다.