nomes_lista = ['Ana', 'Maria', 'Vini', 'Mat']

tamanho_texto = len(nomes_lista)
print(tamanho_texto)

for i in range(len(nomes_lista)):
    for j in range(i + 1, len(nomes_lista)):
        print(nomes_lista[i], nomes_lista[j])

