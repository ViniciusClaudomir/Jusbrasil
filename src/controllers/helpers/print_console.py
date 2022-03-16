def print_table(dict_values):
    for tables in dict_values:
        dados = dict_values[tables]
        titulo = dados['title']
        for index, row in enumerate(dados['data']):
            if index == 0:
                header = dados['data'][row].keys()
                print_header = '\t| '.join(header)
                print(titulo)
                print('-'*(len(print_header)+20))
                print(print_header)
                print('-'*(len(print_header)+20))
            cells =  dados['data'][row].values()
            print_cell = '\t|\t'.join(cells)
            print(print_cell)
        print()