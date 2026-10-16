t = ((1, 2), (3, 4), (5, 6))
result = ()

for subtuple in t:
    result += subtuple

print("Flattened tuple:", result)