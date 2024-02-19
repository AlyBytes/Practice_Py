# def add(x,y):
#     print("It will add numbers %d and %d" %(x,y))
#     return x+y
#
# sum = add(2,3)
# print("=", sum)


def compareTriplets(a, b):
    count_a = 0
    count_b = 0
    new_arr = []

    for i in range(3):
        numAlice = int(a[i])

        print(i)
        print(numAlice)
        for n in range(3):

            numBob = int(b[n])
            print(n)

            print(numBob)
            if numAlice > numBob:
                count_a += 1

            elif numAlice < numBob:
                count_b += 1

            else:
                n=i
                continue

    new_arr.append(count_a)
    new_arr.append(count_b)
    print(new_arr)


def main():
    a = [5, 6, 7]
    b = [3, 6, 10]
    compareTriplets(a, b)


main()
