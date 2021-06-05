import requests

try:
    requests.get("https://core.telegram.org/api/obtaining_api_id", timeout=3)
    print(1)
except requests.ConnectionError:
    print(0)
