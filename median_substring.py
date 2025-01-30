l1=[1,2]
l2=[3,5,4]
def median(l1,l2):
    temp=[]
    for i in range(len(l1)):
        val=min(l1)
        l1.remove(val)
        temp.append(val)
        l1.pop
        
    del l1
    temp2=[]
    for i in range(len(l2)):
        val=min(l2)
        l2.remove(val)
        temp2.append(val)
    del l2
    result=temp+temp2
    mid=len(result)
    if mid==0:
        return 0
    elif mid%2!=0:
        return result[mid//2]
    else:
        return (mid+(mid//2-1))//2
        
print(median(l1,l2))


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def sort(list):
            num=[]
            for i in range(len(list)):
                val=min(list)
                list.remove(val)
                num.append(val)
            return num
        num_list=nums1+nums2
        num3=sort(num_list)
       
        del nums1,nums2
        print(num3)
        length=len(num3)

        if length==0:
            return 0
        elif length%2!=0:
            return num3[int(length//2)]
        else:
            return ((num3[length//2]+num3[length//2-1])/2)
