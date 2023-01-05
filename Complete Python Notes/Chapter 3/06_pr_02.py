letter = '''Dear <|NAME|>
Greetings from ABC Coding house. I am happy to tell you about your selection.
You are selected!
Have a great day ahead!
Thanks and regards,
Bill
Date: <|DATE|>
'''
name = input ("Enter your name\n")
date = input ("Enter date\n")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)