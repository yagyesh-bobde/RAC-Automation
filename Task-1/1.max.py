n = int(input("Enter array size: "))
arr = []

for i in range(n) : 
    arr.append(int(input("Array {} element: ".format(i))))

maxNum = arr[0]

for i in range(1,n): 
    if(arr[i] > maxNum): 
        maxNum = arr[i]

print("Maximum of array is : {}".format(maxNum))