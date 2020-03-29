
class Generator:
    def __init__(self):
        """Список логинов для взлома формирует пользователь программы"""
        self.login_list = ['cat', 'admin', 'jack', 'vitaly', 'julia', 'rodion', 'qween']
        self.index = 0

    def next(self):
        """Функция перебора каждого логина"""
        if self.index < len(self.login_list):
            result = self.login_list[self.index]
            self.index += 1
        else:
            result = None

        return result

