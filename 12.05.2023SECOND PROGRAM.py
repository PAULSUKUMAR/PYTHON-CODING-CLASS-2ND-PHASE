class Solution:
    def pivotIndex(self, arr):
        n=len(arr)
        for i in range(0,n):#i=2
            lsum=0
            rsum=0
            for j in range(0,i):#left sum
                lsum=lsum+arr[j]#0
            for k in range(i+1,n):#right sum
                rsum=rsum+arr[k]
            if lsum==rsum:
                return i
        return -1
