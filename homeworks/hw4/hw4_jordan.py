#Homework 3

#This homework is meant to give you feel for how
#different algorithms can affect runtime.
#For this homework you will be required to implement two different
#sorting algorithms. You can choose from the ones we covered in class
#(not random sort) or use your own (there are lots if you spend some time
#searching online). The only constraint on the two that you pick is that they
#must be in different complexity classes. Most likely you will need to find
#something that is O(n^2) and O(nlogn) but feel free to find something exotic or
#make up your own.You must implement the sorting algorithms yourself.
#Once you have verified that your sorts are working properly (using tests),
#you will need to run a simulation and graph the results. Specifically, produce a
#graph with the following characteristics:
#• The vertical axis is some measure of time
#• The horizontal axis is N (size of set to sort)
#• You have one line for each sort algorithm, showing how time goes up with N
#• Everything is labeled appropriately
#Try to pick an N such that the effect is visually noticeable. It should not take
#a very large increase to make this possible.

#Bonus: Also graph quicksort. Note whether you are graphing average,
#best or worst case run-time. To test average run times try generating an array
#full of random numbers and sorting it. Do this a number of times and take the
#mean run-time.

#Merge Sort ~ O(nlog(n))
def mergesort(numbers):
#1) Recursively split the list in half until we have lists with size one
#specifies that if the list has more than 1 element...
    if len(numbers) > 1:
#...use floor division to locate the middle point...
        middle = len(numbers)//2
#...and then divide numbers list into two halves
        left = numbers[:middle]
        right = numbers[middle:]
#2) Merge each half that was split, sorting them in the process
#recursively sort the left half
        mergesort(left)
#recursively sort the right half
        mergesort(right)
#set indices
        i=0
        j=0
        k=0
#3) Compare the smallest elements of each half, with the smallest value being
#added to the sorted list, and continue comparing with each element (always
#selecting the smaller)
#sorts smaller of the numbers from the two halves into the list, while also
#changing the index of the element being compared
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                numbers[k] = left[i]
                i = i+1
            else:
                numbers[k] = right[j]
                j = j+1
            k = k+1
#check to see if any elements are left and changes indices accordingly
        while i < len(left):
            numbers[k] = left[i]
            i = i+1
            k = k+1
        while j < len(right):
            numbers[k]=right[j]
            j=j+1
            k=k+1
    return str(numbers)

#test
numbers1 = [14,46,43,27,57,41,45,21,70]
mergesort(numbers1)


#Quick Sort ~ O(n^2), O(n), or O(nlog(n))
def pivoting(numbers,low,high):
#1) Choose one value from the list that will serve as the pivot
#create index for smaller element
    i = (low-1)
#select the last element as the pivot
    pivot = numbers[high]
    for j in range(low, high):
#2) Move all elements smaller than the pivot to its left, and all elements
#larger than the pivot to its right
#If current element is smaller than or equal to pivot...
        if numbers[j] <= pivot:
#...then increment index of smaller element and swap them
            i = i+1
            numbers[i],numbers[j] = numbers[j],numbers[i]
    numbers[i+1],numbers[high] = numbers[high],numbers[i+1]
    return (i+1)

#3) Recursively sort the values around the pivot until the entire list is sorted
#now create second function to do quicksort
def quicksort(numbers,low,high):
    if low < high:
#label pivot index
        pivotx = pivoting(numbers,low,high)
#separately sort elements before pivot index and after pivot index
        quicksort(numbers, low, pivotx-1)
        quicksort(numbers, pivotx+1, high)
    return str(numbers)

#test
numbers1 = [14,46,43,27,57,41,45,21,70]
n = len(numbers1)
quicksort(numbers1,0,n-1)


#Plotting
import matplotlib.pyplot as plt
import time
import random

#create function to record time
def timing(n):
#list holding the times
    times=[]
#list holding the numbers
    numbers=[]
#appends each number in range to numbers list
    for i in range(0,n):
        numbers.append(i)
#shuffles the numbers list
    random.shuffle(numbers)
#starts recording time
    begin1 = time.time()
#runs mergesort function
    mergesort(numbers)
#stops recording time
    end1 = time.time()
#appends difference between start and stop times to times list
    times.append(100*(end1-begin1))
#starts recording time
    begin2 = time.time()
#runs quicksort function
    quicksort(numbers,0,(len(numbers)-1))
#stops recording time
    end2 = time.time()
#appends difference between start and stop times to times list
    times.append(100*(end2-begin2))
#returns times list
    return times

#creates dictionary of results for merge and quick sort
results={'Merge':[],'Quick':[]}
#sets range up to 303 numbers in numbers list
for j in range(3,303,3):
#calls the timing function made earlier
    tryitout=timing(j)
#appends merge times to "merge" in results dictionary
    results['Merge'].append(tryitout[0])
#appends quick times to "quick" in results dicitonary
    results['Quick'].append(tryitout[1])

#sets range again up to 303 numbers in numbers list
x = range(3, 303, 3)
#calls the times from the dictionary above
y1 = results['Merge']
y2 = results['Quick']
#based off plotting code from class
plt.subplots_adjust(left = .13, right = .95, top = .9, bottom = .3)
plt.plot(x, y1)
plt.plot(x, y2)
plt.legend(['mergesort', 'quicksort'], loc = "upper left", prop = {"size":10})
plt.ylabel("Time (seconds)")
plt.xlabel("Number of numbers")
plt.title("The Effect of Different Sort Algorithms on Runtime")
txt = """
Compares runtime for merge sort and quick sort
"""
plt.figtext(.5, .05, txt, fontsize = 10, ha = "center")
plt.savefig('plot.pdf')
