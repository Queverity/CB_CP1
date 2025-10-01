# CB 1st For Loops Notes
import time

nums = [145,23664,52346,4213,6,41,421]

for num in nums:
    num /= 2
    if num > 100:
        print(f"{num} is only half of {num*2}. It is a large number.")
    else:
        print(num)

print("The loop is over!")

for num in range(1,15):
    print(num)
    time.sleep(1)

for num in range(20,0,-2):
    print(num)
    time.sleep(2)