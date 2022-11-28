# @arg arr The input list like object to be sorted
# @arg cmp A compare function which takes two element in the array, 
#          cmp(a,b)<0   if a should be placed before b,
#          cmp(a,b)==0  if arr is still sorted after a and b are exchanged,
#          cmp(a,b)>0   if a should be placed behind b.
def multi_sort(arr, cmp, method="None"):
    if(method=="quick"):
        quick_sort(arr,cmp)
    elif(method=="merge"):
        merge_sort(arr,cmp)
    elif(method=="None"): # do nothing
        return
    else:
        print("invalid argument!")

# must be in-place sort
def merge_sort(arr,cmp):
    #pass
    if len(arr) > 1:
        i = 0
        j = 0
        k = 0
        half = len(arr)//2
        leftSide = arr[:half]
        rightSide = arr[half:]

        merge_sort(leftSide)
        merge_sort(rightSide)

        while i < len(leftSide) and j < len(rightSide):
            if leftSide[i] <= rightSide[j]:
                arr[k] = leftSide[i]
                i = i + 1

            else:
                arr[k] = rightSide[j]
                j = j + 1

            k = k + 1

        while i < len(leftSide):
            arr[k] = leftSide[i]
            i = i + 1
            k = k + 1

        while j < len(rightSide):
            arr[k] = rightSide[j]
            j = j + 1
            k = k + 1

# must be in-place sort
def quick_sort(arr,cmp):
    #pass
    bot = 0
    top = len(arr) - 1

    if bot < top:
        x = partition( arr, bot , top)
        z = x

        while x != bot:
            y = partition( arr , bot , x - 1)
            x = x - 1
        
        while z != top:
            a = partition(arr , z + 1 , top)

def partition ( arr , bot , top):
    x = arr[top]
    i = bot - 1
    
    for j in range( bot, top):
        if arr[j] <= x:
            i = i + 1
            (arr[i],  arr[j]) = (arr[j] , arr[i])
    
    ( arr[i + 1] , arr[top]) = (arr[top], arr[i +1])

    return i + 1
