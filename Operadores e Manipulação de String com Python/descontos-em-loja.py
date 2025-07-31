# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = float(input().strip())
cupom = input().strip().upper()

if cupom in descontos:
    desconto = preco * descontos[cupom]
    preco_com_desconto = preco - desconto

    if descontos[cupom] > 0:
        percentual = int(descontos[cupom] * 100)
        print(f"{preco_com_desconto:.2f}")
    else:
        print(f"{preco:.2f}")

else:
    print("Cupom inválido.")
# TODO: Aplique o desconto se o cupom for válido: