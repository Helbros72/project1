first_phrase = ['Believe', 'you', 'can']
second_phrase = ['Clear', 'the', 'air']
_under = []
i = 0
phrase = int(input(' Choose phrase : 1 or 2 '))
print();
print(' Guess phrase :');
print()
if phrase == 1:
    _under = ['_' * len(_word) for _word in first_phrase]
    _phrase = first_phrase
else:
    _under = ['_' * len(_word) for _word in second_phrase]
    _phrase = second_phrase
print(_under)
success_letters = []
while True:
    _letter = input('Enter letter : ')
    count = 0

    for _word in _phrase:
        count += _word.count(_letter)
    if count == 0:
        print('No')
        i -= 1
    else:
        success_letters.append(_letter)
        i += 5
        print('You guess ! ')
        print('Your score :', i)
    # print word with underscores:
    under_phrase = ''
    for _word1 in _phrase:
        for l in _word1:
            if l in success_letters:
                under_phrase += l
            else:
                under_phrase += '_'
        under_phrase += ' '
    print(under_phrase)
    if '_' not in under_phrase:
        print()
        print('Game over')
        print()
        print('YOUR SCORE !!!', i)
        break;
