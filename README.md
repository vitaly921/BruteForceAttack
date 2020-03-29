# Hack passwords

## How to run:

Открыть hack.py и указать методы запроса к серверу, а также определить генераторы логина, пароля.
Передать данные аргументу класса Hack.

`python hack.py`

## API requesters:

Чтобы добавить requester, необходимо создать файл в пакете requesters и создать там функцию.

`request(login, password): return bool`

## API generators:

Чтобы добавить generator, необходимо создать файл в пакете generators и создать там class:

```
class Generator:
    
    def next(self):
        return str or None
```
