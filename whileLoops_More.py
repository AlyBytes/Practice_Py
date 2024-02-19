# more of While Loops by AlyBytes

# a
#
# i = 1
# while i < 6:
#     print(i)
#     i += 1
#
# print()
#
# # b
# i = 2
# while i < 12:
#     print(i)
#     i += 3
#
# print()
#
# # c
# i = -10
# while i <= 0:
#     print(i, end=" ")
#     i += 2
#
# print()
#
# # d
# x = "*"
# i = 0
# while i < 4:
#     print(x * 4)
#     i += 1
# print()
#
# # 2
# def while_str(str):
#     i = 0
#     while i < len(str):
#         print(str[i])
#         i+=1
#
#
# while_str("CSCI 150")

def sum_and_avg():
    list = []
    prompt = "Please enter any number: "
    input_from_user = eval(input(prompt))

    while input_from_user != 0:

        list.append(input_from_user)
        input_from_user = eval(input(prompt))

    print("The sum of numbers entered is: ", sum(list), "and",
          "the average of your numbers is: ", sum(list) / len(list))
    print(sorted(list))


def main():
    print("here is your stuff: ", sum_and_avg())

main()

