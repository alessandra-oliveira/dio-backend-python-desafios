# Entrada do usuário
email = input().strip().lower()

# TODO: Verifique as regras do e-mail:
def validar_email(email):
    if " " in email:
        print("E-mail inválido")
        return

    if email.count("@") == 1:
        parte1, parte2 = email.split("@")

        if len(parte1) > 0:
            if parte2 == "gmail.com" or parte2 == "outlook.com":
                print("E-mail válido")
            else:
                print("E-mail inválido")

        else:
            print("E-mail inválido")

    else:
        print("E-mail inválido")

validar_email(email)