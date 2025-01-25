def two_sum(arr,tar):
    print(arr)
    for i in arr:
        for j in range(i+1,len(arr)):
            if tar==arr[i]+arr[j]:
                return i,j
input_array=[1,2,3,4]
target_value=6
print(two_sum(input_array,target_value))