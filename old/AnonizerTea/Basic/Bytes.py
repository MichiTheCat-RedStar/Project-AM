def BytesIn(text:str) -> bytes:
	text = text.encode('utf-8')
	return bytes(text)


def BytesOut(content:bytes) -> str:
	content = content.decode('utf-8')
	return content


if __name__ == '__main__':
	print('MichiTheCat-RedStar (c) 2026')
	while True:
		_user = input('\n>>> ')
		print('\nБайты:\n', BytesIn(_user))
		print('\nВернувшийся в исходное состояние текст:\n', BytesOut(BytesIn(_user)))
