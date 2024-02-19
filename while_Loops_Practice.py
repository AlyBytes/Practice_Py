# a.
j = 4 # loop variable : it's being used as part of while condition and also changes at the end
while j > -4:
    print(j)
    j -= 1          # 4, 3, 2, 1, 0, -1, -2, -3

# b.
string = "Hello"
builder = "" # aggregator or accumulator
i = 0
while i < len(string):
    builder += string[i].swapcase()
    print(i, builder)
    i += 1
    print(string, "->" , builder)   # hELLO

# c.
x = 0
i = 1
while x < 20:
     if x > 5:
        x += 15
     else:
        x += 1
     print(i, x)     # 1, 1;  2,2; 3,3; ...19,19
     i += 1



x = 0
while x < 20:
    if x>5:
        if x%2==0:
            x*=2
        else:
            x*= -1
    else:
        x+=10           # 10  11   -11  -10  0  1  11   12   24   25
    x+=1
print(x)
