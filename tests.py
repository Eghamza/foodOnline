

def amp(arr=[]):
    arr1=[]
    
    a = len(arr)
    for i in range(a):
        if isinstance(arr[i],int):
            arr1.append(arr[i])

    mx =max(arr1)
    mn = min(arr1)
    result = mx-mn
    return print(f'the amplitude is {result}')

       

arr = [19,20,25,'error',18]
amp(arr)