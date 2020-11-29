from numpy import random

def Initialisation(n, m):
    mems = []
    for _ in range(n):
        mems += [random.permutation(m)]
    return mems

def Fitness(mem):
    penalty = 0
    size = len(mem)
    for i in range(size-1):
        for j in range(i+1, size):
            if mem[i]-i == mem[j]-j or mem[i]+i == mem[j]+j or mem[i] == mem[j]:
                penalty += 1
    return 1.0/(penalty+1)

def Recombination(gene1, gene2):
    size = len(gene1)
    p = random.randint(1, size)
    ngene1 = gene1[0:p]
    ngene2 = gene2[0:p]
    for i in range(size):
        if ngene1.count(gene2[i])==0:
            ngene1 += [gene2[i]]
        if ngene2.count(gene1[i])==0:
            ngene2 += [gene1[i]]
    return [ngene1, ngene2]

def Mutation(gene):
    size = len(gene)
    p = random.permutation(size)[:2]
    gene[p[1]], gene[p[2]] = gene[p[2]], gene[p[1]]
    return gene

def Parent_selection(genes):
    size = len(genes)
    num = 5
    ngenes = []
    for i in random.permutation(size)[:num]:
        ngenes += [genes[i]]
    ngenes.sort(key=Fitness)
    return [ngenes[0], ngenes[1]]

m = 100 # population number
n = 8 # n-queen
mems = Initialisation(m, n) # population initialisation
mems.sort(key=Fitness)

for mem in mems:
    print(Fitness(mem))
