#		looking // ☭
# MichiTheCat-RedStar (c) 2026

from CrawlerLib import Crawler
crawler = Crawler(returning=True, return_only_files=False)

print('looking - MichiTheCat-RedStar (c) 2026')
while True:
	try:
		Path = input('\nУкажите директорию: ').strip()
		if Path == '': Path = '.'
		files = crawler.walk(path=Path)
		print('\nНа каком уровне в виде числа\n | На каком уровне в визуальном виде\n |  |         Название файла\n V  V          V')
		for f in files['paths']:
			_ = list(f)
			__ = 0
			for i in _:
				if '/' == i:
					__ += 1
			print(f'[{__-1}]', '>'*__, f.split('/')[-1])
		print(f'\nВсего файлов и папок: [{len(files["paths"])}]')
	except Exception as e: print('\nОшибка:', e)
