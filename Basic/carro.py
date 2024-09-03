class Carro:
    def __init__(self, marca, cor):
        self.marca = marca
        self.cor = cor
        self.situacao = False

    def ligarCarro(self):
        if self.situacao:
            print('carro já está ligado')
        else:
            self.situacao = True
            print('carro ligou')
    
    def desligarCarro(self):
        if not(self.situacao):
            print('carro já está desligado')
        else:
            self.situacao = False
            print('carro desligou')