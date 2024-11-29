# Função para subtrair dois números usando a máquina de Turing
def mt_subtrair_numeros(fita):
    # Convertendo o parâmetro fita em uma lista de caracteres
    fita = list(fita)
    
    # Inicializando as posições das cabeças (esquerda e direita)
    head_esquerda = 0
    head_direita = len(fita) - 1
    
    # Verificando se o formato é válido, ou seja, deve ter um "#"
    if '#' not in fita:
        return "Formato inválido"
    
    # Movendo a head_esquerda até encontrar o primeiro número (antes do '#')
    while fita[head_esquerda] != '#':
        head_esquerda += 1
    
    # Movendo a head_direita até encontrar o segundo número (depois do '#')
    while fita[head_direita] != '#':
        head_direita -= 1
    
    # Separando os números antes e depois do "#"
    try:
        num1 = int(''.join(fita[:head_esquerda]))
        num2 = int(''.join(fita[head_esquerda + 1:]))
    except ValueError:
        return "Entrada inválida"
    
    # Realizando a subtração
    resultado = num1 - num2
    return resultado

# Testes
print(mt_subtrair_numeros("10#3"))     # 7
print(mt_subtrair_numeros("7#10"))     # -3
print(mt_subtrair_numeros("15#5"))     # 10
print(mt_subtrair_numeros("-5#-3"))    # -2
print(mt_subtrair_numeros("0#-10"))    # 10
print(mt_subtrair_numeros("-10#20"))   # -30
