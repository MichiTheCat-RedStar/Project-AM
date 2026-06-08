#    TeaCoder_File2Str // ☭
# MichiTheCat-RedStar (c) 2026


# Импорт Библиотек
from base64 import b64encode as tEnBase64, b64decode as  tDeBase64
from hashlib import sha512
from secrets import token_urlsafe as tRandomStr, randbits as tRandomBits, token_hex as tRandomHex, token_bytes as tRandomBytes
from random import seed as rSeed, random as rNumber, randint as rRandom
from zlib import compress as zCompress, decompress as zDecompress


# Встроенные Функции
def tHash512(text:str) -> str: return sha512(text.encode()).hexdigest()
def tBinary(text:str) -> int: return int(''.join(f'{byte:08b}' for byte in text.encode('utf-8')))
def rBool() -> bool: return True if rRandom(0, 1) else False


# Протоколы шифрования
import lib # Заглушка, пока там устаревший PurrCrypt


# Основные Функции
''' unstable version | TeaCoder_File2Str
Описание шифрования:
	Значения:
		Контент -> сырые байты (чтение файла в 'rb')
		Ключ -> строка, но из-за использования PurrCrypt переводится в числа (через бинарное преобразование) // TODO: в PurrCrypter2 сделать автоматический перевод в числовые значения и все методы шифрования должны принимать строки
	Метод шифрования:
		Контент -> Base64 (убеждаемся, что все методы шифровая буду работать, так как не будет странных символов)
		Отпечаток0 -> Делаем sha512 отпечаток контента, чтобы сравнивать не был ли он изменён или побит
		Отпечаток1 -> Делаем sha512 отпечаток ключа, мы не будет его использовать в дешифровании из-за безопасности, но он нужен, чтобы вместо падения сразу написать, что ключ не подходит
		Соль -> Создаём соль (32-64)
		Ключ -> Соль+Ключ
		Контент -> Шифруем через выбранный метод шифрования по ключу (на стороне встройщика, но пока только PurrCrypt)
		Контент -> Base64 (Для приведения всего в один безопасный вид)
		Соль -> Base64 (для того, чтобы были безопасные символы в дальнейшем)
		// Получается Контент, Соль, Отпечаток0, Отпечаток1 - все в формате символов от A-Z и чисел от 0-9, то есть безопасно
		Контент -> Соль + '|' + Контент + '|' + Отпечаток0 + '|' + Отпечаток1 получается одна строка, а символ '|' является безопасным, так как не использует A-Z и 0-9, а значит его можно будет легко разбить по *.split('|'))
		Контент -> Base64 (Теперь точно одна безопасная строка)
	Метод дешифрования:
		Всё тоже самое, но наоборот...
	Задачи на стороне встройщика:
		Выбор методов шифрования из тех, что есть в ./protocols корневой папки
		GUI для удобства работы
		Сделать стандартную работу с файлами, вместо простого текста как в примере, читать из файлов сырые байты и записывать их при дешифровании, а при шифровании возвращать строку или записывать её
		// Задачей всего проекта является превращения любого файла в зашифрованную строку, которую можно передать даже QR-кодом при должном размере
		// Так же можно использовать библиотеку zlib для сжатия сырых байтов, чтобы строка занимала не так много места
'''

def tEncrypt(content:bytes, key:str) -> str:
	content = tEnBase64(content)
	hashedContent = sha512(content).hexdigest()
	hashedKey = sha512(key.encode('utf-8')).hexdigest()
	salt = tRandomBytes(32)
	key = tEnBase64(salt+key.encode('utf-8'))
	content = tEnBase64(content).decode('utf-8')
	content = lib.PurrCrypt.purr_encrypt(content, key=tBinary(key.decode('utf-8'))) # TODO: заменить PurrCrypt на выбор из методов шифрования
	content = tEnBase64(salt).decode('utf-8')+'|'+tEnBase64(content.encode('utf-8')).decode('utf-8')+'|'+hashedContent+'|'+hashedKey
	content = zCompress(content.encode('utf-8'))
	return tEnBase64(content).decode('utf-8')

def tDecrypt(content:str, key:str) -> bytes:
	content = tDeBase64(content.encode('utf-8'))
	content = zDecompress(content).decode('utf-8')
	content = content.split('|')
	try: salt, content, hashedContent, hashedKey = content
	except IndexError: raise ValueError('Неправильная строка!')
	salt = tDeBase64(salt.encode('utf-8'))
	content = tDeBase64(content.encode('utf-8')).decode('utf-8')
	if sha512(key.encode('utf-8')).hexdigest() != hashedKey: raise ValueError('Неправильный ключ!')
	key = tEnBase64(salt+key.encode('utf-8'))
	content = lib.PurrCrypt.purr_decrypt(content, key=tBinary(key.decode('utf-8'))) # TODO: тот же, что и выше - надо менять PurrCrypt
	content = tDeBase64(content).decode('utf-8')
	if sha512(content.encode('utf-8')).hexdigest() != hashedContent: raise ValueError('Контент отличаеся! (битый или изменённый)')
	return tDeBase64(content)


# Проверка
if __name__ == '__main__':
	print('MichiTheCat-RedStar (c) 2026')
	while True:
		_user = input('\n>>> ')
		_user = tEncrypt(_user.encode(), key='42')
		print(f'\nЗащищено:\n{_user}')
		print(f'\nВернувшийся в исходное состояние текст:\n{tDecrypt(_user, key="42").decode("utf-8")}')
