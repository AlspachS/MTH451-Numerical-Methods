import math

def test1(x):
    return math.e**x

def test2(x):
    return 1

# I = (2*h/45)*( 7*f(a) + 32*f(a+h) + 12*f(a+2*h) + 32*f(a+3*h) + 7*f(a+4*h) )

def BoolesRule(a, b, f):
    h = abs(b-a) / 4

    acc = 0
    acc += 7 * ( f(a)+f(b) )
    for index in range(min(a, b)+1, max(a, b)):
        if index % 2 == 1:
            acc += 32*f(a+index*h)
        elif index % 4 == 2:
            acc += 12*f(a+index*h)
        elif index % 4 == 0:
            acc += 14*f(a+index*h)

    acc *= ((2*h) / 45)

    return acc

    # acc = 0
    # for i in range(min(a, b), max(a, b), 4):
    #     acc += 7*f(a+i*h)
    #     acc += 32*f(a+(i+1)*h)
    #     acc += 12*f(a+(i+2)*h)
    #     acc += 32*f(a+(i+3)*h)
    #     acc += 7*f(a+(i+4)*h)
    #
    #     acc *= 2*h / 45

    return acc

print(BoolesRule(0, 8, test1))