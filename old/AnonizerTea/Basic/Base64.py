import base64

def Base64In(text:str) -> str:
	text = text.encode('utf-8')
	text = base64.b64encode(text)
	text = text.decode('utf-8')
	return text


def Base64Out(text:str) -> str:
	text = base64.b64decode(text)
	text = text.decode('utf-8')
	return text


if __name__ == '__main__':
	print('MichiTheCat-RedStar (c) 2026')
	while True:
		_user = input('\n>>> ')
		print('\nBase64:\n', Base64In(_user))
		print('\nВернувшийся в исходное состояние текст:\n', Base64Out(Base64In(_user)))
