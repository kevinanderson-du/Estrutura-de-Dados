class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

    def inserir_final(self, valor):
        novo = No(valor)
        if not self.cabeca:
            self.cabeca = novo
            return
        atual = self.cabeca
        while atual.proximo:
            atual = atual.proximo
        atual.proximo = novo

    def reverter(self):
        anterior = None
        atual = self.cabeca
        while atual:
            proximo = atual.proximo
            atual.proximo = anterior
            anterior = atual
            atual = proximo
        self.cabeca = anterior