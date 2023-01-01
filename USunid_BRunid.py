def USunid_BRunid(lista, numCasas):
    lista1 = []
    casas = '{:,.'+str(numCasas)+'f}'
    for i in range(1,len(lista)):
        '''Criando uma lista de strings de números expressos com ponto no decimal e vírgula no milhar'''
        lista1 = [casas.format(lista[i-1]), casas.format(lista[i])]
        '''Convertendo strings de numeros com ponto no decimal e vírgula no milhar para 
        strings com virgula no decimal e pono no milhar:'''
        lista2 = []
        for j in range(len(lista1)):
            a = lista1[j]
            a1 = a.replace(',', 'x') # troca provisoriamente a virgula do milhar para string 'x'
            a2 = a1.replace('.', ',') # troca ponto do decimal para vírgula
            y = a2.replace('x', '.') # traca o 'x' do milhar para ponto
            lista2.append(y)

        return lista2
