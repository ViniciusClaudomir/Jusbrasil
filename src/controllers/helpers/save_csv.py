def to_csv(dict_values):
    csv = ''
    for tables in dict_values:
        dados = dict_values[tables]
        for index, row in enumerate(dados['data']):
            if index == 0:
                header = dados['data'][row].keys()
                csv_header = ','.join(header)
                csv += csv_header
            cells =  dados['data'][row].values()
            csv_cell = ','.join(cells)
            csv += '\n'+csv_cell
    return csv