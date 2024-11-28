#renomear todos os arquivos dentro de uma pasta
import os

diretorio_atual = os.chdir('/home/matsa/Teste')
print(f"Diretório atual > {os.getcwd()}\n")

def list_files(diretorio_atual):
    print(f"Listando o {diretorio_atual} antes de renomear:" )
    for arq in os.listdir():
        print(arq)

list_files(diretorio_atual)

nome_padrao = input("\nQual o padrão de nomes que você deseja colocar nos arquivos(sem extensão): ")

for cont, arq in enumerate(os.listdir()):
    if os.path.isfile(arq):
        nome_arq, exten_arq = os.path.splitext(arq)
        nome_arq = nome_padrao + ' ' + str(cont)

        novo_nome = f'{nome_arq}{exten_arq}'
        os.rename(arq, novo_nome)

print(f'\nArquivos renomeados.')

list_files(diretorio_atual)