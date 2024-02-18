saying = "howdy"
for u in saying.upper():
    print(saying.capitalize(), end="!! ")

print()

# just another average

x = 0
y = 0
for i in range (5):
    x += int(input("Please enter a number: "))
    y += 1

print(x)
print(y)
print(x/y)