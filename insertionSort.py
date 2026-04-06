import random

def insertion_sort(lista):
    comparacoes = 0
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            comparacoes += 1
            lista[j + 1] = lista[j]
            j -= 1
        comparacoes += 1
        lista[j + 1] = chave
    return comparacoes

# cenários
ordenada = list(range(100))
reversa = list(range(100, 0, -1))
aleatoria = [random.randint(0, 100) for _ in range(100)]

print("Ordenada:", insertion_sort(ordenada.copy()))
print("Reversa:", insertion_sort(reversa.copy()))
print("Aleatória:", insertion_sort(aleatoria.copy()))