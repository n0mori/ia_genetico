import population
import reader
import random

def elite(pop, fits, items=4):
    rank = sorted(zip(pop, fits), key=lambda x : x[-1], reverse=True)
    return rank[:items]

def full_random(pop, fits, items=4):
    total_fitness = sum(fits)
    
    chances = [x / total_fitness for x in fits]
    
    rank = list(zip(pop, fits))
    
    selected = []
    for i in items:
        pass
    
    return selected

dataset, cap = reader.read_dataset('item_50.csv')
pop = population.gen_population(len(dataset))
fits = population.apply_fitness(pop, dataset, cap)
print(elite(pop, fits, 4), full_random(pop, fits, 4))
