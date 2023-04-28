def get_triplets(n):
    triplets = set()
    for x in range(1, ceil(n / 3)):
        if (n * n - 2 * n * x) % (2 * n - 2 * x) == 0:
            y = (n * n - 2 * n * x) // (2 * n - 2 * x)
            z = n - x - y
            triplet = [x, y, z]
            triplet.sort()
            triplets.add(tuple(triplet))
    return triplets


def max_abc_triplet(triplets: set):
    maxabc = 1
    if not triplets:
        return -1
    for triplet in triplets:
        abc = triplet[0] * triplet[1] * triplet[2]
        if abc > maxabc:
            maxabc = abc

    return maxabc


if __name__ == "__main__":
    for n in range(3000):
        triplets = get_triplets(n)
        print(n, max_abc_triplet(triplets))
