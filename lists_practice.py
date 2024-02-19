# practicing lists and strings by AlyBytes

def average_num():
    list = []
    for i in range(20):
        list.append(eval(input("Please enter any number: ")))
        # num = eval(input"Please enter a number: ")
        # list.append(num)

    print("The average of your numbers is: ", sum(list) / len(list))


def mangle(str):
    length_of_str = len(str)
    str1 = str.upper()
    str_new = str1[0:2] + (str1[3:- 3]) + (str1[- 2:])
    return str_new


def count_e(list_str):
    count = 0
    # for num in list_str:
    #     if num.count('e') > 0 or num.count('E') > 0:
    #         count += num.count('E') + num.count('e')

    for string in list_str:
        count += string.upper().count("E")

    return count


def count_vowels(list_str):
    count = 0
    # for num in list_str:
    #     if num.count('e') > 0 or num.count('E') > 0:
    #         count += num.count('E') + num.count('e')
    #     elif num.count('a') > 0 or num.count('A') > 0:
    #         count += num.count('a') + num.count('A')
    #     elif num.count('i') > 0 or num.count('I') > 0:
    #         count += num.count('i') + num.count('I')
    #     elif num.count('o') > 0 or num.count('O') > 0:
    #         count += + num.count('o') + num.count('O')
    #     elif num.count('u') > 0 or num.count('U') > 0:
    #         count += + num.count('u') + num.count('U')
    for string in list_str:
        upper = string.upper()
        for vowel in "AEIOU":
            count += upper.count(vowel)
        # count += upper.count("E")
        # count += upper.count("A")
        # count += upper.count("O")
        # count += upper.count("U")
        # count += upper.count("I")
    return count


def main():
    # average_num()

    test_input = ["hellothere", "42 degrees Celsius", "eeeeeee"]
    test_output = ["HELOTHRE", "42DEGREES CELSUS", "EEEEE"]
    for i in range(len(test_input)):
        print("Mangle", test_input[i] + ":", mangle(test_input[i]) == test_output[i])

    # print(mangle("hellothere")=="HELOTHRE")
    # print(mangle("42 degrees Celsius")=="42DEGREES CELSUS")
    # print(mangle("eeeeeee")=="EEEEE")

    # print(count_e(["hi”, “hello”, “EEeeK!"])) #working function call
    print("count E", count_e(["hi”, “hello”, “EEeeK!"]) == 5)  # test
    print("count vowels", count_vowels(["hi", "hello", "OOF!"]))


main()
