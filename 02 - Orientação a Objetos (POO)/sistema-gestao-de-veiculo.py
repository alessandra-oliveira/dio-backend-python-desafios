from datetime import datetime

# Crie a Classe Veiculo e armazene sua marca, modelo e ano como atributos
class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    # Método para verificar a antiguidade do veículo
    def verificar_antiguidade(self):
        ano_atual = datetime.now().year
        diferenca = ano_atual - self.ano
        if diferenca > 20:
            print("Veículo antigo")
        else:
            print("Veículo novo")

# Entrada direta
marca = input("Digite a marca: ").strip()
modelo = input("Digite o modelo: ").strip()
ano = int(input("Digite o ano: ").strip())

# Instanciando o objeto e verificando a antiguidade
veiculo = Veiculo(marca, modelo, ano)
veiculo.verificar_antiguidade()
