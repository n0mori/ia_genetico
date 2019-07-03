import random

# Os vetores serão representados por uma lista cujos elementos serão a ordem
# em que serão colocados na mochila.

def gen_population(item_count, pop_size=20):
    pop = []
    for i in range(pop_size):
        pop.append(random.sample(range(item_count), item_count))
    return pop

def calculate_fitness(gene, dataset, cap):
    fit = 0
    for item in gene:
        weight = int(dataset[item][1])
        imp = int(dataset[item][2])
        if cap - weight >= 0:
            cap -= weight
            fit += imp

    return fit

def bag(gene, dataset, cap):
    bag = [0 for i in gene]
    for item in gene:
        weight = int(dataset[item][1])
        imp = int(dataset[item][2])
        if cap - weight >= 0:
            cap -= weight
            bag[item] = 1
        else:
            bag[item] = 0
    return bag

def fitness(pop, dataset, cap):
    fits = []
    for gene in pop:
        fits.append(calculate_fitness(gene, dataset, cap))
    return fits

def mutate(pop, rate):
    for gene in pop:
        if random.random() > rate:
            random.shuffle(gene)

'''
 Notes about how the crossing works
 1 5 3 2 6 4 7 8
 4 6 2 8 5 3 1 7
 
 6 4 7 8
 2 1 8 4
 
 (2,6) (1,4) (8,7) (4,8)
 (1,4) (2,6) (4,8) (8,7)
 4 6 8 7
 
 5 3 1 7
 2 3 1 7
 (2,5) (3,3) (1,1) (7,7)
 (1,1) (2,5) (3,3) (7,7)

 1 5 3 7

 1 5 3 2 4 6 7 8
 4 6 2 8 1 5 3 7
 
'''

# do not pass fitness
def crossover(mom, dad):
    head_mom = mom[:int(len(mom) / 2)]
    tail_mom = mom[int(len(mom) / 2):]
    
    head_dad = dad[:int(len(dad) / 2)]
    tail_dad = dad[int(len(dad) / 2):]
    
    order_mom = [dad.index(x) for x in tail_mom]
    order_dad = [mom.index(x) for x in tail_dad]
    
    _, half_heir1 = zip(*sorted(zip(order_mom, tail_mom)))
    _, half_heir2 = zip(*sorted(zip(order_dad, tail_dad)))
    
    half_heir1 = [x for x in half_heir1]
    half_heir2 = [x for x in half_heir2]
    
    heir1 = head_mom + half_heir1
    heir2 = head_dad + half_heir2
    
    return heir1, heir2    

# do not pass fitness
def cross_pop(parents):
    new_pop = []
    
    moms = parents[:int(len(parents)/2)]
    dads = parents[int(len(parents)/2):]
    
    for cross in zip(moms, dads):
        new_pop += crossover(cross[0], cross[1])
    
    return new_pop
