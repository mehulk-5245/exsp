#suggest me some better approach if possible
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = 10
result = fibonacci(n)
print("Fibonacci number at position", n, ":", result)
