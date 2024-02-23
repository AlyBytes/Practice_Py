# def add(x,y):
#     print("It will add numbers %d and %d" %(x,y))
#     return x+y
#
# sum = add(2,3)
# print("=", sum)


# def compareTriplets(a, b):
#     count_a = 0
#     count_b = 0
#     new_arr = []
#
#     for i in range(3):
#         numAlice = int(a[i])
#
#         print(i)
#         print(numAlice)
#         for n in range(3):
#
#             numBob = int(b[n])
#             print(n)
#
#             print(numBob)
#             if numAlice > numBob:
#                 count_a += 1
#
#             elif numAlice < numBob:
#                 count_b += 1
#
#             else:
#                 n=i
#                 continue
#
#     new_arr.append(count_a)
#     new_arr.append(count_b)
#     print(new_arr)

def mix(a, b):
    new_str=""


    for let_str1 in a:
        new_str+=let_str1
        for let_str2 in b:
            if a.index(let_str1) == b.index(let_str2):
                new_str+=let_str2

    return new_str
def main():
    # a = [5, 6, 7]
    # b = [3, 6, 10]
    # compareTriplets(a, b)

    print("mix:         ", mix("1234", "ab"))


main()
