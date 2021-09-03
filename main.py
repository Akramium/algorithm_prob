import itertools
import numpy

stuff = [2, 2, 3, 5, 5, 7, 11]

def is_slice_in_list(s, l):
    len_s = len(s)  # so we don't recompute length of s on every iteration
    return any(s == l[i:len_s + i] for i in range(len(l) - len_s + 1))


combinations = []
for L in range(0, len(stuff) + 1):
    for subset in itertools.combinations(stuff, L):
        combinations.append(list(subset))

# print(combinations)

sum_combination = [sum(combination) for combination in combinations]
prod_combination = [numpy.prod(combination) for combination in combinations]

matches = set(sum_combination) & set(prod_combination)

for match in matches:
    possibility = combinations[sum_combination.index(match)] + combinations[prod_combination.index(match)]
    indices = [i for i, x in enumerate(sum_combination) if x == match]

    for indice in indices:
        posibility = combinations[indice] + combinations[prod_combination.index(match)]

        posibility.sort()
        stuff.sort()

        if is_slice_in_list(posibility, stuff):
            print("FOUND!")
            print(f"Group 1 = {combinations[indice]}")
            print(f"Group 2 = {combinations[prod_combination.index(match)]}")
