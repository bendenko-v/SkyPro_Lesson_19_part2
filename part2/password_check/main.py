# Напишите функцию, которая получает пароль
# в открытом виде первым аргументом и хеш вторым аргументом.
# После чего берет хеш от пароля в открытом виде и сравнивает хеши.
# При хэшировании необходимо использовать алгоритм md5
#
# Для удобства самопроверки мы предоставляем вам пароль в открытом виде:
# H4RDP4S$w0rd
# и хеш в формате md5:
# 80309097b712c6828d0f3f6dfd713e80
#
# ##############################################
# Сложно: Напишите функцию, которая получает пароль 
# в открытом виде, хеш, соль и алгоритм хеширования, 
# берет хеш от пароля в открытом виде и сравнивает хеши
#
# Для самопроверки:
#
# Пароль:
# H4RDP4S$w0rd
#
# Хэш sha256:
# b'\xb6`^\x81q\xd8e\x0b\x1f\x93YR\x8dE\x0c\x0f\xc2\xe4\xbc\x14\xf5\xdf\xdc\xec\xad\xcf\xf3\xca\xd2C\x17\xbb'
#
# Соль:
# Skypro
#
# Число итераций: 1000
import hashlib
import hmac


def easy(pwd_hash, other_password):
    hash_other = hashlib.md5(other_password.encode('utf-8')).hexdigest()
    return pwd_hash == hash_other


ALGO = 'sha256'
SALT = b'Skypro'
PWD_HASH_ITERATIONS = 1000
pwd_to_check = 'H4RDP4S$w0rd'
hash_to_check = b'\xb6`^\x81q\xd8e\x0b\x1f\x93YR\x8dE\x0c\x0f\xc2\xe4\xbc\x14\xf5\xdf\xdc\xec\xad\xcf\xf3\xca\xd2C\x17\xbb'


def hard(password_hash, other_password, salt, algo):
    return hmac.compare_digest(
        password_hash,
        hashlib.pbkdf2_hmac(algo, other_password.encode('utf-8'), salt, PWD_HASH_ITERATIONS)
    )


# данные для самопроверки, взятые сверху
print(hard(hash_to_check, pwd_to_check, SALT, ALGO))

# данные для проверки из test_hard
print(hard(
    b'\x87jZ\x17\xf6g\xbb\xd3q\xf9\xb9t\x06O\x08K\x9a\xf4\xa2?YD$\x90N@@\xacodUP',
    'T3$tP4ssword',
    b'testSalt',
    'sha256'),
)
