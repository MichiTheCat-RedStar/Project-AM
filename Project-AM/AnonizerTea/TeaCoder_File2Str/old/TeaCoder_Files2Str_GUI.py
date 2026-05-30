from Basic import *
from random import randbytes
import gzip
from PurrCrypt import * # Временное решение

# Задача сделать код, где любой файл можно превратить в строку, которую можно расшифровать обратно, если знать ключ
def tEncode(content:bytes, key:str) -> str:
	try: content = Bytes.BytesOut(content)
	except UnicodeDecodeError: # на часах 6:41, я так и не лёг, дописываю код, так как побилось чтение фото, а точнее оно не utf-8, поэтому бьётся
		print('UnicodeDecodeError -> вероятно файл не текст.')
		content = str(content)
	content = Base64.Base64In(content) # сырые байты -> base64 // Теперь надо как-то превратить base64 в шифрованные данные
	salt = Base64.Base64In(str(randbytes(32)))
	hashContent = Hash.Hash(content)
	random = salt + key
	random = Binary.BinarIn(random)
	random = random.split(' ')
	random = ''.join(random)
	content = f'{salt}\n{hashContent}\n{purr_encrypt(content, key=int(random))}'
	content = Base64.Base64In(content)
	content = gzip.compress(content.encode('utf-8'))
	return content.decode('latin-1')


# Довольно тяжело писать код без нормального IDE и при этом не видя клавиатуру и вечно используя комментарии как брейншторм, например этот комментарий написан после тех, что в блоках ниже и выше (TEST и tEncode)
def tDecode(content:str, key:str) -> bytes:
	content = content.encode('latin-1') # Чем я занимаюсь в два часа ночи.. Пишу код уже как третий час, правда не конкретно этот, а вообще...
	try: content = gzip.decompress(content)
	except: pass
	try: content = content.decode('utf-8') # говнос, надо будет всё переписать, вся шифровка создана под работу с текстовыми файлами, а не бинарными, что идёт в разрез с изначальноё идеей, но я уже слишком сонный, чтобы всё с нуля переделывать...
	except: content = content.decode('latin-1')
	content = Base64.Base64Out(content)
	content = content.split('\n')
	salt = content[0] # Как я долго провозился с тем, чтобы превратить str как bytes в нормальные bytes, но за весь проект я очень сильно научился работать с типом bytes и у меня отпал вопрос про чтение файлов кроме текста, я получил ответ: сырые байты
	# Изменено: Я писла этот код в 2:00, но из-за ошибок в GUI версии пишу этот комментарий в 4:30, в общем не смотрите на комментарий выше, я полностью всё переписл, это было ещё хуже... Но мне грустно, что из-за неудобства я больше не делаю сотню коммитов и вы не видите прогресс, а только готовый продукт
	random = salt + key
	random = Binary.BinarIn(random)
	random = random.split(' ')
	random = ''.join(random)
	hashContent = content[1]
	content = content[2]
	content = purr_decrypt(content, key=int(random)) #TODO: Из-за псевдорандома мне надо переписать key= на int, это легко сделать используя Basic/Binary, но уже 4:50 и я иду спать, а так же нужно как-то убрать весь этот мусор из комментариев к релизу...
	if Hash.Hash(content) != hashContent: raise ValueError('Контент повреждён!') # 5:54, я всё пофиксил
	content = Base64.Base64Out(content)
	print(content)
	content = Bytes.BytesIn(content)
	return content


if __name__ == '__main__':
	#print(randbytes(32))
	print('MichiTheCat-RedStar (c) 2026')
	_TEST = r'Привет, TeaCoder! Спец Символы: / \ u0u#*02зУЦЗД0ёЁ,c3j d]{)'
	print('\nОбычная строка:\n', _TEST)
	# Задача проекта в том, чтобы совместить Base64, Hash и прочее с целью создания метода кодировки, который бы позволил закодировать любой файл, от текста до изображений, бинаркников и прочего (поэтому использует bytes) в строку, в которой бы не бились символы и которую бы можно было бы без потерь расшифровать, имея ключ
	_TEST = _TEST.encode('utf-8')
	_TEST = tEncode(_TEST, 'Aboba')
	print('\nЗакодированная строка:\n', _TEST)
	_TEST = tDecode(_TEST, 'Aboba')
	print('\nДекодированная строка:\n', _TEST.decode('utf'))
	# Надо будет читать файлы как rb - сырыми байтами, а потом ими оперировать
