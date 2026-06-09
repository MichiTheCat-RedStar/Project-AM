#		CrawlersLib // ☭
# MichiTheCat-RedStar (c) 2026

from os.path import isdir, join as joindir, islink
from os import listdir

class Crawler:
	def __init__(self, path='.', function=lambda x: None, errors=True, returning=False, recursion=True, return_only_files=True):
		'''
		path - директория, в которой будет запущен crawler.
		function - какая функция применяется ко всем файлам.
		errors - возвращать ли ошибки или игнорировать их.
		returning - возвращать ли файл, название.
		recursion - осматривать папки внутри.
		return_only_files - возвращать ли только файлы или ещё и папки с ссылками. должно быть включено returning.
		'''
		self.path = path
		self.function = function
		self.errors = errors
		self.returning = returning
		self.recursion = recursion
		self.return_only_files = return_only_files
	
	def walk(self, path=None):
		'''
		path - директория, в которой будет запущен crawler, но если не указывать, то будет использован тот, что задан в атрибутах crawler, а если не указано и там, то будет использоваться директория, где открыт файл.
		'''
		if path == None: path = self.path
		result = {'paths':[], 'names':[]} if self.returning else None
		try:
			for element in listdir(path):
				full = joindir(path, element)
				if islink(full):
					if not self.return_only_files and self.returning: result['paths'].append(full); result['names'].append(element)
					continue
				if isdir(full) and self.recursion:
					if not self.return_only_files and self.returning: result['paths'].append(full); result['names'].append(element)
					sub_result = self.walk(path=full)
					if self.returning: result['paths'].extend(sub_result['paths']); result['names'].extend(sub_result['names'])
				else:
					self.function(full)
					if self.returning: result['paths'].append(full); result['names'].append(element)
		except Exception:
			if self.errors: raise
		else:
			return result


if __name__ == '__main__':
	_TEST = Crawler(path='_example', function=print, returning=True, return_only_files=False)
	print(_TEST:=_TEST.walk(), '\n\n')
	for _ in range(len(_TEST['names'])): # пример использования CrawlerBase - вот он создан для того, чтобы вывести все файлы и их директории из корневой папки
		print(f'{_TEST["names"][_]} -[{_}]-> {_TEST["paths"][_]}')
