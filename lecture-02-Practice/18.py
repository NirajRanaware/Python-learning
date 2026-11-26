text = input("Enter a word or sentence: ")

text = text.lower()

count = 0

if "a" in text:
    count = count + text.count("a")

if "e" in text:
    count = count + text.count("e")

if "i" in text:
    count = count + text.count("i")

if "o" in text:
    count = count + text.count("o")

if "u" in text:
    count = count + text.count("u")

print("Total vowels:", count)

