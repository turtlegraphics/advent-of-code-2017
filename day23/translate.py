
def fun(b,c):
    h = 0
    g = 1               # fake
    while g != 0:           # 29,30,32

        f = 1               # 9
        d = 2               # 10

        while True:
            e = 2           # 11

            while True:
                if b == d*e:  # 12-14,15
                    f = 0   # 16

                e += 1      # 17
                if e == b:  # 18-19
                    break

                # test+loop # 20

            d += 1          # 21
            if b == d:      # 22-23
                break       # 24

        if f == 0:          # 25
            h += 1          # 26

        g = b-c             # 27-28

        b += 17             # 31
    return h

# part 1:
print('part 1 h =',fun(99,99))

# part 2:
print('part 2 h =',fun(109900, 126900))
