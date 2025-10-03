# CB 1st While Loops Notes
import random
import time

num = 1

# while num <= 20:
    # time.sleep(1)
    # print(num)
    # num += 1

goose = random.randint(1,20)
count = 0

while True:
    if count == goose:
        break
    else:
        print("Duck")
        count += 1
        time.sleep(.5)
else:
    print("GOOSE!")