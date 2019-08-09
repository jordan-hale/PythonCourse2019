## Write a function that counts how many vowels are in a word

def count_vowels(word):
    return sum([j in ['a', 'e', 'i', 'o', 'u'] for j in [i for i in word]])

## Raise a TypeError with an informative message if 'word' is passed as an integer

def count_vowels(word):
    try:
        sum([j in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'] for j in [i for i in word]])
    except TypeError:
        print("Make sure you enter in a string")
    else:
        return sum([j in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'] for j in [i for i in word]])

## When done, run the test file in the terminal and see your results.
