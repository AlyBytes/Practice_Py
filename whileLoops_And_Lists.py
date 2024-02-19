# more on whileD loops by AlyBytes

def average_neg_evens(list):
    #list = []
    count = 0 #aggregator variables
    i=0
    n = 0
    # for num in range(len(list)):
    #     if num < 0 and num % 2 == 0:
    #         count += i
    #         n += 1
    #   #  continue
    while i <len(list):
        if list[i] < 0 and list[i] % 2 == 0:
            count += list[i]
            n += 1
        i += 1

    return count / n


def count_letter(list_str, letter):
    count = 0
    letter =letter.upper()
    for i in list_str:
        count += i.upper().count(letter)
      #  count += i.lower().count(letter)

    return count
def main():
    list = [0, 1, 2, -2, -3, -4, 3, 4]
    # test print("Average is: ", average_neg_evens(list)==-3)
    print("Average is: ", average_neg_evens(list))

    list_str = ["HELLO", "goodbye", "1234 Oooh!"]
    print ("count letter is: ", count_letter(list_str, 'O'));

main()
