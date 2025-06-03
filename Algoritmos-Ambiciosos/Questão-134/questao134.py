from typing import List

class Solucao:
    def pode_completar_circuito(self, combustivel: List[int], custo: List[int]) -> int:
        tanque_total = 0      # Soma total de combustível disponível menos o custo total
        tanque_atual = 0      # Combustível no tanque durante a simulação
        posto_inicio = 0      # Índice do posto candidato para começar a viagem

        for i in range(len(combustivel)):
            ganho = combustivel[i] - custo[i]  # Ganho líquido de combustível nesse trecho
            tanque_total += ganho
            tanque_atual += ganho

            # Se o tanque atual ficar negativo, não dá para sair do posto_inicio até aqui
            if tanque_atual < 0:
                posto_inicio = i + 1   # Próximo posto passa a ser o novo candidato
                tanque_atual = 0       # Zeramos o tanque para recomeçar o cálculo

        # Se o total for positivo, é possível completar a volta
        return posto_inicio if tanque_total >= 0 else -1


# --- Parte interativa para o terminal ---

def ler_lista(mensagem):
    return list(map(int, input(mensagem).strip().split()))

if __name__ == "__main__":
    print("Digite os valores de combustível disponíveis em cada posto (separados por espaço):")
    combustivel = ler_lista("combustível: ")

    print("Digite os custos de combustível para ir de cada posto ao próximo (separados por espaço):")
    custo = ler_lista("custo: ")

    solucao = Solucao()
    resultado = solucao.pode_completar_circuito(combustivel, custo)

    if resultado == -1:
        print("Não é possível completar a volta no circuito partindo de nenhum posto.")
    else:
        print(f"É possível completar a volta começando no posto de índice {resultado}.")
