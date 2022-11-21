numbers = [2,4,6,3,2,3]
for num in numbers:
    if numbers.count(num) == 2:
        numbers.remove(num)
print(numbers)
