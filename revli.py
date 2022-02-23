l=[]
n=int(input('enter number: '))
for i in range(1,n+1):
    x=int(input())
    l.append(x)
print(l)
t=l[n-1]
for i in range(n):
    l[i]=t
    s=n-i-2
    t=l[s]
print(l)
