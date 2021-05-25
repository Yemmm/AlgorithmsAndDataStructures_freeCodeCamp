def index_of_item(collection, target):
    for i in range(0, len(collection)):
        if target == collection[i]:
            return i
    return None


names = ["Ayee Bee", "Cee Dee", "Ee Ef"]
search_names = ["Ayee Bee", "Ee Ef"]

for n in search_names:
    index = index_of_item(names, n)
    print(index)