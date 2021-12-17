import copy
import itertools

def power_set(s):
    if len(s) == 0:
        return [s]
    remove_item = s.pop()
    subsets = power_set(s)
    s2 = copy.deepcopy(subsets)
    s2.append([remove_item])
    for sub in subsets:
        if sub:
            s2.append(sub + [remove_item])
    return s2

print(power_set([1, 2]))


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


def k_subsets_better(s, k):
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


print(k_subsets_better([4, 5, 6], 2))
"""--------------------------------------------------------------------------------"""
def power_set1(S):
if len(s) == 0:
    return [[]]
else:
    x = s.pop()
    ps = power_set(S)
    for i in ps_copy:
        i.appends(x)
    return ps + ps_copy
def power_set2:
    if len(S) == 0:
        return [[]]
    else:
        x = S.pop()
        return ps + [y + [x] for y in ps]

# problem 2
def problem_set(s,k):
    result = []
    for i in power_set1(S):
        if len(i) == k:
            result.append(i)
    return result

# problem 3
def problem_set3(S, k):
    if k < 0 or k > len(S):
        return []
    elif len(S) == k:
        return [S]
    else:
        x = S.pop()
        s_copy = deepcopy(S)
        subset_with_x = problem_set3(S,k)
        for i in subset_with_x:
            i.append(x)
        subset_without_x = subset_with_x(k)

