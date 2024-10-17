from fastapi import FastAPI
import requests

app = FastAPI()

def proxy_auth():
    username = 'lOGlV1CdZCkXVp1X'
    password = 'Nm07679Q209wellk_country-br_session-sgn34f3e_lifetime-0.02s'
    proxy = f'http://{username}:{password}@geo.iproyal.com:12321'
    proxies = {
        'http': proxy,
        'https': proxy,
    }
    return proxies

def check(number: str):
    proxies = proxy_auth()
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
        "Referer": "https://npanxxsource.com/",
        "Origin": "https://npanxxsource.com"
    }
    url = f'https://www.nalennd.com/bi?qsc={number}'
    try:
        response = requests.get(url, headers=headers, proxies=proxies, timeout=5)
        return {"status": response.status_code, "response": response.text}
    except requests.RequestException as e:
        return {"status": "error", "message": str(e)}


@app.get("/check/{number}")
def check_number(number: str):
    result = check(number)
    return result


