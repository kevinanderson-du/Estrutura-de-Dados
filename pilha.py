def verificar(expressao):
    pilha = []
    pares = {')': '(', ']': '[', '}': '{'}

    for char in expressao:
        if char in '([{':
            pilha.append(char)
        elif char in ')]}':
            if not pilha or pilha.pop() != pares[char]:
                return False

    return len(pilha) == 0

print(verificar("[(a+b)*{c-d}]"))  # True
print(verificar("([)]"))           # False