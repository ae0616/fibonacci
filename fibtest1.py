fibvalues = {
    0: 0,
    1: 1,
}


def fib(n):
    if n not in fibvalues:
        fibvalues[n] = fib(n - 1) + fib(n - 2)
    return fibvalues[n]


if __name__ == '__main__':
    for i in range(0, 20):
        print(f'fib({i:2}) ==> {fib(i):4}')
