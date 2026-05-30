# WordCrypter // v0.3a
# MichiTheCat-RedStar (c) 2026

from random import choice


# Списки слов для шифровки | Символы для определения ключа
_WORDS = {
	'RU':[],
	'ENG':[] }
_SYMBS = {
	'RU':list('йцукенгшщзхъфывапролджэячсмитьбюё'+'йцукенгшщзхъфывапролджэячсмитьбюё'.upper()),
	'ENG': list('qwertyuiopasdfghjklzxcvbnm'+'qwertyuiopasdfghjklzxcvbnm'.upper()) }
with open('./WORDS/RU', 'r') as f: _WORDS['RU'] = f.read().strip().split('\n')
with open('./WORDS/ENG', 'r') as f: _WORDS['ENG'] = f.read().strip().split('\n')

_lenWords = 0 # Количество всех слов
for lang in _WORDS: _lenWords += len(_WORDS[lang])


def WordCrypt(text:str) -> str:
	"Шифрует слова в последовательность слов"
	crypted = ''
	
	#TODO: Структура кода
	# Просмотреть слова пользователя:
	#  Понять какие нужно использовать раскладки
	#  Просмотреть какие слова есть на конкретные символы
	#  Выбрать слова на эти символы в список случайных
	# ...?
	
	langWords = []
	'''
	for chr in list(text): # Прохожу первый раз, чтобы понять, какие слова использовать
		if (chr in _SYMBS['RU']) and not (chr in list(langWords)): langWords.append(_WORDS['RU']), print(1)
		elif (chr in _SYMBS['ENG']) and not (chr in list(langWords)): langWords.append(_WORDS['ENG']), print(2)
	'''
	langWords += _WORDS['RU'] + _WORDS['ENG']
	
	curentWords = []
	for chr in text: # Нахожу слова, которые можно использовать для шифрования
		for word in langWords:
			for wordChr in word:
				if wordChr == chr:
					curentWords.append(word)
	
	lastLen = 0
	for chr in text: # Шифруем данные по шаблону
		for word in lastLen:
			if chr in lastLen:
				lastLastLen.append # Всё, уйдите, я не знаю что творю, я продолжаю программировать сонным шестой час подряд и дело не идёт вообще, я вижу что пишу бред, мне нужно было отдохнуть и выспаться - тогда бы были силы думать, а сейчас я слишком рассфокусирован и на сегодня лучшая версия, это предыдущая и первая, учитывая, что у них разные возможности... Всё, пока, до встречи в v0.3b, который я напишу позжа и уберу вот эту хрень выше
	
	return crypted


if __name__ == '__main__':
	print('MichiTheCat-RedStar (c) 2026 - words:', _lenWords)
	while True: print(WordCrypt(input('\n>>> ')))
