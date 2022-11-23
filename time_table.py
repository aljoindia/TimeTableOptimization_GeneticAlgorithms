import pandas as pd
import numpy as np
import random as rand
import itertools as it
from functools import reduce

def crossover(tw):
    for i in range(len(tw)):
        s = list(tw.loc[i])
        # print(s)
        sum = lambda n1, n2: n1 + n2
        val1 = reduce(sum, s)
        if val1 != 3:
            while val1 != 3:
                s = [rand.choice([0, 1]) for _ in range(3 * 3)]
                val1 = reduce(sum, s)

                # print(s, i)
            return s, i

    return s, i

def selection(t1, t2):
    for i in range(len(t1)):
        sc1 = list(t1.loc[i])
        sc2 = list(t2.loc[i])

        print(sc1, i)
    s1, i1 = crossover(t1)
    s2, i2 = crossover(t2)

    return s1, s2, i1, i2

def fitness(t1, t2):
    count = 0

    for i in range(len(t1.T)):
        s1 = list(t1.T.loc[i])
        s2 = list(t2.T.loc[i])
        for j in range(len(s1)):
            if s1[j] == s2[j] and s1[j] == 1 and s2[j] == 1:
                count += 1
    print(f'Number of collisions: {count}')
    fitprob = 1 / (1 + count)
    return fitprob

# def selection(fitnessval):
#     pass

tt1 = pd.read_csv('tt1.csv', header = None).transpose()
tt2 = pd.read_csv('tt2.csv', header = None).transpose()

# print(tt1.T[0])

fit = fitness(tt1, tt2)
print(fit)

gen = 2
while fit != 1:
    print(f'\n This is generation {gen}')
  
    s1, s2, i1, i2 = selection(tt1, tt2)

    tt1 = tt1.T
    tt2 = tt2.T

    tt1[i1] = s1
    tt2[i2] = s2
   
    tt1 = tt1.T
    tt2 = tt2.T
    print(tt1)
    print(tt2)
    
    fit = fitness(tt1, tt2)
    print(f'The fitness is: {fit}')
    gen += 1