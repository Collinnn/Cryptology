import math
import random
from Crypto.Util.number import isPrime

def coprimeElements(N):
    """N is the number to find a list of coprime elements, these are also the element counted by phi"""
    n = []
    for i in range(1, N):
        if math.gcd(i, N) == 1:
            n.append(i)
    print("The list of coprime elements is ")
    print(n)
    return n 

def coprimeElementsAmount(N):
    """N is the number to find the coprime elements of, it also gives back phi"""
    n = 0
    for i in range(1, N):
        if math.gcd(i, N) == 1:
            n=n+1
    print("The number of primitive elements is " + str(n))
    return n


def discreteLogarithm(p,g,h):
    """p is the prime number, g is the generator, h is the element to find the discrete logarithm of, if h is 1 then it will find the order of g"""
    list = []
    for i in range(1,100):
        gPow = pow(g,i,p)
        list.append(gPow)
        if(gPow==h):
            printListTable(list)
            return i

def printListTable(n):
    """n is the list to print as a table"""
    for i in range(1,len(n)+1):
        print(str(i) + "\t", end="")
    print()
    for i in n:
        print(str(i) + "\t", end="")


# find all primitive elements of Z_N
def primitiveElements(N): #Fixed ^T
    """N is the number to find the primitive elements of"""
    #Prints the number of primitive elements
    coprimeElementsAmount(coprimeElementsAmount(13))
    # Coprime elements of N
    required_set = {num for num in range(1, N) if math.gcd(num, N) }
    # Elements that are primitive of N
    return [g for g in range(1, N) if required_set == {pow(g, powers, N)
            for powers in range(1, N)}]

def primitiveElementFinder(N):
    list = []
    primitiveElementList = []
    list = coprimeElements(N)
    orderList = []
    for i in list:
        for j in range(1,N):
            if (j == N-1):
                if(pow(i,j,N) == 1):
                    orderList.append(j)
                    primitiveElementList.append(i)
                    break
            else:
                if(pow(i,j,N) == 1):
                    orderList.append(j)
                    break
    printListTable(orderList)
    print()      
    print("The primitive elements are the following" + str(primitiveElementList))

    

def trial_division(n: int) -> "list[int]":
    """Return a list of the prime factors for a natural number."""
    a = []               # Prepare an empty list.
    f = 2                # The first possible factor.    
    while n > 1:         # While n still has remaining factors...
        if n % f == 0:   # The remainder of n divided by f might be zero.        
            a.append(f)  # If so, it divides n. Add f to the list.
            n //= f      # Divide that factor out of n.
        else:            # But if f is not a factor of n,
            f += 1       # Add one to f and try again.
    return a             # Prime factors may be repeated: 12 factors to 2,2,3.


def diffieHellmannKeyExchange(p,g,a,b):
    """p is the prime number, g is the generator, a is the secret key for Alice, b is the secret key for Bob"""
    A = pow(g,a,p)
    B = pow(g,b,p)
    print("The message for Alice is " + str(A))
    print("The message for Bob is " + str(B))
    sA = pow(B,a,p)
    sB = pow(A,b,p)
    print("The shared secret key for Alice is " + str(sA))
    print("The shared secret key for Bob is " + str(sB))
    if sA == sB:
        print("The shared secret key is the same for both Alice and Bob")
    else:
        print("The shared secret key is not the same for both Alice and Bob")


def extendedEuclideanAlgorithm(a,b):
    """a is the first number, b is the second number"""
    (old_r, r) = (a, b)
    (old_s, s) = (1, 0)
    (old_t, t) = (0, 1) 
    while r != 0:
        qv = old_r//r
        (old_r, r) = (r, old_r - qv * r)
        (old_s, s) = (s, old_s - qv * s)
        (old_t, t) = (t, old_t - qv * t)
    print("The GCD is " + str(old_r))
    print("The Bezout coefficients are " + str(old_s) + " and " + str(old_t))
    print("The quotients by the GCD are " + str(abs(t)) + " and " + str(abs(s)))
    return old_r, old_s, old_t


def RSABruteForce(N,e,c):
    """N is the public key, e is the public exponent, c is the ciphertext"""
    print("The public key is " + str(N) + " and " + str(e))
    p = 0
    q = 0
    for i in range(2, N):
        if N%i == 0:
            p = i
            q = N//i
            break
    print("The private key is " + str(p) + " and " + str(q) + " and " + str(e))
    phi = (p-1)*(q-1)
    print("The value of phi is " + str(phi))
    d = extendedEuclideanAlgorithm(e,phi)[1]
    print("The value of d is " + str(d))
    m = pow(c,d,N)
    print("The plaintext is " + str(m))
    return m


def RSAEncryption(N,e,m):
    """N is the public key, e is the public exponent, m is the plaintext"""
    print("The public key is " + str(N) + " and " + str(e))
    c = pow(m,e,N)
    print("The ciphertext is " + str(c))
    return c


def RSADecryption(p,q,e,c):
    """p and q are the prime numbers, e is the public exponent, c is the ciphertext"""
    n = p*q
    print("The public key is " + str(n) + " and " + str(e))
    print("The private key is " + str(p) + " and " + str(q) + " and " + str(e))
    phi = (p-1)*(q-1)
    print("The value of phi is " + str(phi))
    d = extendedEuclideanAlgorithm(e,phi)[1]
    print("The value of d is " + str(d))
    m = pow(c,d,n)
    print("The plaintext is " + str(m))
    return m


def RSAEncryptionSystem(p,q,e,m):
    """p and q are the prime numbers, e is the public exponent, m is the plaintext"""
    n = p*q
    print("The public key is " + str(n) + " and " + str(e))
    print("The private key is " + str(p) + " and " + str(q) + " and " + str(e))
    phi = (p-1)*(q-1)
    print("The value of phi is " + str(phi))
    d = extendedEuclideanAlgorithm(e,phi)[1]
    print("The value of d is " + str(d))
    c = pow(m,e,n)
    print("The ciphertext is " + str(c))
    m = pow(c,d,n)
    print("The plaintext is " + str(m))
    return c, m


def chineseRemainderTheorem(a,b,N,M):
    """a and b are the two numbers, N and M are the moduli, expects N and M to be coprime"""
    print("The two numbers are " + str(a) + " and " + str(b))
    print("The two moduli are " + str(N) + " and " + str(M))
    T=pow(M,-1,N)
    T2=pow(N,-1,M)
    print("The value of T is " + str(T) + " and " + str(T2))
    x=(M*T*a+N*T2*b)%(N*M)
    print("The solution is " + str(x) + " mod " + str(N*M))
    return x



#discreteLogarithm(17,3,1)


#chineseRemainderTheorem(3,7,9,13)
#              n    e c
#RSABruteForce(9307,3,4151)
#              n  e  c
#RSAEncryption(9307,3,53)
#              n  e  m
#RSADecryption(53,59,3,4151)
#                    p  q  e  m
#RSAEncryptionSystem(53,59,3,4151)
#                           a  b
#extendedEuclideanAlgorithm(17,41)
#print(phi(16))
#coprimeElements(17)
#coprimeElementsAmount(55)
#coprimeElementsAmount(coprimeElementsAmount(13))
#print(primitiveElements(13))

primitiveElementFinder(13)

#primitiveElements(11)
#print(isPrime(41))
#print(trial_division(64))
#                          p  g a b 
#diffieHellmannKeyExchange(17,3,3,5)


#s='s=%r;print(s%%s)';print(s%s)