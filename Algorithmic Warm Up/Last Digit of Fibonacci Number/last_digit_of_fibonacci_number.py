# python3


def last_digit_of_fibonacci_number_naive(n):
    assert 0 <= n <= 10 ** 7

    if n <= 1:
        return n

    return (last_digit_of_fibonacci_number_naive(n - 1) + last_digit_of_fibonacci_number_naive(n - 2)) % 10


def last_digit_of_fibonacci_number(n):
    assert 0 <= n <= 10 ** 7

    # if n == 0:
    #     return 0
    # elif n == 1:
    #     return 1
    #
    # fibo = [None]*(n+1)
    # fibo[0] = 0
    # fibo[1] = 1
    # for x in range(2,n+1):
    #     fibo[x] = fibo[x-1]+fibo[x-2]
    # return fibo[n]%10
    #other way
    # if n == 0 | n == 1:
    #     return n
    # a = 0
    # b = 1
    # c = 1
    # for x in range(2,n+1):
    #     c = a+b
    #     a = b
    #     b = c
    # return c%10
    #other way
    f = [0]*(n+1)
    if (n==0):
        return 0
    if (n == 1 or n==2):
        f[n] = 1
        return 1
    if (f[n] != 0):
        return f[n]
    if (n & 1):
        k = (n+1)//2
        f[n] = (last_digit_of_fibonacci_number(k)*last_digit_of_fibonacci_number(k)+last_digit_of_fibonacci_number(k-1)*last_digit_of_fibonacci_number(k-1))
    else:
        k = n//2
        f[n] = (2*last_digit_of_fibonacci_number(k-1)+last_digit_of_fibonacci_number(k))*last_digit_of_fibonacci_number(k)
    return f[n]%10

if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_fibonacci_number(input_n))
