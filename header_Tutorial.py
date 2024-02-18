# tutorial by AlyBytes
# print a header of a given string(param1) and a symbol surrounding it (param2)

def header (text, surround_char):
    length = len(text) + 4
    # surround_char = "*"
    # text = "Hello World"

    print (surround_char *length)
    print (surround_char, text, surround_char)
    print (surround_char *length)

def main():
    header("TRalalalalalalala", "*")
    header("Python Rocks", "!")
    header("CODER 4 EVER", "+")

main()
