t = (1, 2, 3, 2, 4, 1, 5, 3)
repeated = []

for item in t:
    if t.count(item) > 1 and item not in repeated:
        repeated.append(item)

print("Repeated items:", tuple(repeated))