class Pessoa():
    def __init__(self, nome, idade, genero, profissao) -> None:
        self.nome = nome
        self.genero = genero
        self. profissao = profissao
        self.idade = idade
        self.maioridade = None
    
    def pessoaCadastrada(self):
        return self.nome, self.idade, self.genero, self.profissao

    def verificaIdade(self):
        if self.idade >= 18:
            self.maioridade = 'Sim'
            return f'É maior de idade'
        else:
            self.maioridade = 'Não'
            return f'É menor de idade'
        
p1 = Pessoa('Diego', 18, 'Masculino', 'Programador')
print(p1.verificaIdade())
print(p1.pessoaCadastrada())