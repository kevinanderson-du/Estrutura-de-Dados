class Historico:
    def __init__(self):
        self.pilha = []

    def visitar_pagina(self, url):
        self.pilha.append(url)

    def voltar(self):
        if self.pilha:
            return self.pilha.pop()
        return "Nenhuma página no histórico"

# uso
h = Historico()
h.visitar_pagina("google.com")
h.visitar_pagina("youtube.com")
print(h.voltar())