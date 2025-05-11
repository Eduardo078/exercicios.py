class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.__preco = preco

    def informacoes(self):
        print(f"Nome: {self.nome}, Preço: {self.get_preco()}")

    def get_preco(self):
        return self.__preco
    
    def set_preco(self, novo_preco):
        if novo_preco >= 0:
            self.__preco = novo_preco
        else:
        # "Levanta" um erro, ou seja, faz o programa parar e mostrar a mensagem
            raise ValueError(f"Preço inválido: {novo_preco}. O preço precisa ser maior ou igual a zero.")


produto1 = Produto("Mouse Gamer", 150)

produto1.informacoes()  

produto1.set_preco(120)  
produto1.informacoes()

produto1.set_preco(-50)  


