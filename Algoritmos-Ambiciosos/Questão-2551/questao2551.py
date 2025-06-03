import heapq

def put_marbles(weights, k):
    # Se só podemos usar 1 saco, então todos os pesos vão no mesmo saco
    # Não há cortes, então o score máximo e mínimo são iguais => diferença é 0
    if k == 1:
        return 0

    # Etapa 1: calcular os "valores de corte" possíveis
    # Cada corte entre i e i+1 cria dois grupos com extremos weights[i] e weights[i+1]
    # O impacto desse corte no score total é dado por weights[i] + weights[i + 1]
    cortes = []
    for i in range(len(weights) - 1):
        soma = weights[i] + weights[i + 1]
        cortes.append(soma)

    # Etapa 2: escolher os (k - 1) maiores cortes
    # Esses cortes criam os grupos com maiores somas nos extremos => score máximo
    maiores = heapq.nlargest(k - 1, cortes)

    # Etapa 3: escolher os (k - 1) menores cortes
    # Esses cortes criam os grupos com menores somas nos extremos => score mínimo
    menores = heapq.nsmallest(k - 1, cortes)

    # Etapa 4: retornar a diferença entre o score máximo e mínimo possível
    return sum(maiores) - sum(menores)


# Parte interativa para execução no terminal
if __name__ == "__main__":
    print("Digite os pesos das bolinhas separados por espaço:")
    entrada = input().strip()
    weights = list(map(int, entrada.split()))

    print("Digite o número de sacos (k):")
    k = int(input())

    resultado = put_marbles(weights, k)
    print(f"\nA diferença entre o score máximo e o mínimo é: {resultado}")
