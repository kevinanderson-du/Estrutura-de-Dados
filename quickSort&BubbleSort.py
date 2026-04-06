import random
import time

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivo = lista[len(lista)//2]
    menores = [x for x in lista if x < pivo]
    iguais = [x for x in lista if x == pivo]
    maiores = [x for x in lista if x > pivo]
    return quick_sort(menores) + iguais + quick_sort(maiores)

# teste
lista = [random.randint(0, 10000) for _ in range(1000)]

lista1 = lista.copy()
lista2 = lista.copy()

inicio = time.time()
bubble_sort(lista1)
print("Bubble Sort:", time.time() - inicio)

inicio = time.time()
quick_sort(lista2)
print("Quick Sort:", time.time() - inicio)