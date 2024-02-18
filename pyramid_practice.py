# practicing functions by AlyBytes


def pyramid(ch, n):
    for i in range(1, n + 1):
        print(ch * i)


def absolute_difference(x, y):
    return abs(x - y)


def is_even(num):
    if num % 2 == 0:
        print("this number is even")
    else:
        print("this number is odd")

    #return num%2 == 0


# tax_rate = 0.07
# tip_rate = 0.20

def calculate_total(meal, tax_rate, tip_rate):
    total_cost = meal * tip_rate + meal * tax_rate + meal
    return total_cost


def hey(num):
    return num * num


def there(n):
    k = 2
    if n > 0:
        for i in range(1, n):
            k *= 2
    elif n == 0:
        k = 1
    else:
        k = 0
    return k
    #if n < 0:
    #return 0
    #return 2**n


def are_we(num, string):
    print(string*num)

    # for i in range(num):
    #     print("Are we", string, "yet?", end =" ")
    # print()

def main():
    pyramid("*", 5)
    print(absolute_difference(200, -200))

    # testcase for abs diff
    print("difference between 10 and 5: ", absolute_difference(10, 5) == 5)

    # testcase for even or odd
    print(is_even(4))

    # testcase for calculate_total
    print("The total cost of $66.85 is: ", calculate_total(53.48, .07, .18) == 66.85)

    # testcase for hey
    print("5 squared is: ", hey(5), "and it's: ", hey(5) == 25)
    print("0 squared is: ", hey(0), "and it's: ", hey(0) == 0)
    print("-3 squared is: ", hey(-3), "and it's: ", hey(-3) == 9)

    # testcase for there
    print("2 in 5th power is: ", there(5))
    print("2 in 0 power is: ", there(0))
    print(there(3)==8)
    print(there(-2)==0)
    print(there(-6)==0)

    #testcase for there
    are_we(0, ' hey')
    # print('are_we(3,"there")')
    # are_we(3,"there")

main()
