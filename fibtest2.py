def fib(n):
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    for i in range(0, 20):
        print(f'fib({i:2}) ==> {fib(i):4}')
