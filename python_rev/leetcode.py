# n=input()
# p=len(n)//2
# q=len(n)
# valid=True
# for i in range(len(n)):
#     l=n[i]
#     m=n[q-1-i]
#     if l!=m:
#         valid=False
#         break
# if valid:
#     print("yes")
# else: 
#     print("nno")
# def nga(n,s):
#     res=n*s
#     print(res,end=" ")
# nga(2,"reddy")
# 2011. Final Value of Variable After Performing Operations
# class Solution(object):
#     def finalValueAfterOperations(self, operations):
#         x = 0
        
#         for op in operations:
#             if op == "--X" or op == "X--":
#                 x -= 1
#             else:
#                 x += 1
                
#         return x

class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans=""
        for i in address:
            if i==".":
                ans+="[.]"
            else:
                ans+=i
        return ans