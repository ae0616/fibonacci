a, b = 0, 1


def fibI():
    global a, b
    while True:
        a, b = b, a + b
        yield a


if __name__ == '__main__':
    f = fibI()
    for i in range(1, 20):
        print(f'fib({i:2}) ==> {next(f):4}')
