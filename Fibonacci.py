def fibb(n, a=0, b=1):
    if(n>0):
        print(a, end=" ")
        fibb(n-1,b,a+b)
fibb(10)
