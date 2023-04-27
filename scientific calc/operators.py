import math

#1ST PART: OPERATORS
def add(m,n):
    return m + n

def sub(m,n):
   return m - n

def div(m,n):
    return m / n
    
def prod(m,n):
    return m * n

def sqrtx(m, n):
    return m ** (1/n)

def sqrt(m):
    z = math.sqrt(m)
    return z

def logyx(m,n):
   return math.log(m, n)

#exponent of m accepts n int only in windows calculator, so it's rounded 
def exp(m, n):
    ex = 10 ** round(n)
    return m * ex

def mod(m,n):
    return m % n

def powerx(m,n):
    return ((m) ** (n))

#2ND PART: MODIFIERS
def abs(m):
    if m < 0:
        return (-1 * m)
    else:
        return m

#also int only
def fact(m):
    return (math.factorial(round(m)))


def euler(m):
    return (m * (math.e))

def pi(m):
    return (m * (math.pi))

def oneOver(m):
    return 1/m

def power2(m):
    return m ** 2
    


def tenPowerx(m):
    return 10**m

def ln(m):
    return math.log(m)

def log(m):
    return math.log(a, 10)

def power3(m):
    return m ** (3)

def sqrt3(m):
    return m ** (1/3)


def twoPower(m):
    return (2 ** m)


def eulerpower(m):
    return((math.e) ** (m))

def sine(m):
    return math.sin(math.radians(m))

def cosine(m):
    return math.cos(math.radians(m))

def tangent(m):
    return math.tan(m)

def cotangent(m):
    return (1/(math.tan(m)))

def sec(m):
    return (1/(math.cos(m)))

def cosec(m):
    return (1/(math.sin(m)))

def cotangent(m):
    return (1/(math.tan(m)))

def arcsin(m):
    return math.asin(m)

def arccos(m):
    return math.acos(m)

def arctan(m):
    return math.atan(m)


def arcsec(m):
    return math.acos(1/(m))

def arccsc(m):
    return math.asin(1/(m))

def arccot(m):
    pass
