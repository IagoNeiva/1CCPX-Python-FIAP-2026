# Operadores de Atribuição
num = 15
print(num)

num = num + 2
print(num) # 17

num += 2
print(num)

# Operadores Relacionais

print() # Pular linha
print(6 == 3)

idade = 20
print(idade == 20)

maior_idade = idade >= 18
print(maior_idade)

# Operadores Logicos
# Logica E (and)
print() # Pular linha

verifica_email = True
verifica_senha = False

login = verifica_email and verifica_senha
print(login)

if login:
    print("Entrar no programa")
if not login:
    print("Po cara, acerta ai...")

print() # Pular linha
# Notas...

nota_final = 5

if nota_final <4:
    print("Reprovado")
elif nota_final < 6:
    print("Recuperação")
else:
    print("Aprovado")

print("Fim")