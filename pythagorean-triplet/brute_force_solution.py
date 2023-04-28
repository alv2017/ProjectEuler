import csv
from math import ceil

n = 3000
data = {key: -1 for key in range(1, 3001)}

for n in range(1, 3001):
    for y in range(1, ceil(n / 2)):
        for x in range(1, y):
            z = n - x - y
            if x**2 + y**2 - z**2 == 0:
                abc = x * y * z
                if abc > data[n]:
                    data[n] = abc


with open("test_triplet_data.csv", "w", newline="") as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=",", quotechar="'")
    csv_writer.writerow(["N", "MaxABC"])

    for k, v in data.items():
        csv_writer.writerow([k, v])
