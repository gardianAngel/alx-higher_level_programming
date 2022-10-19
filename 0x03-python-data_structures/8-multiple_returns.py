#!/usr/bin/python3
def multiple_returns(sentence):
    '''My multiple return function
    Arg:
        sentence: String

    Returns:
        A tuple: (length, first_char)
    '''
    temp = []
    if sentence  ==  '':
        temp.append("none")
    else:
        temp.append(len(sentence))
        temp.append(sentence[0])
        print(temp)
        final_tuple = tuple(temp)
        return final_tuple


