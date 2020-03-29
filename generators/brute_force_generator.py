class Generator:
    def __init__(self):
        """Задача алфавита, из которого состоит пароль"""
        self.state = 0
        self.length = 0
        self.alphabet = '0123456789qwertyuiopasdfghjklzxcvbnm'
        self.base = len(self.alphabet)  # Кол-во используемых в пароле символов

    def next(self):
        """Функция перебора каждого предполагаемого пароля"""
        password = ''
        temp_state = self.state  # Локальный счётчик

        while temp_state > 0:
            ceil = temp_state // self.base  # Уменьшение числа на разряд
            rest = temp_state % self.base  # Индекс символа, который будет добавлен

            # Новый символ добавляется слева к паролю
            password = self.alphabet[rest] + password

            # Строка предотвращает "зацикливание" программы и уменьшает число на разряд
            temp_state = ceil

            # Приписываем ноль в левой части генерируемого пароля
            password = self.alphabet[0] * (self.length - len(password)) + password

            # Номер комбинации в разряде length
            self.state += 1

            # Условие для начала нового перебора символов с большим кол-вом разрядов
            # При первом проходе пароль обнуляется и разряд пароля увеличивается
            if password == self.alphabet[-1] * self.length:
                self.length += 1
                self.state = 0

            return password
