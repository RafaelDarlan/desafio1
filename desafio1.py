nome_restaurante = input("Digite o nome do restaurante: ")
tempo_entrega = int(input("Digite o tempo de entrega: "))

def tempo_estimado_entrega(nome_restaurante, tempo_entrega):
    return f"O restaurante {nome_restaurante} entrega em {tempo_entrega} minutos."
    
print(tempo_estimado_entrega(nome_restaurante, tempo_entrega))