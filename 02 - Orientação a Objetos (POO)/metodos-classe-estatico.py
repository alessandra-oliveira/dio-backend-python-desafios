class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod #diz que o método pertence à classe, não à instância.
    def criar_apartir_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2025 - ano
        return cls(nome, idade)
    
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18
    
#p = Pessoa("Alessandra", 21)
p = Pessoa.criar_apartir_data_nascimento(2004, 7, 17, "Alessandra")
print(p.nome, p.idade)
print(Pessoa.e_maior_idade(21))