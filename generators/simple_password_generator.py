
class Generator:
    def __init__(self):
        """Список паролей для взлома формирует пользователь программы"""
        self.password_list = ['batman', 'password', 'master', 'hello', '12345']
        self.index = 0

    def next(self):
        """Функция перебора каждого пароля"""
        if self.index < len(self.password_list):
            result = self.password_list[self.index]
            self.index += 1
        else:
            result = None

        return result

