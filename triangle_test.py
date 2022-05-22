
def triangle_atom(a,b,c):
    if (a<=0 or a>800) or (b<=0 or b>800)  or (c<=0 or c>800):
        return 'OutOfRange'
    if a + b > c and a + c > b and b + c > a:
        if a == b or a == c or b == c:
            if a == b and b == c:
                return 'Equilateral'
            else:
                return 'Isosceles'
        else:
            return 'Normal'
    else:
        return 'Non'
