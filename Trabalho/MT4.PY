# Função para contar o número de ocorrências de um símbolo usando a máquina de Turing
def mt_contar_ocorrencias(fita, simbolo):
    # Verificando se o símbolo é válido
    if len(simbolo) != 1:
        return "Símbolo inválido"
    
    # Convertendo a fita em uma lista de caracteres
    fita = list(fita)
    
    # Inicializando as cabeças
    head_esquerda = 0
    head_direita = len(fita) - 1
    
    # Inicializando o contador de ocorrências
    contador = 0
    
    # Movendo a head_esquerda até o fim da fita
    while head_esquerda <= head_direita:
        if fita[head_esquerda] == simbolo:
            contador += 1  # Incrementa o contador quando encontra o símbolo
        head_esquerda += 1  # Move a cabeça para a direita
    
    return contador

# Testes
print(mt_contar_ocorrencias("aabbbaaa", "b"))  # 3
print(mt_contar_ocorrencias("1110010111", "1"))  # 6
print(mt_contar_ocorrencias("xyzxyzxyz", "z"))  # 3
