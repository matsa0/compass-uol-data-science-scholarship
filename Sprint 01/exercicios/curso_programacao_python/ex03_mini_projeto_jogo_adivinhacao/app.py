import random
import os

random_number = random.randint(1, 15)  

print("Bem-vindo ao jogo de adivinhação!")
attempts = 3

while True:
    guessed_number = int(input("Adivinhe um número inteiro entre 1 e 15: "))

    if(random_number > guessed_number):
        attempts -= 1
        print("\nO número a adivinhar é maior!")
    elif(random_number < guessed_number):
        attempts -= 1
        print("\nO número a adivinhar é menor!")
    else:
        print("Parabéns! Você acertou!")
        print(f"Número adivinhado: {random_number}")

    if(attempts == 0 or random_number == guessed_number):
        print("\nFim de jogo!")
        print(f"Número secreto: {random_number}")
        restart = str(input(f'\nDeseja iniciar um novo jogo? (s - sim, n- não): '))
        if(restart.lower() == 's'):
            print("Gerando novo número...")
            os.system('clear')
            random_number = random.randint(1, 15)  
            attempts = 3
            continue
        elif(restart.lower() == 'n'):
            break

    if(attempts > 0 and random_number !=  guessed_number):
        print(f'Tentativas restantes: {attempts}')

