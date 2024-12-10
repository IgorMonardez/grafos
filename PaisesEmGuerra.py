import heapq
import Dijkstra
INFTY = 99999999


def alterar_prioridade(w, D, L):
    pos = 0
    for i in range(len(D)):
        if D[i][1] == w:
            pos = i
            break
    D[pos] = (L[w], w)
    heapq._siftdown(D, 0, pos)
    return


def pega_dupla():
    entrada = input()
    entrada = tuple(entrada.split())
    entrada = (int(entrada[0]), int(entrada[1]))
    return entrada


def pega_tripla(custos, n_out):
    x, y, h = input().split()
    x = int(x) - 1
    y = int(y) - 1
    h = int(h)
    custos[x][y] = h
    n_out[x].append(y)
    return x, y, h


def define_custos(n, e):
    custo = []
    for i in range(n):
        linha = []
        for j in range(n):
            if i == j:
                linha.append(0)
            else:
                linha.append(INFTY)
        custo.append(linha)
    return custo


def metodo_dijkstra(D, marca, n_out, L, pai, custos):
    while D:
        Lmin, v = heapq.heappop(D)  # tirar a raiz do heap
        marca[v] = 1
        for w in n_out[v]:
            if marca[w] == 0:
                if L[v] + custos[v][w] < L[w]:
                    L[w] = L[v] + custos[v][w]  # atualizar o valor de L[w]
                    alterar_prioridade(w, D, L)  # atualizar o heap
                    pai[w] = v

    return L



def calcula_tempo(n, lista_cartas, n_out, custos):
    for carta in lista_cartas:
        marca = n * [0]
        L = n * [INFTY]
        raiz = carta[0] - 1
        fim = carta[1] - 1
        L[raiz] = 0
        D = []
        for w in range(n):
            heapq.heappush(D, (L[w], w))
        pai = n * [-1]
        L = metodo_dijkstra(D, marca, n_out, L, pai, custos)

        if L[fim] == INFTY:
            print("Nao e possivel entregar a carta")    
        else:
            print(L[fim])



def paises_em_guerra():
    n, e = pega_dupla()
    while (n, e) != (0, 0):
        x_y_h = []
        custos = define_custos(n, e)
        n_out = [[] * n for i in range(n)]
        for i in range(e):
            x_y_h.append(pega_tripla(custos, n_out))

        k = int(input())
        lista_cartas = []
        for i in range(k):
            raiz, fim = pega_dupla()
            lista_cartas.append((raiz, fim))

        calcula_tempo(n, lista_cartas, n_out, custos)
        print()
        n, e = pega_dupla()


if __name__ == '__main__':
    paises_em_guerra()
