# Напишите функцию `check_token`, которая проверяет токен. 
# Внимание, функция должна принимать 3 позиционных агрумента:
# токен, алгоритм и секрет.
# Функция должна возвращать:
# Декодированную информацию если токен удалось декодировать.
# И возвращайть False, если токен декодировать не удалось.
import jwt


# В тестах мы проверим функцию,отправив ей верный и неверный токен.

def check_token(token, secret, algorithms):
    try:
        res = jwt.decode(token, secret, algorithms=algorithms)
        return res
    except Exception:
        return False
