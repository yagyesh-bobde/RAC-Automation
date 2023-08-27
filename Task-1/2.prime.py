def isPrime(num) :
    flag = 0
    if(num == 1 or num == 0): 
        return False 
    for i in range(2, num//2) : 
        if(num % i == 0) : 
            return False
    return True

n = int(input("Enter array size: "))
arr = []

for i in range(n) : 
    arr.append(int(input("Array {} element: ".format(i))))


for i in range(n) : 
    if(isPrime(arr[i])) : 
        print(f"Number-{arr[i]} is prime")