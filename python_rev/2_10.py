# n=input()
# res=','.join(n)
# print(res)
# ------------------
# n=input()
# word=input()
# res=n.replace(word,"")
# print(res)
# -----------------------
# def con(sen):
#     words=sen.split()
#     res=""
#     for word in words:
#         new=""
#         for i in range(len(word)):
#             ch=word[i]
#             if i==0:
#                 if 'a'<=ch<='z':
#                     new+=chr(ord(ch)-32)
#                 else:
#                     new+=ch
#             else:
#                 if 'A'<=ch<='Z':
#                     new+=chr(ord(ch)+32)
#                 else:
#                     new+=ch
#         res+=new+" "
        
#     return res
# txt=input()
# print(con(txt))
# n=int(input())
# res=[i**2 if i%2==0 else i**3 for i in range(1,n)]
# print(res)
# -------------------------------
# l1 = ["apple", "banana", "cherry", "kiwi", "mango", "Papaya"]
# l2 = ["aPPLe", "BaNaNa", "ORANGE", "KiWi", "manGO", "Grape"]
# res=[]
# for i in l1:
#     for j in l2:
#         if i.lower()==j.lower():
#             res.append(i)
# print(res)
# ------------------------------------
# l1=list(map(int,input().split()))
# l2=list(map(int,input().split()))
# res=[]
# for i in l1:
#     for j in l2:
#         if i+j>=10:
#             res.append(i+j)
# print(res)
