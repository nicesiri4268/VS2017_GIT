def a(n):
    if n>2:
        n= a(n-1)+a(n-2)
        return n
    elif n==1 or n==2:
        n=1
        return n

def b(ns):
    a=[1,1]
    if ns>2:
        for n in range(2,ns):
            cout = a[n-1]+a[n-2]
            a.append(cout)
    return a

for n in range(1,10):
    cout= a(n)
    print(cout)
#f=b(50000)
#print (f)