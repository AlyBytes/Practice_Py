# what does this program output when it's:
# Mon? Sat? Sun? Raining?

DoW = input("What day is it? ").lower()
# DoW = DoW.lower()
if DoW == "saturday":
    print("Wake up at 9am")
elif DoW == "sunday":
    print("Wake up at 10 am")
else:
    print("Wake up at 7 am")
