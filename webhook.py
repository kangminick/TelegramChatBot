import requests
from decouple import config

token = config("TELEGRAM_BOT_TOKEN")
url = "https://api.telegram.org/bot"
ngrok_url = "https://142dbcb3.ngrok.io"

data = requests.get(f'{url}{token}/setwebhook?url={ngrok_url}/{token}') #기존 주소 + webhook 주소
print(data)