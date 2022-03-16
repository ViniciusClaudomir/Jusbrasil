from typing import Any
import requests as r
from bs4 import BeautifulSoup as bs

class CrawlerController():
    
	def __init__(self, crawlerAdapter) -> None:
		self.crawlerAdapter = crawlerAdapter()
    
	def handle(self, url: str) -> Any:
		try:
			response = r.get(url)
			if response.status_code != 200:
				return False

			page = bs(response.text, 'html')
			self.dict_page = self.crawlerAdapter.to_dict(page)
            

		except Exception as e:
			print(e)
			return False