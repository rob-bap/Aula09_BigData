def soma (x, y):
    s = x + y
    return s


def sub (x, y):
    su = x - y
    return su


def mult (x, y):
    m = x * y
    return m


def div (x, y):
    d = x / y
    return d


num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("\n ###### MENU DE OPERAÇÕES MATEMÁTICAS #####")
print(40 * "=")
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

print(f"O resultado a sua operação é: {resultado:.2f}")