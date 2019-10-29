def last_digit(n):
    a, b = 0, 1
    for i in range((n + 2) % 60):
        print('i',i)
        a, b = b, (a + b) % 10
        print('b',b)
        print('a',a)
    return 9 if a == 0 else a - 1

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(last_digit(n))
