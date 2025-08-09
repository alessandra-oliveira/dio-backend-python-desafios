#Praticando Encapsulamento:
class ContaBancaria:
    def __init__(self, titular, saldo, senha):
        self.__titular = titular
        self.__saldo = saldo
        self.__senha = senha

    @property
    def titular(self):
        return self.__titular
    
    def depositar(self, valor):
        if valor <= 0:
            print("O valor de depósito não pode ser negativo.")
        self.__saldo += valor

    def sacar(self, valor, senha):
        if senha == self.__senha:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print("Valor não permitido para saque.")
        else:
            print("Senha incorreta.")
    
    def ver_saldo(self, senha):
        if senha == self.__senha:
            print(f"Saldo: R${self.__saldo:.2f}")
        else:
            print("Senha incorreta.")

    def alterar_senha(self, senha_atual, nova_senha):
        senha_atual = str(senha_atual)
        nova_senha = str(nova_senha)

        if senha_atual != self.__senha:
            print("Senha atual incorreta.")
            return
        
        if nova_senha == self.__senha:
            print("A nova senha não pode ser igual à senha atual.")
            return
        
        if len(nova_senha) < 4:
            print("A nova senha deve ter pelo menos 4 caracteres.")
            return
        
        if not nova_senha.isdigit():
            print("A nova senha deve conter apenas números.")
            return
        self.__senha = nova_senha
        print("Senha alterada com sucesso!")

c1 = ContaBancaria("Alessandra", 0, "1234")
print(c1.titular)
c1.depositar(200)
c1.sacar(50, "234") #Senha incorreta
c1.sacar(40, "1234")
c1.ver_saldo("1234")
c1.alterar_senha("1234", "32") #Inválido
c1.alterar_senha("1234", "5678")
