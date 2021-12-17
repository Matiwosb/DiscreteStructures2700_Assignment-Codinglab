def reverse_string(x):
    if x == '':
        return ''
    else:
        return(x[-1] + reverse_string(x[:-1]))


tests = ['', 'a', 'an', 'cat', 'doge', 'sloth', 'abaucs', 'Treveon', '12345678']

for t in tests:
    print(t, reverse_string(t))
