# import random
# import os   # responsavel pela integração com o sistemas
from auxiliar.operacoes_fundamentais import soma, sub, mult, div


# funções
def soma (x, y):
    s = x + y
    return s    # ou podendo usar return = x + y, já retornando o calculo


def sub (x, y):
    su = x - y
    return s


def mult (x, y):
    m = x * y
    return m


def div (x, y):
    if y == 0:
        return "Operação inválida, pois o divisor é 0."
    
    d = x / y
    return d


# inicio
# os.system("cls")    # limpa o terminal

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
# num1 = random.randint(1, 10)
# num2 = random.randint(1, 10)

# os.system("cls")

# print(f"Os números selecionados foram {num1} e {num2}")


print("\n ###### MENU DE OPERAÇÕES MATEMÁTICAS #####")
print(45 * "=")
print("\n[1] - Soma\n[2] - Subtração\n[3] - Multiplicação\n[4] - Divisão")

opcao = int(input("\nEscolha uma operação: "))

match opcao:

    case 1:
        resultado = soma(num1, num2)

    case 2:
        resultado = sub(num1, num2)

    case 3:
        resultado =  mult(num1, num2)

    case 4:
        resultado = div(num1, num2)

    case _:
        print("Opção inválida")

print(f"O resultado a sua operação é: {resultado}")
