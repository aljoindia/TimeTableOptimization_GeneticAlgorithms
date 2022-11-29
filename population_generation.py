import pandas as pd
import random

class Time_Table_Population:

    def __init__(self, teachers, days, slots, hours) -> None:
        self.teachers = teachers
        self.days = days
        self.slots = slots
        self.hours = hours
        # self.fitness = self.__class__.set_fitness_function(self.create_schedule())

    def create_schedule(self):
        self.gene_list = [random.choice([0, 1]) for _ in range(self.teachers * self.slots * self.days)]
        t = {}
        for e in range(1, self.teachers + 1):
            shift_len = self.days * self.slots
            t[e] = self.gene_list[shift_len * (e - 1): shift_len * e]
        schedule_df = pd.DataFrame(data = t)
        # print(schedule_df)
        return schedule_df

# teachers = int(input('Enter number of teachers teaching: '))
# days = int(input('Enter the number of days: '))
# slots = int(input('Enter the number of periods: '))

teachers = 3
days = 3
slots = 3
hours = 3

t1 = Time_Table_Population(teachers, days, slots, hours)
t2 = Time_Table_Population(teachers, days, slots, hours)

class1 = t1.create_schedule().T
class2 = t2.create_schedule().T

class1.to_csv('tt1.csv', index=False, header=False)
class2.to_csv('tt2.csv', index=False, header=False)
