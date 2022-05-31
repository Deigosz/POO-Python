class Cubo:
    def __init__(self, valor):
        self.valor = valor

    def pegaValor(self):
        return f'Valor Criado: {self.valor}'

    def CalculaCubo(self):
        self.cubo = self.valor * self.valor * self.valor
        return f'O valor do cubo do número {self.valor} é: {self.cubo}' 
        
    def MudaNumero(self, valor):
        self.valor = valor

a = Cubo(6)
print(a.pegaValor())
print(a.CalculaCubo())
a.MudaNumero(15)
print(a.CalculaCubo())
