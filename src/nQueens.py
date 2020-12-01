import bisect
from numpy import random
from numpy import zeros
import matplotlib.pyplot as plt

def Initialisation(n, m):
    mems = []
    for _ in range(n):
        mems += [random.permutation(m).tolist()]
    return mems

def Fitness(mem):
    penalty = 0
    size = len(mem)
    for i in range(size-1):
        for j in range(i+1, size):
            if mem[i]-i == mem[j]-j or mem[i]+i == mem[j]+j or mem[i] == mem[j]:
                penalty += 1
    return 1.0/(penalty+1)

def Parent_selection(mems, num):
    size = len(mems)
    nmems = []
    for i in random.permutation(size)[:num]:
        nmems += [mems[i]]
    nmems.sort(key=Fitness, reverse=True)
    return [nmems[0], nmems[1]]

def Recombination(mem1, mem2, prob):
    if(random.rand() > prob):
        return [mem1, mem2]
    size = len(mem1)
    p = random.randint(1, size)
    nmem1 = mem1[0:p]
    nmem2 = mem2[0:p]
    for i in range(size):
        if nmem1.count(mem2[i])==0:
            nmem1 += [mem2[i]]
        if nmem2.count(mem1[i])==0:
            nmem2 += [mem1[i]]
    return [nmem1, nmem2]

def Mutation(mem, prob):
    if(random.rand() > prob):
        return mem
    size = len(mem)
    p = random.permutation(size)[:2]
    mem[p[0]], mem[p[1]] = mem[p[1]], mem[p[0]]
    return mem

def Insert(mems, child):
    size = len(mems)
    cf = Fitness(child)
    for i in range(size):
        if Fitness(mems[i]) <= cf:
            mems.insert(i, child)
            mems.pop()
            break

def Plt_board(n, mem):
    chessboard = zeros((n, n))
    chessboard[1::2,0::2] = 1
    chessboard[0::2,1::2] = 1
    plt.figure(1)
    plt.imshow(chessboard, cmap='binary')
    for i in range(n):
        x = i
        y = mem[i]
        plt.text(x, y, '♕', fontsize=20, ha='center', va='center', color='black' if (x - y) % 2 == 0 else 'white')
    print(mem)


# Variables initialisation:

n = 8 # number of queens | size of chessboard
m = 100 # number of population
num = 5 # number of select for parent selection
Rprob = 1.0 # Recombination probability
Mprob = 0.8 # Mutation probability
T = 10000 # Termination condition


# Genetic-algorithm:

mems = Initialisation(m, n) # population initialisation
mems.sort(key=Fitness, reverse=True) # sort members by fitness
data = [Fitness(mems[0])] # used for Analyze

while Fitness(mems[0]) < 1 and T > 0 :
    T -= 1
    parents = Parent_selection(mems, num)
    childs = Recombination(parents[0], parents[1], Rprob)
    childs[0] = Mutation(childs[0], Mprob)
    childs[1] = Mutation(childs[1], Mprob)
    Insert(mems, childs[0])
    Insert(mems, childs[1])
    data += [Fitness(mems[0])]


# Analyze:

Plt_board(n, mems[0])

plt.figure(2)
plt.plot(data)
plt.ylabel('Fitness')
plt.xlabel('Generations')

plt.show()
