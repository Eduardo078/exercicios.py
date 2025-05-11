class Filme:
    def __init__(self, titulo, diretor, ano):
        self.titulo = titulo
        self.diretor = diretor
        self.ano = ano
    
    def informacoes(self):
        print(f"Titulo: {self.titulo}, Diretor: {self.diretor}, Ano: {self.ano}")

class Locadora:    
    def __init__(self):
        self.filmes = []
    
    def adicionar_filme(self, filme):
        self.filmes.append(filme)
    
    def listar_filme(self):
        for filme in self.filmes:
            filme.informacoes()
    
    def remover_filme(self, titulo):
        for filme in self.filmes:
            if filme.titulo == titulo:
                self.filmes.remove(filme)
                print(f"Filme '{titulo}' removido com sucesso.")
                return
        print(f"Filme '{titulo}' não encontrado.")
    
    def total_filme(self):
        total = len(self.filmes)
        print(f"Existem {total} filmes na locadora.")

locadora = Locadora()

filme1 = Filme("Gente grande 2", "Denis Dugan", 2013)
filme2 = Filme("Arremesso alto", "Jeremiah Zagar", 2022)

locadora.adicionar_filme(filme1)
locadora.adicionar_filme(filme2)

locadora.listar_filme()
locadora.total_filme()

locadora.remover_filme("Arremesso alto")
locadora.listar_filme()
locadora.total_filme()

           
    