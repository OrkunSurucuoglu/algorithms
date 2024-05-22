from random import randint

def binary_search(arr: list[int], x: int) -> int:
    if arr is None:
        return -1
        
    l, r = 0, len(arr) - 1
    
    while l <= r:
        mid = l + (r - l) // 2
        if x == arr[mid]:
            return mid
        elif x < arr[mid]:
            r = mid - 1
        else:
            l = mid + 1
    
    return -1
    
if __name__ == '__main__':
    arr = []
    for i in range(30):
        arr.append(randint(1,100))
    
    arr.sort()
    x = randint(1,100)
    
    index = binary_search(arr, x)
    if index == -1:
        print(f'{x} does not exist in {arr}')
    else:
        print(f'{x} exists in {arr}')
        
        
    
