class Pedido:
    def __init__(self):
        self.itens = []  
    
    # Crie um método chamado adicionar_item que recebe um preço e adiciona à lista de itens:
    def adicionar_item(self, preco):
        #Adicione o preço do item à lista:
        self.itens.append(float(preco))

    #Crie um método chamado calcular_total que retorna a soma de todos os preços da lista:
    def calcular_total(self):
        soma = 0
        for item in self.itens:
            soma += item
        #Retorne a soma de todos os preços
        return soma

quantidade_pedidos = int(input().strip())

pedido = Pedido()

for _ in range(quantidade_pedidos):
    entrada = input().strip()
    nome, preco = entrada.rsplit(" ", 1)
    #Chame o método adicionar_item corretamente: 
    pedido.adicionar_item(preco)
#Exiba o total formatado com duas casas decimais:
total = pedido.calcular_total()
print(f"{total:.2f}")