# Função para verificar se a string é composta apenas por 'a' usando a máquina de Turing
def mt_apenas_a(fita):
    # Convertendo a fita para lista de caracteres
    fita = list(fita)
    
    # Inicializando as cabeças
    head_esquerda = 0
    head_direita = len(fita) - 1
    
    # Inicializando o estado
    estado = "q0"  # Estado inicial
    
    while estado != "q_accept" and estado != "q_reject":
        # Lendo o símbolo na posição da cabeça esquerda
        simbolo = fita[head_esquerda] if head_esquerda < len(fita) else " "  # Se estiver fora da fita, considera "espaço"
        
        if estado == "q0":
            if simbolo == "a":  # Se o símbolo for 'a', move para a próxima posição
                head_esquerda += 1
            elif simbolo == " ":  # Se o símbolo for espaço, significa que a fita terminou corretamente
                estado = "q_accept"  # Aceita a entrada
            else:  # Se encontrar um símbolo diferente de 'a'
                estado = "q_reject"  # Rejeita a entrada
    
    return estado == "q_accept"  # Retorna se o estado final foi "q_accept"

# Testes
print(mt_apenas_a("aaaa"))  # True (apenas 'a')
print(mt_apenas_a("aab"))   # False (contém 'b')
print(mt_apenas_a("bbaaa")) # False (contém 'b')
