# Entrada do número de pacientes
n = int(input().strip())

# Listas para armazenar pacientes por categoria
pacientes = []
urgentes = []
idosos = []
normal = []

# Coleta de dados dos pacientes
for _ in range(n):
    nome, idade, status = input().strip().split(", ")
    idade = int(idade)
    paciente = [nome.title(), idade, status.lower()]
    pacientes.append(paciente)

# Ordena pacientes por prioridade: urgente > idosos > demais
def organiza_pacientes():
    for paciente in pacientes:
        nome, idade, prioridade = paciente
        
        if prioridade == "urgente":
            urgentes.append(paciente)
        elif idade >= 60:
            idosos.append(paciente)
        else:
            normal.append(paciente)

    # Dentro dos urgentes, ordenar idosos primeiro e mais velhos antes
    urgentes.sort(key=lambda p: (p[1] < 60, -p[1]))

# Chamada da função para classificar os pacientes
organiza_pacientes()

# Fila final unida em ordem de prioridade
fila_final = urgentes + idosos + normal

# Saída formatada da ordem de atendimento
print("Ordem de Atendimento:", end=" ")
print(", ".join([p[0] for p in fila_final]))
