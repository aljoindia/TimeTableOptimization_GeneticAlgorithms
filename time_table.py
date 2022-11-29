import random as rand
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as mt
import population_generation as pg


# Crossover the parents to generate 3 children.
def crossover(s, slots, days, hours):
    for k in range(len(s)):
        val0 = 2
        while val0 != hours:
            s[k] = np.array([rand.choice([0, 1]) for _ in range(slots * days)]) # changes the values of the rows (creating a child).
            val0 = sum(s[k])
    
    return s

# If after the crossover if ONE class still has collion(s) we change the values individually again with is mutation.
def mutation(slots, days, hours):
    valthis = 2 # taking some false value.
    while valthis != hours: # check if the row that has the values equal to the number fo hours.
        s = np.array([rand.choice([0, 1]) for _ in range(slots * days)]) # changes the values of the rows (creating a child).
        valthis = sum(s)
    return s


def fitness(s1, s2):
    t1 = pd.DataFrame(s1)
    t2 = pd.DataFrame(s2)
    count = 0
    for i in range(len(t1)):
        s1 = list(t1.loc[i]) # The ith row of class 1.
        s2 = list(t2.loc[i]) # The ith row of class 2.
        for j in range(len(s1)):
            if s1[j] == 1 and s2[j] == 1: # Only when both the classes have Allele as 1 do we consider that there is collision.
                count += 1
    print(f'Number of collisions: {count}')
    fitprob = 1 / (1 + count) # Fitness Function
    return fitprob

def selction(s, slots, days, hours):

    s = crossover(s, slots, days, hours) # Put the Parents to generate a new batch of children.

    val2 = s.sum(axis=0) # give a row of the sum of the values of the rows.
    while (val2 != np.ones(slots*days)).any(): # checking to see if the added values are equal to [1, 1, 1, 1, 1, 1, 1, 1]
        for i in range(len(s)):
            s[i] = mutation(slots, days, hours) # Put each child to generate a new child.
        val2 = s.sum(axis=0) # adding the values back.
        # print(s)

    return s

def plot_schedule(t1, t2, slots, days, teachers):
    x_labels = []
    shift_names = {0: 'period 1', 1: 'period 2', 2: 'period 3'} # Taking 3 periods as a label
    
    for i in range(0, 3 * slots):
        days = mt.floor(i / 3) + 1
        shift = shift_names[i % 3]
        x_labels.append(f'Day {days} : {shift}')

    y_labels = []

    for i in range(0, teachers):
        y_labels.append(f'Teacher: {i+1}')

    fig = plt.figure()
    
    # plt.tight_layout()
    # plt.subplots_adjust(top=0.88)

    plt.subplot(1, 2, 1) # creates a space in a plot window.
    plt.imshow(t1, cmap='binary') # plots the values of o's and 1's in terms of black and white respectively.
    plt.xticks(list(range(0, days * slots)), x_labels, rotation = 90) # the x axis values.
    plt.yticks(list(range(0, teachers)), y_labels) # the y axis values.
    plt.title(f'Class1', size = 14) # size of the values.

    plt.subplot(1, 2, 2) # creates a space in a plot window.
    plt.imshow(t2, cmap='binary') # plots the values of o's and 1's in terms of black and white respectively.
    plt.xticks(list(range(0, days * slots)), x_labels, rotation = 90) # the x axis values.
    plt.yticks(list(range(0, teachers)), y_labels) # the y axis values.
    plt.title(f'Class1', size = 14) # size of the values.

    fig.suptitle(f'Fitness: {fitness(t1, t2)}', size = 16)
    plt.show()

obj = pg # generates a population as soon as you make an instance.
slots = obj.slots # The number of periods in a class.
days = obj.days # The number of days in a week.
teachers = obj.teachers # The number of teachers teaching. (Faculty)
hours = obj.hours # The number of hours every teacher get per week.

# print(slots, days, teachers)

tt1 = pd.read_csv('see1.csv', header = None) # generated population is taken from a csv file for class 1.
tt2 = pd.read_csv('see2.csv', header = None) # Generated population is taken from a csv file for class 2.

plot_schedule(tt1, tt2, slots, days, teachers) # Plots the Initial population with collision.

s1 = np.array(tt1) # converting the dataframe to a numpy array for class 1.
s2 = np.array(tt2) # converting the dataframe to a numpy array for class 2.

print('Generation 1:')
print(pd.DataFrame(s1)) # Printing the original population that was generated for class 1.
print('\n',pd.DataFrame(s2)) # Priniting the original population that was generated for class 2.
fit = fitness(s1, s2)
print(f'Fitness: {fit}') # Show the initial fitness.

gen = 2
while fit != 1: # Keep checking till the two classes give no collisions and fitness is 1.
    s1 = selction(s1, slots, days, hours) # Put the numpy array up to select a batch of children for class 1
    s2 = selction(s2, slots, days, hours) # Put the numpy array up to select a batch of children for class 2

    print(f'\n\nGeneration {gen}:')
    tt1 = pd.DataFrame(s1) # Change the numpy array to a dataframe for class 1
    tt2 = pd.DataFrame(s2) # Change the numoy array to a dataframe for class 2.
    
    print(tt1)
    print(f'\n{tt2}')
    fit = fitness(s1, s2)
    print(f'Fitness: {fit}') # Show the fitness.
    gen += 1 # Increment the Generation count

plot_schedule(tt1, tt2, slots, days, teachers) # Plots the final population without collision.