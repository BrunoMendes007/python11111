url = "bytebank.com/cambio?moedaDestino=do&quantidade=100&moedaOrigem=real"

url ="    "
#Sanitizasao
url = url.replace("   ","   ")

if url =="":
    raise ValueError("A URL esta vazia")

# Separa a base e parâmetros
indice_interrogacao = url.find('?')
url_base = url[8:indice_interrogacao]
url_parametros = url[indice_interrogacao + 1:]
print(url_parametros)


#Busca o valor de um parâmetro
parametro_busca = 'quantidade'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url.parametros.find('&', indice_valor)
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor]
else:
valor = url_parametros[indice_valor:indice_e_comercial]

print(valor)
