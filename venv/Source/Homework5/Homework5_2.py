# Problem 4.5:
#
# There is a method for estimating a definite integral similar to Simpson’s
# rule which we will call Paul’s Peculiar Rule.  It requires that we divide
# the interval into a number of subintervals divisible by four.  Then,
#
#       INTEGRAL a|b f(x)dx ≈ (2h/9)*(−f(a) − f(b)
#                              + 16*sum(0, (n/4)-1, f(xsub(4k + 1)))
#                              - 12*sum(0, (n/4)-1, f(xsub(4k + 2)))
#                              + 16*sum(0, (n/4)-1, f(xsub(4k + 3)))
#                              − 2 *sum(0, (n/4)-1, f(xsub(4k))))
#
# a) Add to your Python file integral.py by writing a short python program
#       called PPR which takes a, b, and n as arguments and estimates
#       INTEGRAL a|b f(x)dx according to Paul’s Peculiar Rule using
#       n subintervals.
#
# b) Estimate INTEGRAL 1|4 ln(x)dx using the Trapezoidal Rule, Simpson’s
#       Rule, and Paul’s Peculiar Rule for n = 12, n = 120, and n = 1200.
#       Compare the methods.
#
# c) What is the order of accuracy of Paul’s Peculiar Rule? How do you know?
#       It appears to be O(h**4).

import math

def trapazoidal(a, b, n, f):
    h = abs(a-b)/n
    area = (h/2)*(f(a) + f(b))
    for i in range(1, n):
        area += f(a + (i*h)) * h
    return area

def simpsons(a, b, n, f):
    h = abs(a-b)/n
    area = f(a) + f(b)
    for i in range(1, n, 2):
        area += 4*f(a+h*i)
    for i in range(2, n-1, 2):
        area += 2*f(a+h*i)
    return area * (h/3)

def PPR(a, b, n, f):
    h = abs(b - a) / n

    area = -f(a) - f(b)
    for i in range(1, n, 2):
        area += 16*f(a+h*i)
    for i in range(2, n, 4):
        area -= 12*f(a+h*i)
    for i in range(4, n, 4):
        area -= 2*f(a+h*i)
    return area * 2*h/9

def F(x):
    return x*math.log(x) - x

exact = F(4) - F(1)
for n in range(1, 4):
    estimate = simpsons(1, 4, 12*10**(n-1), lambda x:math.log(x))
    error = estimate - exact
    print(exact, estimate, error, 12*10**(n-1))
print()
for n in range(1, 4):
    estimate = trapazoidal(1, 4, 12*10**(n-1), lambda x:math.log(x))
    error = estimate - exact
    print(exact, estimate, error, 12*10**(n-1))
print()
for n in range(1, 4):
    estimate = PPR(1, 4, 12*10**(n-1), lambda x: math.log(x))
    error = estimate - exact
    print(exact, estimate, error, 12*10**(n-1)+)