import sympy

def fun(b,c):
    """Counts the number of composite numbers b + 17k between b and c."""
    h = 0
    while b <= c:           # 29,30,32
        if not sympy.isprime(b):          # 25
            h += 1          # 26
        b += 17             # 31
    return h

# part 1:
print('part 1 h =',fun(99,99))

# part 2:
print('part 2 h =',fun(109900, 126900))
