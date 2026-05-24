def Caesars(text:str, ROT:int) -> str:
	result = []
	for c in list(text):
		if 'a' <= c <= 'z':
			result.append(chr((ord(c) - ord('a') + ROT) % 26 + ord('a')))
		elif 'A' <= c <= 'Z':
			result.append(chr((ord(c) - ord('A') + ROT) % 26 + ord('A')))
		elif 'а' <= c <= 'я':
			result.append(chr((ord(c) - ord('а') + ROT) % 32 + ord('а')))
		elif 'А' <= c <= 'Я':
			result.append(chr((ord(c) - ord('А') + ROT) % 32 + ord('А')))
		else:
			result.append(c)
	return ''.join(result)


if __name__ == '__main__':
	print('MichiTheCat-RedStar (c) 2026')
	while True:
		_user = input('\n>>> ')
		print()
		for rot in range(33):
			print(f'ROT{rot}: {Caesars(_user, rot)}')
