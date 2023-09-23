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
