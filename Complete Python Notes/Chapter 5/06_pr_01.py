myDict ={
    "Pankha" : "Fan",
    "Dabba" : "Box",
    "Vastu" : "Item"
}
print("Options are ", myDict.keys())
a = input("Enter the Hindi word\n")
# print("The meaning of word is", myDict[a])

print("The meaning of word is", myDict.get(a))
