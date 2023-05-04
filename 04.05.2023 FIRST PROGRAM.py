class Solution:
    def LeapOrNot(self,year):
        if((year%4==0)and((year%400==0)or(year%100!=0))):
            return True
        else:
            return False

year=int(input("Enter The Year:"))
s=Solution()
if s.LeapOrNot(year):
         print(year,"Is a leap Year ")
else:
    print(year," Is not a leap year")   
