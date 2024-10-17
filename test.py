import requests
with open('p.txt') as f:
    numbers = [number.strip() for number in f.readlines()]


for number in numbers:
    headers = {
    'accept': 'application/json',
    'api-key': 'key1',
}
    r = requests.get(f'http://localhost:8000/check/{number}', headers=headers)
    print(f'{number}: {r.status_code}')
