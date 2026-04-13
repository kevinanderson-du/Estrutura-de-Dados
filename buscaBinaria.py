def busca_binaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1

minha_lista = [10, 20, 30, 40, 50, 60, 70, 80, 90]

numero_procurado = 70

resultado = busca_binaria(minha_lista, numero_procurado)

if resultado != -1:
    print(f"O número {numero_procurado} foi encontrado")
else:
    print(f"-1")