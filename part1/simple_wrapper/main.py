# Напишите декоратор jsonwrap, 
# который при вызове функции будет 
# результат выполнения функции превращать 
# в json строку и возвращать эту строку. 
# Примем на веру, что данные всегда или словарь или список.

import json


def jsonwrap(f):
    def wrapper():
        return json.dumps(f())
    return wrapper


# Ниже следует код для самопроверки:
# TODO Вы можете попробовать задекорировать функцию func
# которая возвращает словарь.

@jsonwrap
def func():
    return {'text': 'tasks',
            'author': 'skypro'}


if __name__ == "__main__":
    func()