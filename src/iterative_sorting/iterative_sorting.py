# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for x in range(i+1, len(arr)):
            if arr[smallest_index] > arr[x]:
                smallest_index = x     



        # TO-DO: swap

        arr[cur_index], arr[smallest_index] =\
        arr[smallest_index], arr[cur_index]




    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swap = True
    while swap == True:
        swap = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swap = True
    return arr


my_arr = [2, 9, 7, 5, 4, 1, 3, 8, 6]
print(my_arr)
my_arr = bubble_sort(my_arr)
print(my_arr)

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr