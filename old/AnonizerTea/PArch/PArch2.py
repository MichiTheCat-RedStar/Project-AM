# 		PArch // ☭
# MichiTheCat-RedStar (c) 2026


from zlib import compress


def PArch(path:str) -> None:
	try:
		if '/' in list(path):
			cont = path.strip().split('/')
			cont = path.split('/')[-1]
		else:
			cont = path
		with open(path, 'rb') as f:
			fIn = f.read()
			fIn = compress(fIn, level=9)
			with open(f'{cont}_PArch.py', 'w') as fOut:
				fOut.write(f"from zlib import decompress\nwith open('PArch_{cont}', 'wb') as f: f.write(decompress({fIn}))")
	except Exception as e: return e


if __name__ == '__main__':
	print('MichiTheCat-RedStar (c) 2026')
	while True:
		_user = input('\n>>> ')
		if len(_user) > 5:
			if _user[0:5] == 'PArch':
				PArch(_user[6:])
			else:
				PArch(_user)
		else:
			PArch(_user)
