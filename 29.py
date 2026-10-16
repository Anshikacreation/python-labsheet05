t = (5, 5, 5, 5, 5)

if len(t) > 0 and all(x == t[0] for x in t):
    print("All elements are the same")
else:
    print("All elements are not the same")