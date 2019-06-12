import csv

def read_dataset(filename):
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        dataset = []
        for row in reader:
            dataset.append(row)

    #retornando o dataset limpo e o volume da mochila
    return dataset[2:], int(dataset[1][1])
