from typing import Any
import requests as r

class CrawlerController(): 
	def __init__(self) -> None:
		pass

	def handle(self, url: str) -> Any:
		
		response = r.get(url)
		if response.status_code == 200:
			return True