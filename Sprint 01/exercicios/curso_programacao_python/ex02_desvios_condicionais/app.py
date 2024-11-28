n1=n2 = 0.0

n1 = float(input("Digite a nota da prova 1: "))
if(n1 < 0.0 or n1 > 10.0):
    print("Nota inválida!")
    exit()

n2 = float(input("Digite a nota da prova 2: "))
if(n2 < 0 or n2 > 10):
    print("Nota inválida!")
    exit()

faltas = int(input("Digite o seu número de faltas: "))

media = (n1 + n2) / 2

if(faltas >= 10):
    print("Reprovado por falta! \nNúmero de faltas: ", faltas)
    print("Nota final: ", media)
    exit()

print()

if(media >= 6):
    print("Aprovado com: ", media, ", parabéns!")
    print("Número de faltas: ", faltas)
elif(media == 10):
    print("Aprovado com nota máxima, parabéns!!")
    print("Número de faltas: ", faltas)
else:
    print("Reprovado com: ", media)
    print("Número de faltas: ", faltas)