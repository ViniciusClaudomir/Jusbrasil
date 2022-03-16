import re
from bs4 import BeautifulSoup as bs


class AdapterVultr():
    def to_dict(self, page: bs) -> dict:
        table = page.find('div', {'id':'optimized-cloud-compute'})
        columns_element = table.find( 'div',{'class':'pt__header'})
        mask = {x.text.strip():'' for x in columns_element.find_all('div', {'class','pt__cell'}) if bool(x.text.strip())}
        list_columns = list(mask.keys())
        dict_object = {}
        for index_subsection, subsection in enumerate(reversed(table.find_all('div', {'class':"pricing__subsection", 'id':'storage-optimized'}))):
            title = subsection.find('p', {'class':'pricing__subsection-desc'}).text
            dict_object.setdefault(index_subsection, {'title':title, 'data': {}})
            rows = {}
            for index_row, row in enumerate(subsection.find_all('div', {'class':'pt__row'})):
                row_concated = []
                for index_cell, cell in enumerate(row.find_all('div', {'class', 'pt__cell'})):
                    retorno_regex = re.search('((|\$)+(\d+?\.\d+|\d+))', cell.text.strip()).group(1)
                    row_concated.append(retorno_regex)
                rows.setdefault(index_row, row_concated)
            for data in rows:
                new_row = {list_columns[index]:val for index, val in enumerate(rows[data])}
                dict_object[index_subsection]['data'].setdefault(data, new_row)
        return dict_object