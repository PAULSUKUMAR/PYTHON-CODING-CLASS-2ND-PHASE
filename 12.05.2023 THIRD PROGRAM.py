# User function Template for python3

class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        # Your code here
        for i in range(0,N):#i=2
            lsum=0
            rsum=0
            for j in range(0,i):#left sum
                lsum=lsum+A[j]#0
            for k in range(i+1,N):#right sum
                rsum=rsum+A[k]
            if lsum==rsum:
                return i
        return -1



#{ 
 # Driver Code Starts
# Initial Template for Python 3

import math


def main():

    T = int(input())

    while(T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]
        ob=Solution()

        print(ob.equilibriumPoint(A, N))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
