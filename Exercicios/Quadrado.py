"""
Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
"""

class Quadrado:
    def __init__(self, tamanho, lado) -> None:
        self.tamanho = tamanho
        self.lado = lado
        print('Objeto criado com sucesso!')
    
    def setValueLado(self, lado):
        self.lado = lado
    
    def getValueLado(self):
        return self.lado
    
    def calcArea(self):
        return self.lado * self.tamanho

        
q1 = Quadrado(tamanho= 10, lado= 5)
print(q1.getValueLado())
q1.setValueLado(10)
print(q1.getValueLado())
print(q1.calcArea())