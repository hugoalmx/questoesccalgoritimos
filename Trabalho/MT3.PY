# Função para verificar se um número binário é par usando a máquina de Turing
def mt_numero_par_binario(fita):
    # Verificando se a fita é válida (somente contém '0' e '1')
    if not fita.isdigit() or any(c not in "01" for c in fita):
        return "Fita inválida"
    
    # Convertendo a fita em uma lista de caracteres
    fita = list(fita)
    
    # Inicializando as cabeças
    head_esquerda = 0
    head_direita = len(fita) - 1
    
    # Movendo a cabeça da esquerda para a direita até o final da fita
    # Vamos apenas verificar o último símbolo
    while head_esquerda <= head_direita:
        if head_esquerda == head_direita:  # Se a cabeça atingir o último símbolo
            return fita[head_esquerda] == '0'  # Verifica se o último símbolo é '0'
        head_esquerda += 1  # Move a cabeça para a direita

# Testes
print(mt_numero_par_binario("110"))  # True (par)
print(mt_numero_par_binario("111"))  # False (ímpar)
print(mt_numero_par_binario("1010"))  # True (par)
