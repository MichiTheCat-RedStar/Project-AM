#		clone // ☭
# MichiTheCat-RedStar (c) 2026

from hashlib import sha1
from CrawlerLib import Crawler

print('clone - MichiTheCat-RedStar (c) 2026')
print('Выводит один клон файла, если находит его...')
PATH = input('\nВведите путь: ')

crawler = Crawler(returning=True)
all_search = len(crawler.walk(PATH)['paths'])

shas, search = {'sha':[], 'path':[]}, 0
def hashing(fp):
	global shas
	global search
	with open(fp, 'rb') as f:
		f = f.read()
		shas['path'].append(fp)
		print(f'\rПоиск... [{search+1}/{all_search}]', end='', flush=True) # print('\n'+fp, '\v-> ', f)
		search += 1
		shas['sha'].append(sha1(f).hexdigest())

crawler = Crawler(function=hashing)
crawler.walk(PATH)
print('\n') # print('\n', shas)

for sha in shas['sha']:
	if sha in shas['sha']:
		shas['path'].pop(shas['sha'].index(sha))
		shas['sha'].pop(shas['sha'].index(sha))
		try:
			shas['sha'].index(sha)
		except ValueError:
			continue
		else:
			print(shas['path'][shas['sha'].index(sha)], 'является клоном!')
input('\nEOF! ')

