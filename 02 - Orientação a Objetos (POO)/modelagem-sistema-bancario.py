import textwrap
from datetime import datetime, date
import re
from abc import ABC, abstractmethod

# =============================
# CLASSE HISTORICO
# =============================
class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        })

    def exibir(self, saldo_atual=None):
        print("\n================ EXTRATO ================")
        if not self.transacoes:
            print("Sem movimentações.")
        else:
            for t in self.transacoes:
                print(f"{t['data']} - {t['tipo']}: R$ {t['valor']:.2f}")
        if saldo_atual is not None:
            print(f"\nSaldo atual: R$ {saldo_atual:.2f}")
        print("==========================================")

# =============================
# INTERFACE TRANSACAO
# =============================
class Transacao(ABC):
    def __init__(self, valor: float):
        self.valor = valor

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, novo_valor):
        if novo_valor <= 0:
            raise ValueError("O valor da transação deve ser positivo.")
        self._valor = novo_valor

    @abstractmethod
    def registrar(self, conta):
        pass

# =============================
# TRANSACOES CONCRETAS
# =============================
class Deposito(Transacao):
    def registrar(self, conta):
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)
            print("Depósito realizado com sucesso!")
        else:
            print("Falha no depósito.")

class Saque(Transacao):
    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)
            print("Saque realizado com sucesso!")
        else:
            print("Falha no saque.")

# =============================
# CLASSE CONTA
# =============================
class Conta:
    def __init__(self, saldo: float, numero: int, agencia: str, cliente):
        self.saldo = saldo
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        if not isinstance(saldo, (int, float)):
            raise ValueError("Saldo deve ser numérico.")
        if saldo < 0:
            raise ValueError("Saldo não pode ser negativo.")
        self._saldo = float(saldo)

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, numero):
        if not isinstance(numero, int):
            raise ValueError("O número deve ser um inteiro.")
        if numero <= 0:
            raise ValueError("Número da conta deve ser positivo.")
        self._numero = numero

    @property
    def agencia(self):
        return self._agencia

    @agencia.setter
    def agencia(self, agencia):
        if not isinstance(agencia, str):
            raise ValueError("Agência deve ser uma string.")
        if not re.match(r'^\d{4}-\d$', agencia):
            raise ValueError("Agência inválida. Formato esperado: [0000-x]")
        self._agencia = agencia

    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, cliente):
        from abc import ABCMeta
        if not hasattr(cliente, "contas"):
            raise ValueError("Cliente inválido. Deve ser uma instância de Cliente.")
        self._cliente = cliente

    def sacar(self, valor: float) -> bool:
        if valor <= 0:
            print("O valor do saque deve ser positivo.")
            return False
        if valor > self.saldo:
            print("Saldo insuficiente.")
            return False
        self._saldo -= valor
        return True

    def depositar(self, valor: float) -> bool:
        if valor <= 0:
            print("O valor do depósito deve ser positivo.")
            return False
        self._saldo += valor
        return True

    @classmethod
    def nova_conta(cls, cliente, numero: int, agencia: str):
        return cls(0.0, numero, agencia, cliente)

# =============================
# CLASSE CONTA CORRENTE
# =============================
class ContaCorrente(Conta):
    @classmethod
    def nova_conta(cls, cliente, numero, agencia, limite=500, limite_saques=3):
        return cls(0.0, numero, agencia, cliente, limite, limite_saques)

    def __init__(self, saldo, numero, agencia, cliente, limite=500, limite_saques=3):
        super().__init__(saldo, numero, agencia, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
        self.saques_realizados = 0

    def sacar(self, valor: float) -> bool:
        if self.saques_realizados >= self.limite_saques:
            print("Limite de saques diários atingido.")
            return False
        if valor > self.limite:
            print("Valor excede o limite por saque.")
            return False
        if super().sacar(valor):
            self.saques_realizados += 1
            return True
        return False

# =============================
# CLASSE CLIENTE E PESSOA FISICA
# =============================
class Cliente:
    def __init__(self, endereco: str):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao: Transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome: str, cpf: str, data_nascimento: str, endereco: str):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y").date()

# =============================
# FUNÇÕES AUXILIARES
# =============================
def mostrar_menu():
    menu = """
    Escolha uma opção:
    [d] Depositar     | [s] Sacar
    [e] Extrato       | [nu] Novo usuário
    [nc] Nova conta   | [lc] Listar contas
    [q] Sair
    => """
    return input(textwrap.dedent(menu)).strip().lower()

def encontrar_cliente(cpf, clientes):
    return next((c for c in clientes if getattr(c, "cpf", None) == cpf), None)

# =============================
# FLUXO PRINCIPAL
# =============================
def main():
    clientes = []
    contas = []
    agencia_padrao = "0001-1"

    while True:
        opcao = mostrar_menu()

        if opcao == "nu":
            nome = input("Nome: ")
            cpf = input("CPF: ")
            nasc = input("Data de nascimento (dd/mm/aaaa): ")
            endereco = input("Endereço: ")
            cliente = PessoaFisica(nome, cpf, nasc, endereco)
            clientes.append(cliente)
            print("Cliente criado com sucesso.")

        elif opcao == "nc":
            cpf = input("CPF do cliente: ")
            cliente = encontrar_cliente(cpf, clientes)
            if cliente:
                numero = len(contas) + 1
                conta = ContaCorrente.nova_conta(cliente, numero, agencia_padrao)
                cliente.adicionar_conta(conta)
                contas.append(conta)
                print("Conta criada com sucesso.")
            else:
                print("Cliente não encontrado.")

        elif opcao == "d":
            cpf = input("CPF do cliente: ")
            cliente = encontrar_cliente(cpf, clientes)
            if cliente and cliente.contas:
                valor = float(input("Valor do depósito: "))
                transacao = Deposito(valor)
                cliente.realizar_transacao(cliente.contas[0], transacao)
            else:
                print("Cliente ou conta não encontrado.")

        elif opcao == "s":
            cpf = input("CPF do cliente: ")
            cliente = encontrar_cliente(cpf, clientes)
            if cliente and cliente.contas:
                valor = float(input("Valor do saque: "))
                transacao = Saque(valor)
                cliente.realizar_transacao(cliente.contas[0], transacao)
            else:
                print("Cliente ou conta não encontrado.")

        elif opcao == "e":
            cpf = input("CPF do cliente: ")
            cliente = encontrar_cliente(cpf, clientes)
            if cliente and cliente.contas:
                conta = cliente.contas[0]
                conta.historico.exibir(saldo_atual=conta.saldo)
            else:
                print("Cliente ou conta não encontrado.")

        elif opcao == "lc":
            for conta in contas:
                print(f"Agência: {conta.agencia} | Conta: {conta.numero} | Cliente: {conta.cliente.nome}")

        elif opcao == "q":
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
