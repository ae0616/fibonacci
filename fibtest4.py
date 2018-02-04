a, b = 0, 1


def fib_iter():
    global a, b
    while True:
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    f = fib_iter()
    for i in range(0, 20):
        print(f'fib({i:2}) ==> {next(f):4}')
