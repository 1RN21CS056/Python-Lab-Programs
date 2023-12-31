# 4a) Insertion + mergeSort
def insertionSort(arr, n):
    for i in range(1, n):
        temp = arr[i]
        j = i-1
        while(j>=0 and arr[j] > temp):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp
    return arr

def mergeSort(arr, l, h):
    if l<h:
        mid = (l+h)//2
        mergeSort(arr, l, mid)
        mergeSort(arr, mid+1, h)
        merge(arr, l, mid, h)

def merge(arr, l, m, h):
    k = i = l
    j = m + 1
    B = [None]*len(arr)
    while i<=m and j<=h:
        if arr[i] < arr[j]:
            B[k] = arr[i]
            i += 1
        else:
            B[k] = arr[j]
            j += 1
        k += 1

            
    while i<=m:
        B[k] = arr[i]
        i += 1
        k += 1 
        
    while j<=h:
        B[k] = arr[j]
        j += 1
        k += 1
        
    i = l
    while(i<=h):
        arr[i] = B[i]
        i += 1
        
    return arr

n = int(input("Enter no of elements: "))
arr = [None]*n
print("Enter elements: ")
for i in range(n):
    arr[i] = int(input())
    
print("Before Sorting : ",arr)
mergeSort(arr, 0, len(arr)-1)
print("After Merge Sort : ",arr)
insertionSort(arr,n)
print("After Insertion sort : ",arr)