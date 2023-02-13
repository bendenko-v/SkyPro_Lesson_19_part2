# Просто: Напишите функцию `easy` которая 
# получает пароль в открытом виде и 
# возвращает хеш с использованием алгоритма md5
#
# Сложно: Напишите функцию `hard` которая 
# получает пароль в открытом виде и соль 
# и возвращает хеш с использованием алгоритма sha256
import hashlib
import base64


def easy(password):
    hash_pw = hashlib.md5(password.encode('utf-8'))
    return hash_pw.hexdigest()


def hard(password, salt):
    hash_digest = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 1000)
    return hash_digest