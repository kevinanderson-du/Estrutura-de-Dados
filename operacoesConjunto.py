logica = ["Ana", "João", "Maria"]
estrutura = ["Maria", "Carlos", "Ana"]

set1 = set(logica)
set2 = set(estrutura)

print("Ambos:", set1 & set2)
print("Só lógica:", set1 - set2)