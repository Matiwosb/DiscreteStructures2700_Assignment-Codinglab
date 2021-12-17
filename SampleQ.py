def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

def modInv(a,b):
    for x in range(1,b):
        if((a*x)%b) == 1:
            return x
def mod_exp(x, y, n):
    p = 1
    x = x % n
    r=y
    while r > 0:
        if (r % 2) == 1:
            p = (p * x) % n
            y = r / 2
            o = (x * x) % n
            return p, y, o
        #return r
            #return x
p = int(input('Enter the value of p (prime number 1)= '))
q = int(input('Enter the value of q (prime number 2)= '))
x = int(input('Enter an integer to be encrypted = '))
n = p*q
phi = (p-1)*(q-1)
            #calculating phi
e=3
#We have choosen e=3 from common choices 3,5,17,257,65537
while e<n:
    if gcd(e, phi)==1:
         break;
    else:
        e += 1
        Ct = mod_exp(x,e,n)
                    #encryption
        d=modInv(e,phi)
        #Modulo Inversion function called
        Dt=mod_exp(Ct,d,n)
                    #Decryption
print("You entered Original text = " + str(x))
print("cipher text = " + str(Ct))
print("Deciphered text = " + str(Dt))