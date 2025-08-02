confirmadas = []
recusadas = []
indisponivel = []

def processar_reservas():
    # Entrada dos quartos disponíveis
    quartos_disponiveis = set(map(int, input().split()))
    
    # Entrada das reservas solicitadas
    reservas_solicitadas = list(map(int, input().split()))

    def verificar_reservas(quartos_disponiveis, reservas_solicitadas):
        for reserva in reservas_solicitadas:
            if reserva in quartos_disponiveis:
                confirmadas.append(reserva)
                quartos_disponiveis.remove(reserva)  # remove do conjunto para evitar duplicidade
            else:
                recusadas.append(reserva)
                
    verificar_reservas(quartos_disponiveis, reservas_solicitadas)

    # Saída dos resultados conforme especificação
    print("Reservas confirmadas:", " ".join(map(str, confirmadas)))
    print("Reservas recusadas:", " ".join(map(str, recusadas)))

# Chamada da função principal
processar_reservas()
