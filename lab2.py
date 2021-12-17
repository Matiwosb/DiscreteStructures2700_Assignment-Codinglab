# Question 1
def matrix_print(A):
    for list in A:
        for number in list:
            print(number, end=" ")
        print()


# Question 2
def matrix_add_boolean(A, B):
    sum = []
    for i in range(len(A)):
        sum.append([])
        for j in range(len(A[i])):
            if A[i][j] == 1 or B[i][j] == 1:
                sum[i].append(1)
            else:
                sum[i].append(0)
    return sum


# Question 3
def matrix_multiply_boolean(A, B):
    S = [[0 for row in range(len(A))] for col in range(len(B[0]))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                S[i][j] = S[i][j] + A[i][k] * B[k][j] # addition metrix 0 or 1 boolean
    return S


# Question 4
def matrix_power(A, n):
    result = A
    for i in range(n - 1):
        result = matrix_multiply_boolean(result, A)
    return result


# Question 5
def transitive_closure(A):
    n = len(A)
    result = A
    for i in range(n + 1):
        r = matrix_power(A, i)
        result = matrix_add_boolean(result, r)

    return result


# Question 6
def main():
    print("Addition Matrix")
    A = [[0, 1], [1, 0]]
    B = [[1, 0], [1, 0]]
    M = matrix_add_boolean(A, B)
    matrix_print(M)
    print("Multiplication Matrix")
    A = [[0, 1, 1], [1, 0, 1]]
    B = [[1, 0], [0, 0], [0, 1]]
    result = matrix_multiply_boolean(A, B)
    matrix_print(result)
    print("Power Matrix")
    R = [[0, 0, 0, 1], [0, 1, 1, 0], [0, 0, 0, 1], [0, 0, 1, 0]]
    result1 = matrix_power(R, 2)
    matrix_print(result1)
    print("Transitive Closure")
    R = [[0, 0, 0, 1], [0, 1, 1, 0], [0, 0, 0, 1], [0, 0, 1, 0]]
    result2 = transitive_closure(R)
    matrix_print(result2)


if __name__ == '__main__':
    main()
