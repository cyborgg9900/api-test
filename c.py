from fastapi import FastAPI, Depends, Header, HTTPException
import requests

API_KEYS = {
    "key1": "user1",
    "key2": "user2",
}

# API key verification
def verify_api_key(api_key: str = Header(None)):
    if api_key not in API_KEYS:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return API_KEYS[api_key]

# Proxy authentication function
def proxy_auth():
    username = 'lOGlV1CdZCkXVp1X'
    password = 'Nm07679Q209wellk_country-br_session-sgn34f3e_lifetime-0.02s'
    proxy = f'http://{username}:{password}@geo.iproyal.com:12321'
    proxies = {
        'http': proxy,
        'https': proxy,
    }
    return proxies

# Check function to make the external request with proxy
def check(number: str):
    proxies = proxy_auth()
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
        "Referer": "https://npanxxsource.com/",
        "Origin": "https://npanxxsource.com"
    }
    url = f'https://www.nalennd.com/api/wbi?qsc={number}'
    try:
        response = requests.get(url, headers=headers, proxies=proxies, timeout=5)
        return {"status": response.status_code, "response": response.text}
    except requests.RequestException as e:
        return {"status": "error", "message": str(e)}



app = FastAPI()

# Route to check the number with rate limiting and API key verification
@app.get("/check/{number}")
def check_number(number: str, user: str = Depends(verify_api_key)):
    result = check(number)
    return {"user": user, "result": result}