# fractional and recursions beginning by AlyBytes

def double(x):
    return 2 * x  # 10


def quad(x):
    return double(double(x))  # 2*(2*4)


def hello(name):
    print("Hello", name + ", how are you today?")


def repeat(string, n):
    return string * n  # prints hi 10 times


def square(string, n):
    for i in range(n):
        print(repeat(string, n))  # 4 rows of 4 stars


print(double(5))
print(quad(4))
hello("joey")
print(repeat("hi", 10))
square("*", 4)
