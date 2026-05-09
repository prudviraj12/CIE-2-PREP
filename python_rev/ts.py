n=input()
p=len(n)//2
q=len(n)
valid=True
for i in range(len(n)):
    l=n[i]
    m=n[q-1-i]
    if l!=m:
        valid=False
        break
if valid:
    print("yes")
else: 
    print("nno")
    