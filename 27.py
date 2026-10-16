data = [(1, "A"), (2, "B"), (3, "C")]

numbers, letters = zip(*data)

print("Numbers:", list(numbers))
print("Letters:", list(letters))