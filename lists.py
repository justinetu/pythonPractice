# A simple program that gets the maximum value within a list
numbers = [10,2,4,11,5]
max = numbers[0]
for num in numbers[1:]:
    if num > max:
        max = num
print(max)
