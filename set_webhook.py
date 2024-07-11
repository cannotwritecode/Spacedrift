import requests
from config import TELEGRAM_BOT_TOKEN

response = requests.get(f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/setWebhook?url=https://your_domain_or_IP/webhook')
print(response.json())