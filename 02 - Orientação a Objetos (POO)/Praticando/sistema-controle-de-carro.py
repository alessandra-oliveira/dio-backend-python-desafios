#Praticando o Encapsulamento:
class Carro:
    def __init__(self, marca, velocidade=0):
        self.marca = marca
        self._velocidade = min(velocidade, 200)
        self.__ligado = False

    #Getter para permitir o acesso ao estado do carro como se fosse um atributo comum, mesmo que na verdade ele seja um método
    @property
    def estado(self):
        return "Ligado" if self.__ligado else "Desligado"
    
    #Getter para permitir o acesso à velocidade:
    @property
    def velocidade(self):
        return self._velocidade
    
    #Setter para permitir a mudança do valor de velocidade:
    @velocidade.setter
    def velocidade(self, valor):
        if isinstance(valor, (int, float)) and valor >= 0:
            self._velocidade = valor
        else:
            raise ValueError("Velocidade deve ser um número positivo.")
    
    #Método para ligar o carro:
    def ligar(self):
        if not self.__ligado:
            self.__ligado = True
        else:
            print("Carro já está ligado.")

    #Método para desligar o carro:
    def desligar(self):
        if self.__ligado:
            self.__ligado = False
        else:
            print("Carro já está desligado.")

    #Método para acelerar o carro:
    def acelerar(self, valor):
        if self.__ligado:
            if valor > 0:
                if self._velocidade + valor <= 200:
                    self._velocidade += valor
                else:
                    print("Não é permitido acelerar mais que 200 km/h.")
                    print(f"Velocidade atual: {self._velocidade} km/h")
        else:
            print("O carro deve estar ligado para acelerar ser possível.")

    #Método para frear o carro:
    def frear(self, valor):
        if self.__ligado:
            if valor >= 0:
                self._velocidade = max(0, self._velocidade - valor)
            else:
                print("A velocidade não pode ser menor que zero.")
        else:
            print("O carro está desligado.")

c1 = Carro("gol", 200)
print(c1.estado)

c1.ligar()
print(c1.estado)

c1.acelerar(180)
print(c1.velocidade)

c1.acelerar(10)
c1.frear(50)
print(c1.velocidade)
