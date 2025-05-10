class Turma:
    def __init__(self):
        self.alunos = []

    def adicionar_aluno(self, nome):
        self.alunos.append(nome)

    def listar_alunos(self):
        for aluno in self.alunos:
            print(f"Nome: {aluno.nome}, idade:{aluno.idade} anos")

    def total_de_alunos(self):
        total = len(self.alunos)
        print(f"total de alunos na turma: {total}")

    def remover_aluno(self, nome):
        for aluno in self.alunos:
            if aluno.nome == nome:
                self.alunos.remove(aluno)
                print(f"Aluno {nome} removido da turma.")
                return
        print(f"Aluno {nome} não encontrado na turma.")

        


class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


turma1 = Turma()

aluno1 = Aluno("Eduardo", 16)
aluno2 = Aluno("Theo", 16)
aluno3 = Aluno("Isaque", 16)

turma1.adicionar_aluno(aluno1)
turma1.adicionar_aluno(aluno2)
turma1.adicionar_aluno(aluno3)

turma1.remover_aluno("Eduardo")

turma1.listar_alunos()
