def dobro(n):
    d = n * 2
    return d


def triplo(n):
    t = n * 3
    return t


def quadrado(n):
    q = n ** 2
    return q


num = int(input('Informe o número: '))

restuado_dobro = dobro(num)
restuado_triplo = triplo(num)
restuado_quadrado = quadrado(num)

print(f'Dobro: {restuado_dobro}')
print(f'Triplo: {restuado_triplo}')
print(f'Quadrado: {restuado_quadrado}')