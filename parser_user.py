import requests
from datetime import datetime

response = requests.get('http://127.0.0.1:3000/alex')

data = response.json()

possible_pass =    [data['username'],
                    data['first_name'],
                    data['second_name'],
                    str(data['email'])[0:-8],
                    datetime.fromtimestamp(int(data['DOB'])).strftime('%Y')[-2:],
                    datetime.fromtimestamp(int(data['DOB'])).strftime('%Y'),
                    datetime.fromtimestamp(int(data['DOB'])).strftime('%m%Y'),
                    datetime.fromtimestamp(int(data['DOB'])).strftime('%d%m%Y'),
                ]


f = open('pass.txt', 'w')

for index in possible_pass:
    f.write(index + '\n')

f.close
