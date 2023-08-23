class Solution:
    def kthSmallest(self,arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        arr.sort()
        return arr[k-1]

a=[7,10,4,3,20,15]
min=Solution().kthSmallest(a,0,len(a)-1,3)
print(min)