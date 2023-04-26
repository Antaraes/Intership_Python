def bubbleSort(array):
    for i in range(len(array)):
        swapped = False
        for j in range(0,len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j + 1] = temp
                swapped = True
        if not swapped:
            break

def partition(array,low,high):
        pivot = array[high]
        i = low - 1
        for j in range(low,high):
            if array[j] <= pivot:
                i = i + 1
                (array[i],array[j]) = (array[j],array[i])

        (array[i+1],array[high]) = (array[high],array[i+1])

        return i + 1
def quickSort(array,low,high):
        if low < high:
            pi = partition(array,low,high)
            quickSort(array,low,pi-1)
            quickSort(array,pi+1,high)
def get_QuickSort(data:list):
    size = len(data)
    quickSort(data,0,size - 1)