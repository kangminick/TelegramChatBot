import requests
from decouple import config

token = config("TELEGRAM_BOT_TOKEN")
url = "https://api.telegram.org/bot"
paw_url = "https://kangminick.pythonanywhere.com/"


data = requests.get(f'{url}{token}/setwebhook?url={paw_url}{token}') #기존 주소 + webhook 주소
print(data)
#주소가 변경될때만 웹훅 변경.
