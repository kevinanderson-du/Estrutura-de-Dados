class TabelaHash:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]

    def hash(self, chave):
        return chave % self.tamanho

    def inserir(self, chave, valor):
        indice = self.hash(chave)
        self.tabela[indice].append((chave, valor))

    def buscar(self, chave):
        indice = self.hash(chave)
        for k, v in self.tabela[indice]:
            if k == chave:
                return v
        return None