# TelegramChatBot
Telegram ChatBot project
## 텔레그램 챗봇 만들기

1. 텔레그램 설치

   http://www.telegram.pe.kr/

2. 텔레그램에서 @BotFather 과 대화하기

- 챗봇 이름을 두번에 걸쳐 전송
- 두번째 챗봇 이름 전송시에는 끝이 bot으로 끝나도록 하기
- 챗봇 생성 완료 (@<챗봇이름>하면 검색할 수 있다)
- 토큰 복사하기

1. request 요청하는 방법

https://core.telegram.org/bots/api

상기의 사이트를 참고하여 다음과 같은 url로 request 한다.

form : `https://api.telegram.org/bot/METHOD_NAME`

- getme: 봇 정보 가져오기

```
https://api.telegram.org/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/getMe
```

- getupdates: 업데이트 상태 보여주기

```
https://api.telegram.org/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/getupdates
```

- sendMessage:메세지 보내기

```
https://api.telegram.org/bot<토큰>/sendMessage?chat_id=<보낼 chat_id번호>&text=<메세지>

##아이디 번호를 알고싶다면 bot에게 메세지를 보내고 getupdates로 chat_id를 확인해보자 
```

- 기타 메소드를 알고싶다면 telegram api사이트를 참고

1. app.py 와 html 작성하기

- 유의사항: token과 chat_id는 개인정보로 github등 공개된 공간에 오픈하지 않는것이 좋다
  - 따라서 python- decouple을 이용하여 개인정보는 숨겨놓기

```
$ pip install python-decouple
```

- .env파일을 만들어 개인 정보 입력하기

```
$touch .env
```

- python 파일에서 import 하고 사용하기

```
from decouple import config
```

1. webhook 이용하기
   - https://ngrok.com/ 에서 다운로드

- ngrok: 외부에서 로컬의 서버에 접속할 수 있도록 하여 내부 flask에 접속할 수 있도록 하는 프로그램
  - window 프롬프트에서 다음 명령어 실행

```
ngrok http 5000
```

`https://로 시작하는 주소`/플라스크 라우트 주소 입력하면 플라스크로 만든 페이지로 이동할 수 있다.

- set Webhook: 로컬의 서버(Flask서버)를 텔레그램 서버와 연동해주는 매소드
  - webhook.py참고

```
https://api.telegram.org/bot{token}/setwebhook?url={웹훅주소}/{토큰}
```
