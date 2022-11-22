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

for ch in phone_number:
    str += numbers.get(int(ch), "!") + " "
print(str)
