# У вас есть словарь, который содержит 
# данные о пользователе. На его основе 
# сгенерируйте токен. 
#
# В качестве секрета используйте слово 's3cR$eT',
# В качестве алгоритма формирования токена используйте 'HS256'.
# Сгенерированный токен запишите в переменную access_token.

import jwt

data = {
    "username": "Skypro",
    "role": "admin"
}

secret = 's3cR$eT'
algo = 'HS256'

access_token = jwt.encode(data, secret, algorithm=algo)
