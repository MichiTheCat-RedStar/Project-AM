from random import choice

# Списки слов для шифровки | Символы для определения ключа
_WORDS = {
	'RU':['привет', 'программирование', 'кодировка', 'питон', 'бобёр', 'общежитие', 'хрустящий', 'наименование'],
	'ENG':['hello', 'world', 'code', 'python'],
	'NUM':[x for x in range(0, 10)], # Заменить из-за отсутствия смысла в шифровке, лучше использовать _SPEC или вместо _SPEC ставить тот символ, который и вызвал fallback
	'SPEC':['*NULL', '_NULL', '-NULL', '=NULL', '+NULL'] }
_SYMBS = {
	'RU':list('йцукенгшщзхъфывапролджэячсмитьбюё'),
	'ENG': list('qwertyuiopasdfghjklzxcvbnm') }

_LenWords = 0 # Количество всех слов
for lang in _WORDS: _LenWords += len(_WORDS[lang])

def WordCrypt(text:str) -> str:
	crypted, last_len = '', 0
	text = list(text)
	loaded = []
	for chr in text: # Цикл загрузки слов для того, чтобы не делать это каждый раз в следующем цикле
		'''
		if chr in _SYMBS['RU']: # Переписать все .append() на +=, но исправив проверку _WORDS по словам, а не списку
			if not _WORDS['RU'] in loaded: loaded.append(_WORDS['RU'])
		elif chr in _SYMBS['ENG']:
			if not _WORDS['ENG'] in loaded: loaded.append(_WORDS['ENG'])
		else:
			if not _WORDS['SPEC'] in loaded: loaded.append(_WORDS['SPEC'])
		'''
		# Сделать так, чтобы список добавлял только новое
		if chr in _SYMBS['RU']: loaded += _WORDS['RU']
		elif chr in _SYMBS['ENG']: loaded += _WORDS['ENG']
		else: loaded += _WORDS['SPEC']
	loaded = list(dict.fromkeys(loaded))
	for chr in text: # Цикл перевода каждой буквы в шифр
		chr = chr.lower() # Нужно добавить проверку строчной или заглавной буквы, пока что тут это
		randSymb = [] # Каждый раз создаёт пустой список, заполняемый случайными словами для последующей шифровки
		for word in loaded:
			if chr in word:
				randSymb.append(word)
		#print(loaded)
		#print(randSymb)
		for word in randSymb:
			print(word, '-', list(word).index(chr))
			break
		#TODO: Брать слова и через randSymb вставлять случайный через choice
	return crypted

print('MichiTheCat-RedStar (c) 2026 - words:', _LenWords)
print(WordCrypt(input('\n>>> ')))
