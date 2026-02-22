def caching_fibonacci():
    cache = {}
    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if not n in cache:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    return fibonacci


def fibonacci_list_with_no_recursion(n):
    fib_list = [0]
    a, b = 0, 1
    while n > 0:
        fib_list.append(b)
        a, b = b, a+b
        n -= 1
    return fib_list

fibonacci_with_cache = caching_fibonacci()
print(fibonacci_with_cache(10))
print(fibonacci_list_with_no_recursion(10))