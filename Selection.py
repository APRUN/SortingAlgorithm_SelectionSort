import time
import random
#Function to generate Random number array
def RandomArray(size):
    Numbers=[]
#Assigning radom numbers to array
    for i in range(size):
        rand_number=random.randint(-50000,50000)
        Numbers.append(rand_number)
    return Numbers

#Function to get minimu element
def GetMinimum(arr,starting,ending):
    if(starting<=ending):
        min=starting
        for i in range(starting,ending):
            if(arr[i]<arr[min]):
                min=i
        return min
   
#Function for Selection sort
def SelectionSort(array,start,end):
    for i in range(0,end-1):
        min_index=GetMinimum(array, start, end)
        start=start+1
        array[i],array[min_index]=array[min_index],array[i]
    return array

#Getting Random Array
random_array=RandomArray(500000)
start_time=time.time()
array=SelectionSort(random_array,0,len(random_array))
end_time=time.time()
#Printng
print("Time: ",end_time-start_time)
print("Array: ",array)
#WriteDatatoFile(array, "C:\\Users\\Ahmad\\Downloads\\Khalil\\Lab2\\SortedSelectionSort.csv")
    
