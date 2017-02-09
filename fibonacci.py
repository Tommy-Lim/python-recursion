# with caching
def fib_fast(n, d={-1: 0, 0:0, 1:1}):
    if n in d:
        return d[n]
    else:
        d[n] = fib_fast(n-1) + fib_fast(n-2)
        return d[n]

# with caching
def fib_print_fast(n, cache={}, indent=""):
    print(indent, f"fib({n})")
    if n < 2:
        print(indent, f"{n} less than two. returning 1.")
        return 1
    if n in cache:
        print(indent, f"{n} in cache[{n}]. returning", cache[n])
        return cache[n]
    print(indent, f"{n} not in cache[n]. calculating fib({n-1}) + fib({n-2})")
    cache[n] = fib_print_fast(n - 1, cache, indent + "  ") + fib_print_fast(n - 2, cache, indent + "  ")
    print(indent, f"setting cache[{n}] = {cache[n]}")
    return cache[n]

# wihtout caching
def fib_print_slow(n, indent=""):
    print(indent, f"fib({n})")
    if n < 2:
        print(indent, f"fib({n}) == 1")
        return 1
    print(indent, f"fib({n}) == fib(n - 1) + fib(n - 2)")
    return fib_print_slow(n - 1, indent + "  ") + fib_print_slow(n - 2, indent + "  ")


print("10 fast:", fib_fast(10))
print("20 fast:", fib_fast(20))
print("50 fast:", fib_fast(50))
print()

print("10 print fast:", fib_print_fast(10))
print()

print("10 print slow:", fib_print_slow(10))
