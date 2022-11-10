import numpy as np
import matplotlib.pyplot as plt

def factorial(N) : 
    if N == 0 : return 1
    elif N >= 1 : return factorial(N-1) * N

def probability(k, n, p) : 
    nCk = factorial(n) / (factorial(k)*factorial(n-k))
    return nCk * p**k * (1-p)**(n-k)

if __name__ == "__main__" : 
    pLi = [1/6, 2/6, 3/6]
    nLi = [20, 30, 40, 50]
    cLi = ["#f08080", "#66cdaa", "#4169e1"]

    fig, ax = plt.subplots(len(pLi),len(nLi))
    for i in range(len(pLi)) : 
        for j in range(len(nLi)) : 
            data = np.array([probability(k, nLi[j], pLi[i]) for k in range(nLi[j]+1)])
            ax[i,j].bar(list(range(nLi[j]+1)), data, color=cLi[i])

    plt.show()