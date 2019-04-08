#-*- coding:utf-8 -*-
import csv
import requests
from bs4 import BeautifulSoup

class search():
	def __init__(self, search, nPage, proxies=None):
		"""
			@params str search
			@param int nPage
			@params dict proxies={'https': 'http://10.10.1.10:1080'}
		"""
		self.search = self.ReplaceChar(search)
		self.page = []
		self.nPage = nPage*10
		self.result = []
		self.proxies = proxies

	def Run(self):
		count = 0
		while self.nPage >= count:
			if self.proxies != None:
				self.page.append(requests.request('GET', "https://www.google.com.br/search?q="+str(search)+"&oq="+str(search)+"&start="+str(count),proxies=self.proxies))
				count = count*10
			else:
				self.page.append(requests.request('GET', "https://www.google.com.br/search?q="+str(search)+"&oq="+str(search)+"&start="+str(count)))
				count = count*10
		for x in range(0, len(page)):
			self.result.append(soup.find("div", {"id": "search"}))

	def SaveInHtml(self, path):
		arquivo = open(path+'result.html', 'a+')
		for x in result:
			for x in result:
				arquivo.write(x)
		arquivo.close()


	def ReplaceChar(self, string):
		with open('caracteres.csv') as f:
			f_csv = csv.DictReader(f)
			for row in f_csv:
				string = string.replace(row['simb'], row['ASC'])
		return string

procura = search("ovos lindos",3)
procura.Run()
procura.SaveInHtml("test")
