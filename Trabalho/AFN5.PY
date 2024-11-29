# MT para verificar se um número binário é par usando a lógica de estados
def mt_numero_par_binario(fita):
    pos = 0
    estado = "q0"  # Estado inicial
    
    while estado != "q_accept" and estado != "q_reject":
        simbolo = fita[pos] if pos < len(fita) else " "  # Lê o símbolo na posição atual
        
        if estado == "q0":  # Estado inicial
            if simbolo == "0":  # Se o símbolo for '0', aceitamos o número como par
                estado = "q_accept"  # Aceita a entrada
            elif simbolo == "1":  # Se o símbolo for '1', move-se para o próximo dígito
                pos += 1
            elif simbolo == " ":  # Se for espaço, a fita está vazia (não há números)
                estado = "q_reject"  # Rejeita a entrada, pois não há dígitos binários
        elif estado == "q_accept":  # Se aceitou, finaliza
            return True
        elif estado == "q_reject":  # Se rejeitou, finaliza
            return False

    return estado == "q_accept"  # Retorna se o estado final for "q_accept"

# Testes
print(mt_numero_par_binario("110"))  # True (par)
print(mt_numero_par_binario("111"))  # False (ímpar)
print(mt_numero_par_binario("1010"))  # True (par)
