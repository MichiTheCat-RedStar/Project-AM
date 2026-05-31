#    TeaCoder_File2Str // ☭
# MichiTheCat-RedStar (c) 2026


from TeaCoder2_File2Str_Lib import tEncrypt, tDecrypt

print('MichiTheCat-RedStar (c) 2026')

while True:
	print('\n1 - file2str\n2 - str2file')
	try:
		user = input('\n>>> ')
		if user == '1':
			with open(input('\nУкажите путь: '), 'rb') as f:
				print(tEncrypt(f.read(), input('Задайте ключ: ')))
		elif user == '2':
			with open(input('\nУкажите путь: '), 'wb') as f:
				f.write(tDecrypt(input('Base64 шифр: '), input('Введите ключ: ')))
				print('Успешно!')
	except KeyboardInterrupt: print(); continue
	except Exception as e: print('\nОшибка: ', e)
