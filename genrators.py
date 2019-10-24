# A simple generator for Fibonacci Numbers
def fib(n):
    a,  b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b

# creating a generator object
x = fib(5)

print(x.__next__())
print(x.__next__())
print(x.__next__())