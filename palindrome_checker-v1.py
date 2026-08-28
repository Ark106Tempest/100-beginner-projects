word = "lol"
forword = ""
backword = ""
for x in word:
    forword = forword + x
for y in reversed(word):
    backword = backword + y
if forword == backword:
    print("palindrome: True")
else:
    print("palindrome: False")
