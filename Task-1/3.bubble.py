def bubbleSort(arr) :
    for i in range(n-1) : 
        for j in range(n-i-1) : 
            if(arr[j] > arr[j+1]): 
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

n = int(input("Enter array size: "))
arr = []

for i in range(n) : 
    arr.append(int(input("Array {} element: ".format(i))))

print("Before Sorting: " , arr)
bubbleSort(arr)
print("After Sorting: " , arr)