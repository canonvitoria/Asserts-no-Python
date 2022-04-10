# Assert no python consiste em ser uma estrutura do mesmo, quando usamos o assert é +/- a usar o "for"
#Serve para verificar se uma condição está sendo satisfeita para garantir a continuação do código
#Usado apenas para produção

#Exemplo ->

print("Início")
assert 1 < 2      #Se eu colocar 1 > 2 vai aparecer como "assertionError" ou seja um erro de asssert, sendo assim mais fácil de encontrar o erro
print("Final")

#Caso prático ->

import request

requisicao = request.get("https://economia.awesomeapi.com.br/last/USD-BRL")
requisicao_dic = requisicao.json()

cotacao = requisicao_dic["USDBRL"]["bid"]
cotacao = float(cotacao)
print(cotacao)

preco_produto = 100

assert cotacao > 0

faturamento = preco_produto * cotacao
print(faturamento)

