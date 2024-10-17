import httpx
import asyncio

# Proxy Configuration
PROXY_USERNAME = 'lOGlV1CdZCkXVp1X'
PROXY_PASSWORD = 'Nm07679Q209wellk'
PROXY_URL = f'http://{PROXY_USERNAME}:{PROXY_PASSWORD}@geo.iproyal.com:12321'

PROXIES = {
    'http://': PROXY_URL,
    'https://': PROXY_URL,
}

# Asynchronous Check Function
async def check(number):
    retries = 10
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
        "Referer": "https://npanxxsource.com/",
        "Origin": "https://npanxxsource.com"
    }
    url = f'https://www.nalennd.com/api/wbi?qsc={number}'

    async with httpx.AsyncClient(proxies=PROXIES, timeout=10) as client:
        for _ in range(retries):
            try:
                response = await client.get(url, headers=headers)
                if response.status_code == 200:
                    print(f"{number}: Success")
                    return
                elif response.status_code == 429:
                    # print(f"{number}: Rate limited. Retrying...")
                    await asyncio.sleep(0.3)
                elif response.status_code == 404:
                    print(f"{number}: Invalid")
                    return
                else:
                    print(f"{number}: Unexpected status {response.status_code}")
                    return
            except httpx.RequestError as e:
                print(f"{number}: Error - {str(e)}")
                return
        print(f"{number}: Not found")

# Main async function to run checks for all numbers
async def main():
    with open('p.txt') as f:
        numbers = [number.strip() for number in f.readlines()]
    
    tasks = [check(number) for number in numbers]
    await asyncio.gather(*tasks)

# Run the async main function
if __name__ == "__main__":
    asyncio.run(main())