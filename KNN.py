class Neighbor:
    def __init__(self, values, group):
        self.values = values
        self.group = group

def get_distance(neighbor):
    return neighbor.distance

def k_nearest_neighbors(dataset, query, k = 1):
    for neighbor in dataset:
        neighbor.distance = (sum((v - q) ** 2 for v, q in zip(neighbor.values, query))) ** 0.5
    dataset.sort(key = get_distance)
    freqs = {neighbor.group: 0 for neighbor in dataset[0:k]}
    biggest = 0
    index = 0
    for i in range(k):
        group = dataset[i].group
        freqs[group] += 1

        if freqs[group] > biggest:
            biggest = freqs[group]
            index = group
    return index

def load_iris(path):
    with open(path) as f:
        lines = f.readlines()
    dataset = [line.split(',') for line in lines]

    return [Neighbor((float(value) for value in line[0:3]), line[4]) for line in dataset]

if __name__ == '__main__':
    dataset = load_iris('C:\\Users\\Heitor\\Dropbox\\Computing\\F#\\ML4U\\ML4U\\iris.data')
    query = [5.957, 3.115, 5.17474, 1.789484]
    group = k_nearest_neighbors(dataset, query, 5)

    print(group)
