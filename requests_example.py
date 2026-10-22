import requests

response = requests.get("https://api.github.com")

print("Код відповіді сервера:", response.status_code)