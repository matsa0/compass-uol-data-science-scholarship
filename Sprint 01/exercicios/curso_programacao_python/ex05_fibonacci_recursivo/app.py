#Fibonacci

def fibonacci(num):
    if num == 1:
        return [0]
    elif num == 2:
        return [0, 1]
    else:
        sequence = fibonacci(num - 1)
        sequence.append(sequence[-1] + sequence[-2])
        return sequence
    
if __name__ == '__main__':
    try:
        num = int(input("Digite o número para gerar a sequência fibonacci: "))
        result = fibonacci(num)
    except ValueError:
        print("Erro. Digite um valor válido!")
    else:
        print(f'Sequência fibonacci: {result}')