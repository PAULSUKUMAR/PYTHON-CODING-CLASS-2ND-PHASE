class Solution:
    def PalindromeOrNot(self,num):
        t=num
        s=0
        while(num!=0):
            r=num%10
            s=(s*10)+r
            num=num//10
        if(t==s):
            return True
        else:
            return False

num=int(input("Enter a Number:"))
s=Solution()
if s.PalindromeOrNot(num):
         print(num,"Is a palindrome")
else:
    print(num,"Is not a palindrome")             

