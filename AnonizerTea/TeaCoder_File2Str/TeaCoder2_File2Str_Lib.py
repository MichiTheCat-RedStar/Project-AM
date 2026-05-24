#    TeaCoder_File2Str // ☭
# MichiTheCat-RedStar (c) 2026


# Импорт Библиотек
from base64 import b64encode as tEnBase64, b64decode as  tDeBase64
from hashlib import sha512
from secrets import token_urlsafe as tRandomStr, randbits as tRandomBits, token_hex as tRandomHex, token_bytes as tRandomBytes
from random import seed as rSeed, random as rNumber, randint as rRandom


# Встроенные Функции
def tHash512(text:str) -> str: return sha512(text.encode()).hexdigest()
def tBinary(text:str) -> int: return int(''.join(f'{byte:08b}' for byte in text.encode('utf-8')))
def rBool() -> bool: return True if rRandom(0, 1) else False


# Протоколы шифрования
import lib # Заглушка, пока там устаревший PurrCrypt


# Основные Функции
def tEncrypt(content:bytes, key:str) -> str:
	key = tBinary(key)
	content = content.decode('latin-1')
	# TODO шифрование
	return content

def tDecrypt(content:str, key:str) -> bytes:
	key = tBinary(key)
	# TODO ...
	return bytes(content.encode())


# Проверка
if __name__ == '__main__':
	print('MichiTheCat-RedStar (c) 2026')
	while True:
		_user = input('\n>>> ')
		print(f'\nЗащищено:\n{tEncrypt(_user.encode(), key="42")}')
		print(f'\nВернувшийся в исходное состояние текст:\n{tDecrypt(tEncrypt(_user.encode(), key="42"), key="42").decode("utf-8")}')
