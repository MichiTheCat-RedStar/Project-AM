import hashlib

def Hash(text:str) -> str:
	text = hashlib.sha512(text.encode())
	text = text.hexdigest()
	return text


if __name__ == '__main__':
	print('MichiTheCat-RedStar (c) 2026')
	while True:
		_user = input('\n>>> ')
		print('\n', Hash(_user))
