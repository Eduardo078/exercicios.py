class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
    
    def informacoes(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}, Ano: {self.ano}")

class Biblioteca:
    def __init__(self):
        self.livros = []  

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        for livro in self.livros:
            livro.informacoes()


    def remover_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo: 
                self.livros.remove(livro)  
                print(f"Livro '{titulo}' removido com sucesso.")
                return
        print(f"Livro '{titulo}' não encontrado na biblioteca.")

        

    def total_de_livros(self):
        total = len(self.livros) 
        print(f"Total de livros na biblioteca: {total}")

biblioteca = Biblioteca()

livro1 = Livro("Dom Casmurro", "Machado de Assis", 1899)
livro2 = Livro("Dom Quixote", "Miguel de Cervantes", 1605)
livro3 = Livro("Menino do pijama listrado", "John Boyne", 2006)

biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)

biblioteca.listar_livros()
biblioteca.total_de_livros()

biblioteca.remover_livro("Dom Quixote")
biblioteca.listar_livros()
biblioteca.total_de_livros()



