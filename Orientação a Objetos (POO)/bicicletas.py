class Bicicleta():
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Plim Plim")
    
    def parar(self):
        print("Parando a bicicleta...")
        print("Bicicleta parou!")

    def correr(self):
        print("Vrummmm...!")

    def __str__(self):
        return f"{self.__class__.__name__}: {", ".join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

b1 = Bicicleta("rosa", "caloi", 2021, 500)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.ano, b1.modelo, b1.valor)

b2 = Bicicleta("Lilás", "Monark", 2001, 600 )
print(b2)