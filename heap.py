import heapq

tarefas = []

def adicionar_tarefa(nome, prioridade):
    heapq.heappush(tarefas, (prioridade, nome))

def processar_tarefa():
    if tarefas:
        return heapq.heappop(tarefas)
    return "Sem tarefas"

# uso
adicionar_tarefa("Estudar", 2)
adicionar_tarefa("Dormir", 1)

print(processar_tarefa())