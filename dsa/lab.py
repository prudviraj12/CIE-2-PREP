# def ms(a):
#     if len(a)<=1:
#         return a
#     m=len(a)//2
#     l=ms(a[:m]);
#     r=ms(a[m:])
#     i=j=0; 
#     res=[]
#     while i<len(l) and j<len(r):
#         if l[i]<r[j]:
#             res.append(l[i]); i+=1
#         else: 
#             res.append(r[j]); j+=1
#     return res+l[i:]+r[j:]
# a=list(map(int,input().split()))
# print(ms(a))
# # def qs(a,l,h):
#     if l<h:
#         p=a[h]; i=l-1
#         for j in range(l,h):
#             if a[j]<=p:
#                 i+=1; a[i],a[j]=a[j],a[i]
#         a[i+1],a[h]=a[h],a[i+1]
#         qs(a,l,i); qs(a,i+2,h)

# a=list(map(int,input().split()))
# qs(a,0,len(a)-1)
# print(a)
def eval_postfix(exp):
    s=[]
    for c in exp:
        if c.isdigit():
            s.append(int(c))
        else:
            b=s.pop(); a=s.pop()
            if c=='+': s.append(a+b)
            elif c=='-': s.append(a-b)
            elif c=='*': s.append(a*b)
            elif c=='/': s.append(a/b)
    return s[0]

print(eval_postfix(input()))