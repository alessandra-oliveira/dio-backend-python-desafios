import textwrap
from datetime import datetime

def criar_endereco_formatado():
    logradouro = input("Logradouro: ").strip().title()

    try:
        numero = int(input("Número: "))   
    except ValueError:
        print("-- Entrada inválida, digite apenas números. --")
        return None

    bairro = input("Bairro: ").strip().title()
    cidade = input("Cidade: ").strip().title()
    uf = input("UF/Sigla do Estado: ").strip().upper()

    return f"{logradouro}, {numero}, {bairro}, {cidade}/{uf}"

def criar_data_formatada():
    nascimento = input("Nascimento [dd/mm/aaaa]: ").strip()
    try:
        nascimento = datetime.strptime(nascimento, "%d/%m/%Y")
        return nascimento.strftime("%d/%m/%Y")
    except ValueError:
        print("Data inválida.")
        return None

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n-- Valor inválido para depósito. --")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("\n-- Saldo insuficiente. --")
    elif valor > limite:
        print("\n-- Valor excede o limite por saque. --")
    elif numero_saques >= limite_saques:
        print("\n-- Número máximo de saques excedido. --")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")
    else:
        print("\n-- Valor inválido. --")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Sem movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

def filtrar_usuario(cpf, usuarios):
    return next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ").strip()
    if filtrar_usuario(cpf, usuarios):
        print("\nUsuário já cadastrado.")
        return

    nome = input("Nome completo: ").strip().title()
    nascimento = criar_data_formatada()
    if not nascimento:
        return

    endereco = criar_endereco_formatado()
    if not endereco:
        return

    usuarios.append({
        "nome": nome,
        "nascimento": nascimento,
        "cpf": cpf,
        "endereco": endereco
    })

    print("\n=== Usuário criado com sucesso! ===")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("CPF do usuário: ").strip()
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario
        }

    print("\n-- Usuário não encontrado. --")
    return None

def listar_contas(contas):
    for conta in contas:
        linha = f"""
        Agência:\t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 50)
        print(textwrap.dedent(linha))

def main():
    AGENCIA = "0001" #constante
    LIMITE_SAQUES = 3
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("Saindo do sistema...")
            break

        else:
            print("\n-- Opção inválida. Tente novamente. --")

main()
