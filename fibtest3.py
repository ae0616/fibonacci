def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a

if __name__ == '__main__':
    for i in range(0,20):
        print(f'fib({i:2}) ==> {fib(i):4}')
