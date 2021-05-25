def binary_search(collection, target):
    first = 0
    last = len(collection) - 1
    first = 0
    last = len(collection) - 1
    while first <= last:
        midpoint = (first + last)
        if collection[midpoint] == target:
            return midpoint
        elif collection[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None

names = ["Ayee Bee", "Cee Dee", "Ee Ef"]
search_names = ["Ayee Bee", "Ee Ef"]
for n in search_names:
    index = binary_search(names, n)
    print(index)

