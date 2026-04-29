# n=input()
# res=','.join(n)
# print(res)
# ------------------
# n=input()
# word=input()
# res=n.replace(word,"")
# print(res)
# -----------------------
def con(sen):
    words=sen.split()
    res=""
    for word in words:
        new=""
        for i in range(len(word)):
            ch=word[i]
            if i==0:
                if 'a'<=ch<='z':
                    new+=chr(ord(ch)-32)
                else:
                    new+=ch
            else:
                if 'A'<=ch<='Z':
                    new+=chr(ord(ch)+32)
                else:
                    new+=ch
        res+=new+" "
        
    return res
txt=input()
print(con(txt))
