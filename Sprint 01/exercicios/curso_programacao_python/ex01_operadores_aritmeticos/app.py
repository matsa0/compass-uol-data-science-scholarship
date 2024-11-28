'''
Além da soma, exiba:
subtração
divisão
módulo
o primeiro elevado ao segundo
'''
x = y = 0

x = int(input("Digite um número inteiro: "))
y = int(input("Digite outro número inteiro: "))

soma = x + y
subtracao = x - y
divisao = x / y
modulo = x % y
elevado = x ** y

print("A soma entre x e y é: ", soma)
print("A subtração entre x e y é: ", subtracao)
print("A divisão entre x e y é: ", divisao)
print("O módulo entre x e y é: ", modulo)
print("O primeiro elevado ao segundo entre x e y é: ", elevado)