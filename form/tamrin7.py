string = 'salam man amir hastam, khushbakhtam.'

counter = dict()

for letter in string:
    if letter in counter:
        counter[letter] = counter.get(letter, 0) + 1
for this_one in list(counter.keys()):
    print ('%s appeared %s time' %(this_one, counter[this_one]))