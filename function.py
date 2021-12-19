def sloth(n):
    for i in range(n):
        print('sloth')

def add(x,y):
    return x + y

def solve_hanoi(n, start, end, scratch):
    if n != 0:
        
    solve_hanoi(n-1, start, scratch, end)
    print(f'Move the disc from {start} to {end}')
    solve_hanoi(n-1, scratch, end, start)
    

if ___name___ == '__main__':
    sloth(4)
    
    z = add(10, 2)
    print(z)


    solve_hanoi(3, 'A', 'B', 'C')

 
