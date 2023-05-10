import math
from Crypto.Util.number import isPrime
def coprimeElements(N):
    """N is the number to find the coprime elements of"""
    n = 0
    for i in range(1, N):
        if math.gcd(i, N) == 1:
            n=n+1
            print("Number is "+ str(n) + " The point is " + str(i))
    print("The number of primitive elements is " + str(n))



# find all primitive elements of Z_N
def primitiveElements(N): #Fixed ^T
    """N is the number to find the primitive elements of"""
    k = 100
    
    listN = []
    for i in range(1, N-1):
        found = False
        for j in range(1, k):
            if math.pow(i,j)%N == 0:
                found = True
                break
        if not found:
            listN.append(i)
    print(listN)
    

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
#coprimeElements(55)
#primitiveElements(400)
#print(isPrime(41))
print(trial_division(64))
#                          p  g a b 
#diffieHellmannKeyExchange(17,3,3,5)
