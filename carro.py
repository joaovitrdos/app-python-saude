class Carro:
    def __init__(self,modelo,marca,ano,cor, desligar, ligar):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.cor = cor
        self.velocidade = 123
        self.desligar = True
        self.ligar = True

    def ligar(self,):
        self.ligar = True
        print("O carro está ligado.")

    def desligar(self, ):
        self.desligar = True
        print("O carro está desligado.")

    def acelerar (self, icremento):
        self.velocidade += icremento
        print(f"O caroo do modelo {self.modelo} foi acelerado {self.velocidade} Km/h")

    def frear(self, decremento):
        self.velocidade -= decremento
        print(f"O carro do modelo {self.modelo} foi frear {self.velocidade} Km/h")

    def pintar(self, nova_cor):
        self.cor = nova_cor
        print(f"O carro do modelo {self.modelo} foi pintado {self.cor}")

object1 = Carro (marca ="Toyata", modelo = "Corrola", ano = 2015, cor = "Azul", desligar = True, ligar = False)
object2 = Carro ( marca = "BMW", modelo = "I5", ano = 2021, cor = "Branco", desligar = False, ligar = True)

print(f"Carro: marca {object1.marca}, modelo {object1.modelo}, ano {object1.ano}, cor {object1.cor}, {object1.velocidade} Km/h")