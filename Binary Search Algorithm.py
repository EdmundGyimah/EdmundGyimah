#Binary Search is a search operation that works by repeatedly splitting a set of data in half till the target value is found.

#A function that takes a list and target parameter
#Multiple variables: Start, Middle, End, Steps(Number of times the search is done)
#Recursion or While Loop(Manual Entry)
#Increase the steps each time a split is done
#Conditions to track target position

def binary_search(list, element):
    middle = 0
    start = 0
    end = len(list)
    steps = 0

    while(start<=end):
        print("Step",steps, ":" ,str(list[start:end+1]))

        steps = steps+1
        middle = (start + end) // 2

        if element == list[middle]:
            return middle
        if element < list[middle]:
            end = middle -1
        else: 
            start = middle + 1

    return -1

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
target = 12

binary_search(my_list, target)
