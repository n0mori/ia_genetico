import population
import random

def elite(pop, fits, items=4):
    rank = sorted(zip(pop, fits), key=lambda x : x[-1], reverse=True)
    return rank[:items]

def roulette(pop, fits, items=4):
    total_fitness = sum(fits)
    rank = list(zip(pop, fits))

    chances = [x[1] / total_fitness for x in rank]
    
    odds = [chances[0]]
    for c in chances[1:]:
        odds.append(c + odds[-1])
        
    print(chances, odds)
    selected = []
    for i in range(items):
        num = random.random()
        for o in odds:
            if o > num:
                selected.append(rank[odds.index(o)])
                break
    
    return selected

def tournament(zipped_pop, items):
    # gerando a bracket
    random.shuffle(zipped_pop)

    if len(zipped_pop) <= items:
        return zipped_pop
    
    winners = []
    for i in range(int(len(zipped_pop) / 2)):
        home, away = zipped_pop[i], zipped_pop[-1 - i]
        if home == away:
            winners.append(home)
        elif home[1] >= away[1]:
            winners.append(home)
        else:
            winners.append(away)
    
    return tournament(winners, items)

