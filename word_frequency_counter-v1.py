sentence = "Co2 O2 H Li F Co2 Fe He Co2 O2 Na"
word =  sentence.split()
count = {}
for i in word:
    print(i) # to show the words (not necessary)
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
print(count)
