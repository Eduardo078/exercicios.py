class Carro:
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0
    
    def acelerar(self):
        self.velocidade += 10
    
    def freiar(self):
        if self.velocidade >= 10:
            self.velocidade -= 10
        else:
            self.velocidade = 0

    def informacoes(self):
        print(f"Modelo: {self.modelo}, Ano: {self.ano}, Velocidade: {self.velocidade} km/h")

class Garagem:
    def __init__(self):
        self.carros = []

    def adicionar_carro(self, carro):
        self.carros.append(carro)

    def listar_carros(self):
        for carro in self.carros:
            carro.informacoes()

    def remover_carro(self, modelo):
        for carro in self.carros:
            if carro.modelo == modelo:
                self.carros.remove(carro)
                print(f"Carro '{modelo}' removido com sucesso.")
                return
        print(f"Carro '{modelo}' não encontrado.")

    def total_carros(self):
        total = len(self.carros)
        print(f"Total de carros na garagem: {total}")



carro1 = Carro("Fusca", 1980)
carro2 = Carro("Gol", 2005)

garagem = Garagem()

garagem.adicionar_carro(carro1)
garagem.adicionar_carro(carro2)

garagem.listar_carros()
garagem.total_carros()

carro1.acelerar()
carro1.acelerar()
carro1.freiar()

carro1.informacoes()

garagem.remover_carro("Gol")
garagem.listar_carros()
garagem.total_carros()
