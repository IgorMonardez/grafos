Y_enum = ['A', 'B', 'C', 'D', 'E']

def desenho_continuo():

    T = int(input("T: "))

    for i in range(T):
        N = int(input("N: "))
        pontos = []
        for n in range(N):
            for z in range(2):
                ponto = input("Ponto:")

                pontos.append(ponto)

            print(pontos)

desenho_continuo()