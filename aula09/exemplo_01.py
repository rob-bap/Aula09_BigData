import random
import os

from auxiliar.operacoes import dobro, triplo, quadrado, metade
# def dobro(n):
#     d = n * 2
#     return d


# def triplo(n):
#     t = n * 3
#     return t


# def quadrado(n):
#     q = n ** 2
#     return q


# def metade(n):
#     m = n / 2
#     return m

os.system("cls")

# num = int(input('Informe o número: '))
num = random.randint(1, 100)

print(f"\nO número selecionados foi {num} ")
print("\n ##### MENU DE OPÇÕES #####")
print(30 * "=")
print("[1] - Dobro\n[2] - triplo\n[3] - Quadrado\n[4] - Metade")

opcao = int(input("\nInforme a sua opção: "))

match opcao:
    
    case 1:
        resultado = dobro(num)

    case 2:
        resultado = triplo(num)

    case 3:
        resultado = quadrado(num)

    case 4:
        resultado = metade(num)
    
    case _:
        print("Opção inválida.")

print(f"\nO resultado da sua operação é: {resultado} ")