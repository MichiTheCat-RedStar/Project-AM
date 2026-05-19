def BinarIn(text:str) -> str:
	text = text.encode('utf-8')
	return ' '.join(f'{byte:08b}' for byte in text)


def BinarOut(text:str) -> str:
    text = ''.join(text.split())
    if len(text) % 8 != 0:
        raise ValueError('Строка должна быть кратна восьми.')
    text = [int(text[i:i+8], 2) for i in range(0, len(text), 8)]
    return bytes(text).decode("utf-8")


if __name__ == '__main__':
	print('MichiTheCat-RedStar (c) 2026\n')
	while True:
		_user = input('>>> ')
		print('\nДвоичный код:\n', BinarIn(_user))
		print('\nВернувшийся в исходное состояние текст:\n', BinarOut(BinarIn(_user)), '\n')
