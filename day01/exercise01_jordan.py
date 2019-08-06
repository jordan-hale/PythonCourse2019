## Fibonacci sequence
## X_[i] = X_[i-1] + X_[i-2], where X_1 = 1, X_2 = 1
## 1,1,2,3,5,8,....

## Write a for loop, while loop, or function (or all three!) to create a
## list of the first 10 numbers of the fibonacci sequence

fibonacci = []
for i in range(1, 11):
    if i  == 1 or i == 2: fibonacci.append(1)
    else: fibonacci.append(sum([fibonacci[i - 2], fibonacci[i - 3]]))

fibonacci

"""return true if there is no e in 'word', else false"""


"""return true if there is e in 'word', else false"""


"""return true if word1 contains only letters from word2, else false"""


"""return true if word1 uses all the letters in word2, else false"""


"""true/false is the word in alphabetical order?"""
