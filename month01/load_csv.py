import csv

with open("customers.csv", newline="") as f:
    reader = csv.DictReader(f)
    customers = list(reader)

print(customers[:3])
