from collections import deque

fila = deque()

def adicionar_cliente(nome):
    fila.append(nome)

def chamar_cliente():
    if fila:
        return fila.popleft()
    return "Fila vazia"

# uso
adicionar_cliente("João")
adicionar_cliente("Maria")
print(chamar_cliente())