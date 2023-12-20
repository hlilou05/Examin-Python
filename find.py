def find(x,l):
    a = 0
    b = len(l)-1
    def z(a,b):
        if a > b :
            return None
        m=(a+b)//2
        if l[m]==x :
            return m
        elif l[m] > x:
            return z(a,m-1)
        elif l[m] < x:
            return z(a,m+1)
        
assert find(3,[3]) == 0
assert all( (fe:=find(ie:=i,ir:=r)) == (i if 0<=i<N else None)
    for N in range(9) for r in [range(N)]
    for i in list(r)+[-1,N] ), (ir, ie, fe)
assert all( l[fe:=find(ie:=i,il:=l)] == i
    for N in range(5) for R in [2,3]
    for l in [[ e for e in range(N) for _ in range(R) ]]
    for i in range(N)), (il, ie, fe)
