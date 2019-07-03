#!/usr/bin/env python3.7

import population
import reader
import selection
import sys

filename = sys.argv[1]
gens = 50
mutation_rate = 0.2

dataset, volume = reader.read_dataset(filename)
pop = population.gen_population(len(dataset), 4)

alpha = None
for i in range(gens):    
    parents, fitness = zip(*selection.elite(pop, population.fitness(pop, dataset, volume), items=2))

    max_fit = (max(fitness), parents[fitness.index(max(fitness))])
    

    print('gen:', i, 'fitness:', max_fit[0], max_fit[1])
    
    if alpha == None or max_fit[0] > alpha[0]:
        alpha = max_fit
    
    population.mutate(parents, 0.2)
    pop = population.cross_pop(parents)

# Printing the best bag
output_file = open("output.txt", "w")
population.calculate_fitness(alpha[1], dataset, volume, export_func=lambda x: print(x, file=output_file))

print('golden individual:', alpha)
