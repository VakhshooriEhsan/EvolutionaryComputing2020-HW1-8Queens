# Solution of n-queens by Genetic-algorithm

## 0. Setup:
* install Python3.
* install python3 library:
```bash
$ pip install numpy
$ pip install matplotlib
```
* clone and run:
```bash
$ git clone https://github.com/VakhshooriEhsan/EvolutionaryComputing2020-HW1-8Queens.git
$ cd EvolutionaryComputing2020-HW1-8Queens/src
$ python nQueens.py
```

## 1. Issue:
Place n queens on an nxn chessboard in such a way that they cannot check each other.

## 2. Solving:

### 2.1. Representation:
* Phenotype: a board configuration
* Genotype: a permutation of the numbers 0, 1, ...(n-1)

![representation](https://github.com/VakhshooriEhsan/EvolutionaryComputing2020-HW1-8Queens/blob/master/docs/imgs/representation.PNG?raw=true)

### 2.2. Initialisation:
Initialisation(n, m) function returns m random members of n-queens genotype.

### 2.3. Fitness:
Fitness(mem) function get member value as a n-queens genotype and returns 1/(penalty+1) that penalty is number of each pair of queens that check each other.

### 2.4. Parent selection:
Parent_selection(mems, num) function get population members & number and return best 2 members of random number.

### 2.5. Recombination:
Recombination(mem1, mem2, prob) function get 2 members as parents & probability of combination and return 2 childs with use cut-and-crossfill crossover.

### 2.6. Mutation:
Mutation(mem, prob) function get 1 member & mutation probability and return mutated member with use swap mutation.

### 2.7. Survival_selection:
Survival_selection(mems, child) function get population members & 1 child and replace child with the worst population member.

## 3. Result and Analyze:
* Best answers of final result

![representation](https://github.com/VakhshooriEhsan/EvolutionaryComputing2020-HW1-8Queens/blob/master/docs/imgs/Figure_1.png?raw=true)

* diagram of Max fitness & k-max fitness average of each generation

![representation](https://github.com/VakhshooriEhsan/EvolutionaryComputing2020-HW1-8Queens/blob/master/docs/imgs/Figure_2.png?raw=true)
