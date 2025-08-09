class Conta:
    def __init__(self, nro_agencia, saldo =0):
        self._saldo = saldo
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    def mostrar_saldo(self):
        return self._saldo


conta = Conta("0002", 100)
conta.depositar(100)
print(conta.nro_agencia)
print(conta.mostrar_saldo())

#Outro exemplo:
class A:
   a = 1 # atributo publico
   __b = 2 # atributo privado a class A

class B(A):
   __c = 3 # atributo privado a B

   def __init__(self):
     print(self.a)
     print(self.__c)

a = A()
print(a.a) # imprime 1

b = B()