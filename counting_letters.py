import pprint # import the pprint module for nice text printing at the end

message = 'Today is Monday, and it is just before lunch.'
count = {} #this is the count dictionary we're creating. But it's empty. The For Loop below will populate it.

for character in message.upper(): # The For Loop will run through each index of the string above.
    count.setdefault(character, 0) # we're using the setdefault method where it starts 'character' off at 0.
    count[character] = count[character] + 1 # The For Loop runs through each index, notes the letter, then adds a count of 1 to that letter's count. The loop again.

counttext = pprint.pformat(count)
print(counttext)

#change message to message.upper if you wish to run through the loop looking for capital letters.