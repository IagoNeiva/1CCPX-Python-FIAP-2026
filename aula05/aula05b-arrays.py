lista_frutas = ["morango", "Maça", "Uva"]

# lista_fruta[0] = "Morango"
# lista_fruta[1] = "Maça"
# lista_fruta[2] = "Uva"
print(lista_frutas[0])

print()

lista_frutas.append("Melancia")
print(lista_frutas[3])

print()

for i in range(len(lista_frutas)):
    print(lista_frutas[i])

print()

for fruta in lista_frutas:
    print(fruta)