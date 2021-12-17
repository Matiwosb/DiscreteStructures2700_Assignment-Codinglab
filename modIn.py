'''
def mode_inverse (x, n):
    for r in range(1, n):
        if(x*r)%n == 1:
            return r

print(mode_inverse(6, 5))
print(mode_inverse(35, 18))
print(mode_inverse(6, 3))
'''


def mult(a, b):
    if a == 0:
        return 0
    elif a == 1:
        return b
    else:
        return b + mult(a - 1, b)


