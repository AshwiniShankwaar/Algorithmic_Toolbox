# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3
    count = 0
    while money >0:
        if money >=10:
            money = money-10
            count = count+1
        elif money>=5 and money<10:
            money = money -5
            count = count+1
        else:
            money = money -1
            count = count+1

    return count



if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
