
first_phrase = [ 'Believe', 'you', 'can' ]
second_phrase = [ 'Clear' , 'the' , 'air' ]
_under=[]
i = 0
j = 0
phrase = int (input ( ' Choose phrase : 1 or 2 '))
#def print_cavim () :
print(); print (' Guess phrase :'); print()
if phrase == 1 :
    _under = ['_' * len(_word) for _word in first_phrase]
else :
    _under = ['_' * len(_word) for _word in second_phrase]
print(_under)

# this is more complicated than a list of letters
#def _phrase () :
    #i = 0
_letter = input('Enter letter : ')
for _word_index in range(len(first_phrase)):
    new_word = ''
    for _letter_index in range(len(first_phrase[_word_index])):
            #print(first_phrase[_word_index][_letter_index], end=' ')
        if first_phrase[_word_index][_letter_index] == _letter:
            new_word += _letter
            i += 5
            print('You guess ! ')
            print('Your score :', i)


        else :
            new_word += _under[_word_index][_letter_index]
    _under[_word_index] = new_word

print(_under)




