texto = "FIAP Paulista"

print(texto[0])
print(texto[1])
print(texto[2])
print(texto[3])
print()

tamanho_texto = len(texto) # len = tamanho
print(tamanho_texto)

print()

for i in range(tamanho_texto):
    print(f'texto[{i}] = {texto[i]}') # Mostra os caracteres ao invés de números

print()

for c in texto:
    print(c)

