# Average Real Number by AlyBytes

total_sum = 0  # aggregator variable and must be initialized before the loop

for i in range(10):
    user_num = eval(input("Please enter a real number: "))
    total_sum += +user_num

print("Average number is: ", total_sum/10)
