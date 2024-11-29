# Implementação de um "Autômato" para reconhecer palavras que terminam com "bab"
def mt_termina_com_bab(palavra):
    # Definindo os estados
    estado = "q0"  # Estado inicial

    # Percorrendo a palavra, caractere por caractere
    for simbolo in palavra:
        if estado == "q0":
            if simbolo == "b":
                estado = "q1"
            elif simbolo == "a":
                estado = "q0"  # Permanece no estado q0 se encontrar 'a'
            else:
                estado = "q_rejeitado"  # Caractere inválido, rejeita a palavra

        elif estado == "q1":
            if simbolo == "a":
                estado = "q2"
            elif simbolo == "b":
                estado = "q1"  # Permanece em q1 se encontrar 'b'
            else:
                estado = "q_rejeitado"  # Caractere inválido, rejeita a palavra

        elif estado == "q2":
            if simbolo == "b":
                estado = "q3"  # Se encontrar 'b' vai para o estado de aceitação
            elif simbolo == "a":
                estado = "q2"  # Permanece em q2 se encontrar 'a'
            else:
                estado = "q_rejeitado"  # Caractere inválido, rejeita a palavra

        elif estado == "q3":
            if simbolo == "b":
                estado = "q1"  # Se encontrar 'b', volta ao estado q1
            elif simbolo == "a":
                estado = "q2"  # Se encontrar 'a', vai para o estado q2
            else:
                estado = "q_rejeitado"  # Caractere inválido, rejeita a palavra

        if estado == "q_rejeitado":
            return False  # A palavra foi rejeitada

    # Aceita a palavra se terminou no estado final q3
    return estado == "q3"

# Testando com algumas palavras
if __name__ == "__main__":
    palavras = ["bab", "bbab", "aab", "babbab", "aaa", "bbbbab"]
    for palavra in palavras:
        if mt_termina_com_bab(palavra):
            print(f"A palavra '{palavra}' é aceita.")
        else:
            print(f"A palavra '{palavra}' não é aceita.")
