class Passaro:
    def voar(self):
        print("Voando...")

class Pardal(Passaro):
    def voar(self):
        super().voar()
    
class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar.")

class Aviao(Passaro):
    def voar(self):
        print("Avião está decolando...")

def plano_voo(obj):
    obj.voar()

pardal = Pardal()
avestruz = Avestruz()
plano_voo(pardal)
plano_voo(avestruz)
plano_voo(Aviao()) #passando a instância