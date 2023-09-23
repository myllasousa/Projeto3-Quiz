score = 0

print('''
Q1 - Qual é a capital do Brasil?
a - Rio de Janeiro
b - Barcelona
c - Brasília
''')
resposta = input().lower()

if resposta == "a":
    print("Não, a resposta está incorreta :(")
elif resposta == "b":
    print("Não seja bobinho :(")
elif resposta == "c":
    print("Correto!! :)")
else:
    print("Você não escolheu a, b ou c")
if resposta == "c":
    score = score + 1

print('''
Q2 - Quantas patas tem uma aranha?
a - 8
b - 6
c - 50
''')
resposta = input().lower()

if resposta == "a":
    print("Correto!! :)")
elif resposta == "b":
    print("Não, a resposta está incorreta :(")
elif resposta == "c":
    print("Não seja bobinho :(")
else:
    print("Você não escolheu a, b ou c")
if resposta == "a":
    score = score + 1

print('''
Q3 - Quanto é 5 + 3 * 5 ?
a - 40
b - 1000
c - 20
''')
resposta = input().lower()

if resposta == "a":
    print("Não, devemos fazer a multiplicação primeiro :(")
elif resposta == "b":
     print("Não seja bobinho :(")
elif resposta == "c":
    print("Correto!! :)")
else:
    print("Você não escolheu a, b ou c")
if resposta == "c":
    score = score + 1

if score == 3:
    print("Muito bem!! Você acertou tudo!")
else:
    print("Tente novamente :(")

