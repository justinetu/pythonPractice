#Simple program that converts numbers to words
numbers = {
    0: "Zero",
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7:"Seven",
    8: "Eight",
    9: "Nine"
}
phone_number = input("Phone: ")
str = ""
list = []
for num in phone_number:
    str += num
    list.append(int(num))

for i in list:
    if i in numbers:
        print(numbers.get(i), end = " ") #end will print things on one line
