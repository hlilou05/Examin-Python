def celsius_to_farenheit(C):
    assert C >= -273.15
    return (9/5)*C + 32
def farenheit_to_celsius(F):
    assert F>= -459.67
    return (F-32)*5/9
def isalmost(n,m,d=1):
    assert isalmost( farenheit_to_celsius(-459.67),-273.15,1e-13)
    return (abs(n-m) <= d)
print(farenheit_to_celsius(-459.67))