# Solution of n-queens by Genetic-algorithm

## 1. Issue:
Place n queens on an nxn chessboard in such a way that they cannot check each other.

## 2. Representation:
* Phenotype: a board configuration
* Genotype: a permutation of the numbers 0-n

![representation](https://raw.githubusercontent.com/VakhshooriEhsan/EvolutionaryComputing2020-HW1-8Queens/master/docs/imgs/representation.PNG)

## 3. Initialisation:
Initialisation(n, m) function returns m random members of n-queens genotype.

## 4. Fitness:
Fitness(mem) function get mem value as a n-queens genotype and returns 1/(penalty+1) that penalty is number of each pair of queens that check each other.

<!--
# Representation: Permutations
# Recombination: 'Cut-and-crossfill' crossover, probability: 100%
# Mutation: Swap, probability: 80%
# Parent selection: Best 2 out of random 5

# Survival selection: Replace worst
# Population size: 100
# Number of offspring: 2
# Initialisation: Random
# Termination condition: Solution or 10000 fitness evaluations
-->
