import bisect
import math
import numpy as np
import matplotlib.pyplot as plt

def Initialisation(P, S, B):
    mems = np.zeros((P, B), dtype=int)
    for i in range(P):
        for j in range(B-1):
            mems[i][j] = np.random.randint(S-int(mems[i].sum())+1)
        mems[i][B-1] = S - int(mems[i].sum())
    return mems

def Fitness(mems, mem):
    score = 0.0
    P = len(mems)
    B = len(mem)
    for i in range(P):
        rival = mems[i]
        tmp=0
        for j in range(B):
            if(mem[j] > rival[j]):
                tmp += 1
            elif(mem[j] < rival[j]):
                tmp -= 1
        if(tmp>0):
            score += 1
    return score/P

def Tournament_selection(mems, k):
    P = len(mems)
    nmems = []
    for i in np.random.permutation(P)[:k]:
        nmems += [mems[i]]
    m0 = 0
    m1 = 1
    if(Fitness(mems, nmems[m0])<Fitness(mems, nmems[m1])):
        m0, m1 = m1, m0
    for i in range(2, k):
        if(Fitness(mems, nmems[m1])<Fitness(mems, nmems[i])):
            m1 = i
        if(Fitness(mems, nmems[m0])<Fitness(mems, nmems[m1])):
            m0, m1 = m1, m0
    for i in range(k):
        print(Fitness(mems, nmems[i]))
        print(nmems[i])
    return [nmems[m0], nmems[m1]]

def Recombination(mem1, mem2, prob):
    if(np.random.rand() > prob):
        return [mem1, mem2]
    size = len(mem1)
    p = np.random.randint(1, size)
    nmem1 = mem1[0:p]
    nmem2 = mem2[0:p]
    for i in range(size):
        if nmem1.count(mem2[i])==0:
            nmem1 += [mem2[i]]
        if nmem2.count(mem1[i])==0:
            nmem2 += [mem1[i]]
    return [nmem1, nmem2]

def Mutation(mem, prob):
    if(np.random.rand() > prob):
        return mem
    size = len(mem)
    p = np.random.permutation(size)[:2]
    mem[p[0]], mem[p[1]] = mem[p[1]], mem[p[0]]
    return mem

def Survival_selection(mems, child):
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
        chessboard = np.zeros((n, n))
        chessboard[1::2,0::2] = 1
        chessboard[0::2,1::2] = 1
        plt.imshow(chessboard, cmap='binary')
        for j in range(n):
            x = j
            y = mems[i][j]
            plt.text(x, y, '♕', fontsize=40/xb, ha='center', va='center', color='black' if (x - y) % 2 == 0 else 'white')

# Variables initialisation:

S = 20 # number of soldiers
B = 4 # number of battles
P = 50 # number of population
ELITISM = 0.1 # elitism probability

# n = 8 # number of queens | size of chessboard
# m = 100 # number of population
K = 5 # number of select for Tournament selection
# Rprob = 1.0 # Recombination probability
# Mprob = 0.8 # Mutation probability
# T = 10000 # Termination condition
# data = [] # used for analyze


# Genetic-algorithm:

mems = Initialisation(P, S, B) # population initialisation
# mems.sort(key=Fitness, reverse=True) # sort members by fitness
# data += [mems.copy()]

# while Fitness(mems[0]) < 1 and T > 0 :
#     T -= 1
parents = Tournament_selection(mems, K)
print(parents)
#     childs = Recombination(parents[0], parents[1], Rprob)
#     childs[0] = Mutation(childs[0], Mprob)
#     childs[1] = Mutation(childs[1], Mprob)
#     Survival_selection(mems, childs[0])
#     Survival_selection(mems, childs[1])
#     data += [mems.copy()]


# Analyze:

# maxFit = [] # max fitness
# k = 10
# avgFits = [] # avg of k-max fitness
# l = len(data) # last result
# t = 12 # number of result show

# for i in range(l):
#     maxFit += [Fitness(data[i][0])]
#     tmp = 0
#     for j in range(min(k, len(data[i]))):
#         tmp += Fitness(data[i][j])
#     avgFits += [tmp/k]

# plt.figure(1)
# Plt_board(data[l-1][:t])

# plt.figure(2)
# plt.subplot(2, 1, 1)
# plt.plot(maxFit, '.-')
# plt.title('Fitness Analyze')
# plt.ylabel('Max Fitness')

# plt.subplot(2, 1, 2)
# plt.plot(avgFits, '.-')
# plt.xlabel('Generations')
# plt.ylabel('Avg of k-max Fitness')

# plt.show()
