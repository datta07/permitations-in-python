#writter-gurudatta
#algorithm-backtracking
#language-python
print("enter the word or number to have permitations")
a=input()
k=list(a)
c=[a]
n=1

for i in range(1,len(a)+1):
    n=n*i
print("they are permitations in",a)
def fun(p):
    global a
    global c
    for i in range(0,len(c)):
        if (p==c[i]):
           return False
    c.append(p)
    return True
def ass(j,b,k):
    global a
    if j==len(a):
       p=''.join(b)
       return fun(p)
    for i in range(0,len(a)):
        if k[i]!=0:
           b[j]=k[i]
           k[i]=0
           if (ass(j+1,b,k)):
              return True
           k[i]=a[i]
    return False
try:
    for i in range(0,n):
       ass(0,list(a),list(a))
       print(i+1,c[i])
    print('these are the ',i,'permitations')
    
except:
    print('these are the ',i,'permitations')
    