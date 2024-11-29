# MT para verificar se a palavra tem comprimento par
def mt_comprimento_par(palavra):
    # Definindo os estados
    estado = "q0"  # Estado inicial

    # Percorrendo a palavra, caractere por caractere
    for simbolo in palavra:
        if estado == "q0":
            if simbolo == "a" or simbolo == "b":
                estado = "q1"  # Transita para o estado q1 quando encontra qualquer caractere
            else:
                estado = "q_rejeitado"  # Caractere inválido, rejeita a palavra
        elif estado == "q1":
            if simbolo == "a" or simbolo == "b":
                estado = "q0"  # Transita de volta para o estado q0 quando encontra outro caractere
            else:
                estado = "q_rejeitado"  # Caractere inválido, rejeita a palavra
        
        if estado == "q_rejeitado":
            return False  # A palavra foi rejeitada se um caractere inválido for encontrado

    # Aceita a palavra se o comprimento for par (se o estado final for q0)
    return estado == "q0"

# Testando com algumas palavras
if __name__ == "__main__":
    palavras = ["aa", "ab", "abc", "aabb", "abab", "aabbb"]
    for palavra in palavras:
        if mt_comprimento_par(palavra):
            print(f"A palavra '{palavra}' é aceita.")
        else:
            print(f"A palavra '{palavra}' não é aceita.")
