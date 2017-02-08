def fib(n, d={-1: 0, 0:0, 1:1}):
    if n in d:
        return d[n]
    else:
        d[n] = fib(n-1) + fib(n-2)
        return d[n]

print(0, fib(0))
print(1, fib(1))
print(2, fib(2))
print(3, fib(3))
print(4, fib(4))
print(5, fib(5))
print(6, fib(6))
print(7, fib(7))
print(10, fib(10))
print(20, fib(20))
print(50, fib(50))
