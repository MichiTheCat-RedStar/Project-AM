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

_LenWords = 0 # Количество всех слов
for lang in _WORDS: _LenWords += len(_WORDS[lang])

def WordCrypt(text:str) -> str:
	crypted, last_len = '', 0
	text = list(text)
	loaded = []
	for chr in text: # Цикл загрузки слов для того, чтобы не делать это каждый раз в следующем цикле
		# Сделать так, чтобы список добавлял только новое
		if chr in _SYMBS['RU']: loaded += _WORDS['RU']
		elif chr in _SYMBS['ENG']: loaded += _WORDS['ENG']
		else: crypted+=' '
	loaded = list(dict.fromkeys(loaded))
	for chr in text: # Цикл перевода каждой буквы в шифр
		chr = chr.lower() # Нужно добавить проверку строчной или заглавной буквы, пока что тут это
		randSymb = [] # Каждый раз создаёт пустой список, заполняемый случайными словами для последующей шифровки
		for word in loaded:
			if chr in word:
				randSymb.append(word)
		#print(loaded)
		#print(randSymb)
		for word in randSymb: # DEBUG
			if (list(word).index(chr)%(last_len+1)) == last_len: # Всё, мозг кипит, уже работаю третий час подряд, надо взять перерыв и дописать нормально
				last_len = len(word)
				print(word, '-', list(word).index(chr))
				crypted += word+' '
				break
		
	return crypted

print('MichiTheCat-RedStar (c) 2026 - words:', _LenWords)
print(WordCrypt(input('\n>>> ')))
