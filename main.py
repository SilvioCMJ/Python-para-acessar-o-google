from googlesearch import search

pesquisa = 'teste'
#buscando resuoltados
result = list(search(pesquisa, Long='pt-BR', num_results=5))
print(result)