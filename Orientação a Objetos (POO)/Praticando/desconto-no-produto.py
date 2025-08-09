#Praticando Métodos de Classe e Estáticos
class Produto:
    desconto = 0.10 #atributo da classe

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    #Método de classe: quando a função não precisa saber nada sobre a classe ou a instância.
    @classmethod
    def desconto_padrao(cls, valor):
        return valor * (1 - cls.desconto) #cálculo do desconto
    
    #Método estático: quando a função precisa saber algo sobre a classe (como atributos da classe ou criar objetos).
    @staticmethod
    def converter_para_dolar(valor_em_reais):
        cotacao = 5
        valor_em_dolar = valor_em_reais / cotacao
        return valor_em_dolar

produto1 = Produto("Shampoo", 15)
print(produto1.preco)
preco_com_desconto = produto1.desconto_padrao(produto1.preco)
print(f"Preço com desconto de {Produto.desconto * 100:.0f}% :{preco_com_desconto:.2f}")
preco_em_dolar = produto1.converter_para_dolar(produto1.preco)
print(f"O valor R${produto1.preco:.2f} em dólar é: ${preco_em_dolar:.2f}")