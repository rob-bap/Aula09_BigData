def soma (x, y):
    s = x + y
    return s    # ou podendo usar return = x + y, já retornando o calculo


def sub (x, y):
    su = x - y
    return su


def mult (x, y):
    m = x * y
    return m


def div (x, y):
    if y == 0:
        return "Operação inválida, pois o divisor é 0."
    
    d = x / y
    return d