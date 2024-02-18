# loops by AlyBytes

# 1a
for i in range(1, 6):
    print(i)
print("")

# 1b
for i in range(2, 12, 3):
    print(i)
print("")

# 1c
for i in range(-10, 1, 2):
    print(i, end=" ")
print("")

# 1d
for i in range(4):
    print("****")
print("")

for i in range(4): #or for i in "****":
    print("*" * 4)
print("")

# nested loop
for i in range(4): #lines
    for n in range(4): #columns for each row
        print("*", end="")
    print()
print("")

# 2
str = "CSCI 150"
for char in str:
    print(char)
print("")

# 3
for i in range (1, 11):
    print(i)