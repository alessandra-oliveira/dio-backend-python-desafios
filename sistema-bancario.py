menu = """
-- Sistema Bancário --

Opções:
[d] - Depositar
[s] - Sacar
[e] - Extrato
[q] - Sair do sistema
"""
conta_saldo = 0
depositos = []
saques = []
quantidade_saldo = 0

while True:
    opcao = input(menu).lower().strip()

    if opcao == "d":
        print("Opção escolhida: Depósito")
        valor = float(input("Valor: "))
        if valor <= 0:
            print("O valor do depósito não pode ser zero e não pode ser negativo. Por favor, digite um valor válido.")
            continue
        conta_saldo += valor
        depositos.append(valor)
        print(f"O depósito de R${valor:.2f} foi concluído com sucesso!")

    elif opcao == "s":
        print("Opção escolhida: Saque")

        if quantidade_saldo == 3:
            print("Limite diário de saque extraviado.")
            continue

        print(f"Seu saldo atual: R${conta_saldo:.2f}")

        if conta_saldo <= 0:
            print("Não é possível realizar o saque pois o seu saldo atualmente está negativo.")
            continue

        valor = float(input("Valor: "))
        if valor > 500:
            print("Não é possível realizar saques maiores que R$500.00")
            continue
        if valor <= 0:
            print("O valor do saque não pode ser zero e não pode ser negativo. Por favor, digite um valor válido.")
            continue
        conta_saldo -= valor
        quantidade_saldo += 1
        print(f"O saque de R${valor:.2f} foi concluído com sucesso!")
        saques.append(valor)

    elif opcao == "e":
        print("Opção escolhida: Extrato")
        print("-- Extrato da conta --")

        if depositos:
            print("-- Depósitos --")
            for i, deposito in enumerate(depositos):
                print(f"{i+1} - Deposito de R${deposito:.2f}")
        else:
            print("Nenhum deposito foi feito.")

        if saques:
            print("-- Saques --")
            for i, saque in enumerate(saques):
                print(f"{i + 1} - Saque de R${saque:.2f}")
        else:
            print("Nenhum saque foi feito.")

        print(f"Saldo atual da conta: {conta_saldo:.2f}")

    elif opcao == "q":
        print("Saindo do Sistema Bancário...")
        break

    else:
        print("Opção inválida, digite apenas uma opção fornecida anteriormente.")
        continue