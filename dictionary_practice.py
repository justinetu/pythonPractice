words = input("> ")

emojis = {
    ":)" : "😁",
    ":(" : "😒",
    ":D" : "😂"
}
output = ""
message = words.split(' ')
for word in message:
    output += emojis.get(word, word) + " "
print(output)
