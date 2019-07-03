#!/usr/bin/env python3.7

import population
import reader
import selection
import sys
import time

def run(filename, seconds=10, mutation_rate=0.2, selector=selection.elite):
    dataset, volume = reader.read_dataset(filename)
    pop = population.gen_population(len(dataset), 4)

    alpha = None
    i = 0
    target_time = time.time() + seconds
    while time.time() < target_time:
        parents, fitness = zip(*selector(pop, population.fitness(pop, dataset, volume), items=2))

        max_fit = (max(fitness), parents[fitness.index(max(fitness))])
        

        print('gen:', i, 'fitness:', max_fit[0], max_fit[1])
        i += 0
        
        if alpha == None or max_fit[0] > alpha[0]:
            alpha = max_fit
        
        population.mutate(parents, 0.2)
        pop = population.cross_pop(parents)

    # Printing the best bag
    output_file = open("output.txt", "w")
    for i in population.bag(alpha[1], dataset, volume): print(i, file=output_file)

    print('golden individual:', alpha)

run(sys.argv[1])
