from Question2 import k_subsets_naive


def k_subsets_better(s, k):
    # base condition for recursion
    if (k < 0 or k > len(s) or len(s) == 0):
        return []

    # if k = 1, then return a list of lists, where each inner list contains one element of s
    if (k == 1):
        l = []
        for item in s:
            l.append([item])
        return l

    # remove an arbitrary element x, now s will be smaller by one element
    # here we are removing last element from set, let removed element is x
    x = s.pop()

    # find all k-1 subsets of s
    k_1_subsets = k_subsets_better(s, k - 1)
    for subset in k_1_subsets:
        # insert x into all k-1 subsets
        subset.append(x)

    # find all the k subsets that don't contain x (removed element)
    no_x_subsets = k_subsets_better(s, k)

    # combine k_1_subsets and no_x_subsets to get result
    k_subsets = k_1_subsets + no_x_subsets

    return k_subsets


print(k_subsets_better(['a', 'b', 'c', 'd', 'e'], 3))
'''Answer
to
question
4:'''

# code to time
import time

subset_test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
k = 5

start_time = time.process_time()
ans_naive = k_subsets_naive(subset_test, k)
end_time = time.process_time()
elpased_time = end_time - start_time
print("Time taken by naive method: {} seconds".format(elpased_time))

start_time = time.process_time()
ans_better = k_subsets_better(subset_test, k)
end_time = time.process_time()
elpased_time = end_time - start_time
print("Time taken by better method: {} seconds".format(elpased_time))
