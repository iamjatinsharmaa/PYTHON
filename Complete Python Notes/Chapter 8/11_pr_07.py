def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

this = "     Jatin is a good      "
n = remove_and_split(this, "Jatin")
print(n)
# print(this)
# print(this.strip())
