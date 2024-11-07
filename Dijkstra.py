import heapq

def alterar_prioridade(w, D, L):
    for i in range(len(D)):
        if D[i][1] == w:
            pos = i
            break
    D[pos] = (L[w], w)
    heapq._siftdown(D, 0, pos)
    return

def dijkstra(D, L, marca, custo, pai, n_out):
    while D:
        Lmin, v = heapq.heappop(D)  # tirar a raiz do heap
        marca[v] = 1
        for w in n_out[v]:
            if marca[w] == 0:
                if L[v] + custo[v][w] < L[w]:
                    L[w] = L[v] + custo[v][w]  # atualizar o valor de L[w]
                    alterar_prioridade(w, D, L)  # atualizar o heap
                    pai[w] = v
