from typing import Any
import requests as r
from bs4 import BeautifulSoup as bs
import json
from src.controllers.helpers.print_console import print_table
from src.controllers.helpers.save_csv import to_csv

'''
Ao importar o adapter o mesmo deve ter um metodo chamado to_dict onde deve retornar no formato

{
    0: {
        'title':'Titulo Qualquer',
        'data': {
            0: {
            
            }, ...
        
        }
    }, ...


}

'''

class CrawlerController():

    def __init__(self, crawlerAdapter) -> None:
        self.crawlerAdapter = crawlerAdapter()

    def handle(self, url: str) -> Any:
        try:
            response = r.get(url)
            if response.status_code != 200:
                return False

            self.dict_page = self.crawlerAdapter.to_dict(url)

        except Exception as e:
            print(e)
            return False

    def to_json(self, file_name: str) -> Any:
        if file_name.endswith(".json"):
            with open(file_name, 'w') as arq:
                arq.write(json.dumps(self.dict_page))
        else:
            raise Exception("Prefix json error")
            
    def to_csv(self, file_name: str) -> Any:
        if file_name.endswith(".csv"):
            with open(file_name, 'w') as arq:
                csv = to_csv(self.dict_page)
                arq.write(csv)
        else:
            raise Exception("Prefix csv error")
        
    def console(self):
        print_table(self.dict_page)
