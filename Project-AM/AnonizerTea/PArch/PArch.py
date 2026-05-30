# 		PArch // ☭
# MichiTheCat-RedStar (c) 2026

def PArch(path:str) -> None:
	try:
		if '.' in list(path):
			cont = path.strip().split('.')
			cont = path.split('.')[-1]
		else:
			cont = ''
		with open(path, 'rb') as f:
			fIn = f.read()
			with open('PArchOut.py', 'w') as fOut:
				fOut.write(f"with open('PArch.{cont}', 'wb') as f: f.write({fIn})")
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
