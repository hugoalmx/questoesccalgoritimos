 # Implementação de um AFN para reconhecer palavras que contêm "ab" ou "ba"
class AFN:
    def __init__(self):
        # Definindo o estado inicial e os estados de aceitação
        self.start_state = 'q0'
        self.accept_states = {'q2', 'q4'}

    def process(self, palavra):
        # Definindo o estado inicial como q0
        estado = 'q0'

        if not palavra:  # Se a palavra for vazia, rejeitamos
            return estado in self.accept_states

        # Processando a palavra caractere por caractere
        for caractere in palavra:
            if estado == 'q0':
                if caractere == 'a':
                    estado = 'q1'  # Transição de q0 para q1 com 'a'
                elif caractere == 'b':
                    estado = 'q3'  # Transição de q0 para q3 com 'b'
                else:
                    estado = 'q_rejeitado'  # Caractere inválido, rejeita a palavra
            elif estado == 'q1':
                if caractere == 'b':
                    estado = 'q2'  # Transição de q1 para q2 com 'b'
                else:
                    estado = 'q_rejeitado'  # Caractere inválido, rejeita a palavra
            elif estado == 'q3':
                if caractere == 'a':
                    estado = 'q4'  # Transição de q3 para q4 com 'a'
                else:
                    estado = 'q_rejeitado'  # Caractere inválido, rejeita a palavra
            else:
                estado = 'q_rejeitado'  # Se o estado for inválido, rejeita a palavra

            # Se algum estado inválido for atingido, a palavra é rejeitada
            if estado == 'q_rejeitado':
                return False

        # A palavra é aceita se o estado final for um estado de aceitação
        return estado in self.accept_states

# Testando o autômato
if __name__ == "__main__":
    afn = AFN()

    palavras = ["ab", "ba", "aa", "bbb", "bbaa", "banana"] 
    for palavra in palavras:
        if afn.process(palavra):
            print(f"A palavra '{palavra}' é aceita.")
        else:
            print(f"A palavra '{palavra}' não é aceita.")
