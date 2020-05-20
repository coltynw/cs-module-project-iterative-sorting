# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for x in range(i + 1, len(arr)):
            if arr[cur_index] > arr[x]: #if the current index is smaller than the smallest
                cur_index = x #assign the current index to be the new smallest
#write 2 loops, nested loops


        # TO-DO: swap
        # Your code here
        temp = arr[i] #swap index i with smallest position
        arr[i] = arr[cur_index]
        arr[cur_index] = temp

        # print(arr)
# selection sort allows for the minimum number of swaps
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    for i in range(0, len(arr)): #first for loop
        #the first loop is to make sure you get the biggest element at the end
        for x in range(0, len(arr) - i - 1): #2nd for loop using first as parameter
            #the 2nd loop is to do it again and make sure the smallest element is first
            if arr[x] > arr[x +1]: #if the first number is better than the 2nd, swap
                temp = arr[x] #all of this is just the process of swapping
                arr[x] = arr[x + 1] 
                arr[x + 1] = temp


    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here


    return arr
