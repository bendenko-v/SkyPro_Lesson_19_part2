# Написать функцию `generate_jwt` которая 
# генерирует access_token и refresh_token.
# В качестве аргумента функция должна принимать словарь вида user_obj.
# Для формирования токена используйте алгоритм 'HS256' и ключ 's3cR$eT'.
# В access и в refresh токене должна содержаться информация об:
# 1. имени пользователя ('username')
# 2. роли ('role')
# 3. времени действия токена ('exp')
# Время действия access токена должно составлять 30 с момента получения
# Время действия refresh токена - 130 дней c момента получения
import calendar
import datetime

import jwt

user_obj = {
    "username": 'test_user',
    "role": 'admin'
}

SECRET = 's3cR$eT'
ALGO = 'HS256'


def generate_jwt(data):
    timedelta_30min = datetime.datetime.now() + datetime.timedelta(minutes=30)
    timedelta_130days = datetime.datetime.now() + datetime.timedelta(days=130)

    data['exp'] = calendar.timegm(timedelta_30min.timetuple())
    access_token = jwt.encode(data, SECRET, algorithm=ALGO)

    data['exp'] = calendar.timegm(timedelta_130days.timetuple())
    refresh_token = jwt.encode(data, SECRET, algorithm=ALGO)

    return {
        'access_token': access_token,
        'refresh_token': refresh_token
    }
