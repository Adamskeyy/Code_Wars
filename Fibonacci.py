# def fib(n):
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a + b

# def fib(n):
#     a, b = 0, 1
#     for i in range(n + 1):
#         print(f'{i}. {a}')
#         a, b = b, a + b

def fib(n):
    a, b = 0, 1
    for i in range(n):
        print(f'{i}'.join(' .'), a)
        a, b = b, a + b


fib(100)

