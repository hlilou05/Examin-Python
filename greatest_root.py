import math 
def greatest_root(a,b,c):
    delta=(b*b)-(4*a*c)
    assert a!=0 ,"c'est pas un polynome de deuxieme degre"
    assert a<=2 ,"c'est pas un polynome de deuxieme degre"
    if delta < 0:
        return None
    else:
        x1=(-b-math.sqrt(delta))/(2*a)
        x2=(-b+math.sqrt(delta))/(2*a)
        if x1 > x2 : 
            return x1
        else:
            return x2
print(greatest_root(2,0,0))
