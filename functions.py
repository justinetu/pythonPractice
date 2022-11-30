def emoji_converter(words):
    emojis = {
        ":)": "😁",
        ":(": "😒",
        ":D": "😂"
    }
    output = ""
    message = words.split(' ')
    for word in message:
        output += emojis.get(word, word) + " "
    return output

words = input("> ")
result = emoji_converter(words)

print(result)
