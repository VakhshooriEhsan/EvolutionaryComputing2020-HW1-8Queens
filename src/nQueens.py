import bisect
import math
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

def Plt_board(mems):
    size = len(mems)
    yb = math.ceil(math.sqrt(size))
    xb = math.ceil(size/yb)
    n = len(mems[0])
    for i in range(size):
        plt.subplot(xb, yb, i+1)
        chessboard = zeros((n, n))
        chessboard[1::2,0::2] = 1
        chessboard[0::2,1::2] = 1
        plt.imshow(chessboard, cmap='binary')
        for j in range(n):
            x = j
            y = mems[i][j]
            plt.text(x, y, '♕', fontsize=40/xb, ha='center', va='center', color='black' if (x - y) % 2 == 0 else 'white')

# Variables initialisation:

n = 8 # number of queens | size of chessboard
m = 100 # number of population
num = 5 # number of select for parent selection
Rprob = 1.0 # Recombination probability
Mprob = 0.8 # Mutation probability
T = 10000 # Termination condition
data = [] # used for analyze


# Genetic-algorithm:

mems = Initialisation(m, n) # population initialisation
mems.sort(key=Fitness, reverse=True) # sort members by fitness
data += [mems.copy()]

while Fitness(mems[0]) < 1 and T > 0 :
    T -= 1
    parents = Parent_selection(mems, num)
    childs = Recombination(parents[0], parents[1], Rprob)
    childs[0] = Mutation(childs[0], Mprob)
    childs[1] = Mutation(childs[1], Mprob)
    Insert(mems, childs[0])
    Insert(mems, childs[1])
    data += [mems.copy()]


# Analyze:

maxFit = [] # max fitness
k = 10
avgFits = [] # avg of k-max fitness
l = len(data) # last result
t = 12 # number of result show

for i in range(l):
    maxFit += [Fitness(data[i][0])]
    tmp = 0
    for j in range(min(k, len(data[i]))):
        tmp += Fitness(data[i][j])
    avgFits += [tmp/k]

plt.figure(1)
Plt_board(data[l-1][:t])

plt.figure(2)
plt.subplot(2, 1, 1)
plt.plot(maxFit, '.-')
plt.title('Fitness Analyze')
plt.ylabel('Max Fitness')

plt.subplot(2, 1, 2)
plt.plot(avgFits, '.-')
plt.xlabel('Generations')
plt.ylabel('Avg of k-max Fitness')

plt.show()
