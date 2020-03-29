import requests


def request(login, password):
    """Фугкция обращения к защищённому серверу"""
    response = requests.post('http://127.0.0.1:4000/auth', json={'login': login, 'password': password})
    return response.status_code == 200
