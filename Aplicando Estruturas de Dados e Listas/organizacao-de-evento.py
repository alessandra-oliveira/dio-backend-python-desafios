# Dicionário para agrupar participantes por tema
eventos = {}

# Entrada do número de participantes
n = int(input().strip())

# TODO: Crie um loop para armazenar participantes e seus temas:
for _ in range(n):
    linha = input().strip().title()
    posicao_virgula = linha.rfind(",")

    pessoa = linha[:posicao_virgula].strip()
    tema = linha[posicao_virgula + 1:].strip()

    if not tema in eventos:
        eventos[tema] = []

    if not pessoa in eventos[tema]:
        eventos[tema].append(pessoa)

# Exibe os grupos organizados
for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")