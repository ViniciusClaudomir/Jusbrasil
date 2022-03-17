from src.controllers.crawler.crawler_controller import CrawlerController
from src.controllers.adapters.adapter_digitalocean import AdapterDigitalOcean
from src.controllers.adapters.adapter_vultr import AdapterVultr


crawler = CrawlerController(AdapterVultr)
crawler.handle('https://www.vultr.com/pricing/#cloud-compute')
crawler.console()
crawler.to_json('vultr.json')
crawler.to_csv('vultr.csv')


crawler = CrawlerController(AdapterDigitalOcean)
crawler.handle('https://www.digitalocean.com')

crawler.console()
crawler.to_json('digitalocean.json')
crawler.to_csv('digitalocean.csv')