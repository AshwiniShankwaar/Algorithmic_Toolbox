# python3
import array as arr

def fibonacci_number_naive(n):
    assert 0 <= n <= 45

    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n):
    assert 0 <= n <= 45
    if n == 0:
        return 0
    elif n == 1:
        return 1

    fibo = [None]*(n+1)
    fibo[0] = 0
    fibo[1] = 1
    for x in range(2,n+1):
        fibo[x] = fibo[x-1]+fibo[x-2]
    return fibo[n]







if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
