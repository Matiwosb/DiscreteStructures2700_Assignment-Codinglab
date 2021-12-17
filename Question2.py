import itertools

def k_subsets_naive(S, k):
    if k < 0 or k > len(S):
        return []

    subsets = [[]]
    for i in range(1, len(S) + 1):
        subsets = subsets + list(itertools.combinations(S, i))

    k_subsets = []
    for i in subsets:
        if len(i) == k:
            k_subsets.append(i)

    return k_subsets


print(k_subsets_naive([4, 5, 6], 2))
