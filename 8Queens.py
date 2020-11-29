# Representation: Permutations
# Recombination: 'Cut-and-crossfill' crossover, probability: 100%
# Mutation: Swap, probability: 80%
# Parent selection: Best 2 out of random 5

# Survival selection: Replace worst
# Population size: 100
# Number of offspring: 2
# Initialisation: Random
# Termination condition: Solution or 10000 fitness evaluations

from numpy import random

def Eval(gene):
    penalty = 0
    size = len(gene)
    for i in range(size-1):
        for j in range(i+1, size):
            if gene[i]-i == gene[j]-j or gene[i]+i == gene[j]+j or gene[i] == gene[j]:
                penalty += 1
    return penalty

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
    ngenes.sort(key=Eval)
    return [ngenes[0], ngenes[1]]

def Initialisation(n, size):
    genes = []
    for i in range(n):
        genes += [random.permutation(size)]
    return genes


population = 100
size = 8
genes = Initialisation(population, size)


print(genes)