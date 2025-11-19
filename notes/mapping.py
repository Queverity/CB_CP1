# CB 1st Mapping Notes

numbers = [234,643,796,476,946,357,758,754]
"""new_nums = []

for number in numbers:
    new_nums.append(number/3)

print(new_nums)"""


new_nums = map(lambda num:num/3, numbers)
for num in new_nums:
    print(num)