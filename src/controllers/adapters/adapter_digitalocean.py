import requests as r
from parsel import Selector
import re
from .helpers.digitalocean import (restructure_json, restructure_droplet_config, concat, Vt)



class AdapterDigitalOcean():
    def to_dict(self, url_base: str):
        '''
        O caso da digital ocean foi mais interresante, por ser uma pagina renderizada com javascript com base
        na interação do usuario, não dava para obter os dados de maneira mais cotidiana, para isso recuperei o arquivo .js
        onde era pre-carregado esses dados durante a requisição
        
        link: https://www.digitalocean.com/_next/static/chunks/pages/pricing-11a835d19308d25d.js
        
        nesse arquivo .js, os dados do droplets são divididos em 2 sessões, uma que possui os dados referente a memoria, HD, SSD
        e o outro referente aos custos
        
        na primeira parte vamos pegar os dados referentes aos valores utilizando regex na linha 25 e 26
        e logo apos pegamos os dados referente a memoria na linha 30 e 31
        
        apos fazer o merge entre os 2 dicionarios, retornamos os dados estruturados para o controller
        '''
        response = r.get(url_base+"/pricing")
        etree = Selector(response.text)
        url_pricing_js = url_base + etree.xpath("*//script[contains(@src, 'pricing-')]").xpath('@src').get()
        response = r.get(url_pricing_js)
        droplets_itens = re.findall('{droplet:.*?}.{3}', response.text)
        droplets_itens = [restructure_json(x) for x in droplets_itens]
        config_droplet = "d_=(.*?),m_"
        string = re.search(config_droplet,response.text).group(1)
        droplets_config = re.findall('{column_text_1.*?}', string)
        droplets_config = [restructure_droplet_config(x) for x in droplets_config]

        cabecalho = droplets_config[0]
        dados = droplets_config[1:]
        dict_object = {0:{'title':'Basic Droplets', 'data':{}}}

        cust_rate = {}
        for droplets in droplets_itens:
            id_ = droplets['droplet']['size_id']
            month = droplets['droplet']['item_price']['usd_rate_per_month']
            hour = droplets['droplet']['item_price']['usd_rate_per_hour']
            cust_rate.setdefault(id_, {'$/HR':hour, '$/MO':month})

        c = 0
        for obj in dados:
            new_layout = {}
            pass_ = True
            for k, v in obj.items():
                new_key = cabecalho[k]
                if k == 'column_text_7':continue
                if not v:continue
                if v in list(cabecalho.values()):
                    pass_ = False
                new_layout.setdefault(new_key, v)
            if pass_:
                new_layout['$/HR'] = cust_rate[new_layout['$/HR']]['$/HR']
                new_layout['$/MO'] = cust_rate[new_layout['$/MO']]['$/MO']
                dict_object[0]['data'].setdefault(c, new_layout)
                c += 1
        return dict_object
