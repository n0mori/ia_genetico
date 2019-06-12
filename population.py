import random

# Os vetores serão representados por uma lista cujos elementos serão a ordem
# em que serão colocados na mochila.

def gen_population(item_count, pop_size=20):
    pop = []
    for i in range(pop_size):
        pop.append(random.sample(range(50), 50))
    return pop

def fitness(gene, dataset, cap):
    fit = 0;
    for item, _ in sorted(enumerate(gene), key=lambda tpl: tpl[1]):
        weight = int(dataset[item][1])
        imp = int(dataset[item][2])
        if cap - weight >= 0:
            cap -= weight
            fit += imp
    return fit

def apply_fitness(pop, dataset, cap):
    fits = []
    for gene in pop:
        fits.append(fitness(gene, dataset, cap))
    return fits

