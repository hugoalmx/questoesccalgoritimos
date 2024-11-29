# Função para multiplicar dois números inteiros usando a máquina de Turing
def mt_multiplicar_numeros(fita):
    # Verificando se o formato da fita está correto (contém o caractere '#')
    if '#' not in fita:
        return "Formato inválido"
    
    # Convertendo a fita em uma lista de caracteres
    fita = list(fita)
    
    # Inicializando as cabeças
    head_esquerda = 0
    head_direita = len(fita) - 1
    
    # Movendo a cabeça esquerda até encontrar o símbolo '#'
    while fita[head_esquerda] != '#':
        head_esquerda += 1
    
    # Movendo a cabeça direita até o final da fita
    while fita[head_direita] != '#':
        head_direita -= 1
    
    # Extraindo os números da fita (antes e depois do '#')
    num1_str = ''.join(fita[:head_esquerda])
    num2_str = ''.join(fita[head_esquerda + 1:])
    
    # Verificando se as partes extraídas são números válidos
    try:
        num1 = int(num1_str)
        num2 = int(num2_str)
    except ValueError:
        return "Entrada inválida"
    
    # Realizando a multiplicação
    produto = num1 * num2
    return str(produto)

# Testes
print(mt_multiplicar_numeros("3#4"))  # Resultado esperado: "12"
print(mt_multiplicar_numeros("5#6"))  # Resultado esperado: "30"
