
from random import random
from Tools.scripts.pdeps import inverse
# 1
def gcd(x, y):
    if x == 0 and y == 0:
        return None
    elif x == 0:
        return y
    return gcd(y % x, y)


# 2
def mod_inv(x, y):
    r0, r1 = x, y
    s0, s1 = 1, 0
    t0, t1 = 0, 1

    while r1 != 0:
        q = r0 // r1
        r0, r1 = r1, r0 % r1
        s0, s1 = s1, s0 - q * s1
        t0, t1 = t1, t0 - q * t1

    if r0 != 1:
        return None
    invs = (s0 % y + y) % y
    return invs


# 3
def mod_exp(x, y, n):
    p = 1
    x = x % n
    r = y
    while r > 0:

        if (r % 2) == 1:
            p = (p * x) % n

        r = r / 2
        x = (x * x) % n

    return p


# #4
def generate_RSAKeys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    for i in range(3, phi, 2):
        if (gcd(i, phi) == 1:
            e = i
            break

    d = inverse(e, phi)

    return [[e, n], d]


# 5


def main():
    x = int(input("Enter an integer: "))
    y = int(input("Enter an integer: "))
    print(gcd(x,y))

    p = int(input())
    q = int(input())
    print(generate_RSAKeys(p, q))

    n = int(input("Enter an integer: "))
    print(mod_exp(x,y,n))


if __name__ == '__main__':
    main()
