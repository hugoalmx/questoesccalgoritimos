# MT para verificar se a palavra começa e termina com 'a'
def mt_comeca_termina_com_a(palavra):
    # Definindo os estados
    estado = "q0"  # Estado inicial

    if not palavra:
        return False  # Palavra vazia não pode começar e terminar com 'a'

    # Verificando o primeiro e o último símbolo da palavra
    for i, simbolo in enumerate(palavra):
        if estado == "q0":
            if i == 0:  # Primeira posição da palavra
                if simbolo == "a":
                    estado = "q1"  # Transita para o estado q1 após encontrar 'a' no início
                else:
                    estado = "q_rejeitado"  # Palavra não começa com 'a', rejeita
            else:
                if simbolo == "a":
                    estado = "q1"  # Continua em q1 ou vai para q2
                elif simbolo == "b":
                    estado = "q1"  # Permanece em q1 ao encontrar 'b'
                else:
                    estado = "q_rejeitado"  # Caractere inválido, rejeita a palavra
        elif estado == "q1":
            if simbolo == "a":
                estado = "q2"  # Transita para q2 quando encontra 'a'
            elif simbolo == "b":
                estado = "q1"  # Permanece em q1 ao encontrar 'b'
            else:
                estado = "q_rejeitado"  # Caractere inválido, rejeita a palavra
        elif estado == "q2":
            if simbolo == "a":
                estado = "q2"  # Permanece em q2 ao encontrar 'a'
            elif simbolo == "b":
                estado = "q2"  # Permanece em q2 ao encontrar 'b'
            else:
                estado = "q_rejeitado"  # Caractere inválido, rejeita a palavra
        
        if estado == "q_rejeitado":
            return False  # A palavra foi rejeitada

    # Aceita a palavra se o último caractere for 'a' (se o estado final for q2)
    return palavra[-1] == "a" and estado == "q2"

# Testando com algumas palavras
if __name__ == "__main__":
    palavras = ["aa", "abbaa", "aba", "b", "ba", "abb"]
    for palavra in palavras:
        if mt_comeca_termina_com_a(palavra):
            print(f"A palavra '{palavra}' é aceita.")
        else:
            print(f"A palavra '{palavra}' não é aceita.")
