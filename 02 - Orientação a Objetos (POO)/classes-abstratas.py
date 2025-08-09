from abc import ABC, abstractmethod

class ControleRemoto(ABC): #quando uma classe se torna abstrata, ela não pode mais ser instanciada diretamente
    @abstractmethod
    def ligar(self):
        pass

    def desligar(self):
        pass

    @property
    @abstractmethod
    def marca(self):
        pass

class ControleTV(ControleRemoto): #qualquer classe que herdar de ControleRemoto será obrigada a implementar os métodos definidos ali
    def ligar(self):
        print("Ligando a TV...")

    def desligar(self):
        print("Desligando a TV...")

    @property
    def marca(self):
        return "LG"

class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o Ar Condicionado...")

    def desligar(self):
        print("Desligando o Ar Condicionado...")
    
    @property
    def marca(self):
        return "LG"

controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)

controle2 = ControleArCondicionado()
controle2.ligar()
controle2.desligar()
print(controle2.marca)