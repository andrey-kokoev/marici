"""Generic interval-series certificate attempt for the order-two Hausdorff corner."""
import itertools, json, math
from decimal import Decimal
from fractions import Fraction
from pathlib import Path
from eta_order_six_decimal_interval import intervals, down, up, add as add2, neg

def add(*xs):
    z=(Decimal(0),Decimal(0))
    for x in xs:z=add2(z,x)
    return z
def sub(x,y):return add(x,neg(y))
def mul(x,y):
    lo=[down.multiply(a,b) for a in x for b in y]
    hi=[up.multiply(a,b) for a in x for b in y]
    return min(lo),max(hi)
def qbox(q):
    return (down.divide(Decimal(q.numerator),Decimal(q.denominator)),
            up.divide(Decimal(q.numerator),Decimal(q.denominator)))
def scale(q,x):return mul(qbox(q),x)
def divp(x,y):
    assert y[0]>0
    return mul(x,(down.divide(Decimal(1),y[1]),up.divide(Decimal(1),y[0])))
def powi(x,n):
    z=qbox(Fraction(1))
    for _ in range(n):z=mul(z,x)
    return z

def atan_box(q,terms):
    s=Fraction(0)
    for k in range(terms):s+=(-1)**k*q**(2*k+1)/(2*k+1)
    t=s+(-1)**terms*q**(2*terms+1)/(2*terms+1)
    return min(s,t),max(s,t)
a5,a239=atan_box(Fraction(1,5),80),atan_box(Fraction(1,239),30)
pi=qbox(Fraction(1))
pi=(down.divide(Decimal((16*a5[0]-4*a239[1]).numerator),Decimal((16*a5[0]-4*a239[1]).denominator)),
    up.divide(Decimal((16*a5[1]-4*a239[0]).numerator),Decimal((16*a5[1]-4*a239[0]).denominator)))
logpi=(down.next_minus(down.ln(pi[0])),up.next_plus(up.ln(pi[1])))

def zeta_integer(p,m=300):
    row=[Fraction(1,n**p) for n in range(1,m+2)]
    s=Fraction(0);two=2
    for _ in range(m):
        s+=row[0]/two
        row=[row[i]-row[i+1] for i in range(len(row)-1)];two*=2
    err=Fraction(1,2**m)
    factor=Fraction(1,1-Fraction(2,2**p))
    return qbox(factor*(s-err)),qbox(factor*(s+err))

zetas={p:(zeta_integer(p)[0][0],zeta_integer(p)[1][1]) for p in range(2,7)}
L=intervals[0]
eta=[scale(Fraction(1,math.factorial(k)),intervals[k]) for k in range(7)]
etap=[scale(Fraction(k+1),eta[k+1]) for k in range(6)]
q=[]
for n in range(6):
    numerator=etap[n]
    for k in range(1,n+1):numerator=sub(numerator,mul(eta[k],q[n-k]))
    q.append(divp(numerator,eta[0]))

g0=divp(add(eta[1],scale(Fraction(1,2),powi(L,2))),L)
ell=[]
for n in range(6):
    inv=qbox(Fraction((-1)**n))
    B=qbox(Fraction(0))
    if n==0:B=scale(Fraction(1,2),L)
    if n==1:B=scale(Fraction(-1,12),powi(L,2))
    if n==3:B=scale(Fraction(1,720),powi(L,4))
    if n==5:B=scale(Fraction(-1,30240),powi(L,6))
    if n==0:
        gamma=add(scale(Fraction(-1,2),g0),neg(L))
        constant=scale(Fraction(-1,2),logpi)
    else:
        gamma=scale(Fraction((-1)**(n+1)*(2**(n+1)-1),2**(n+1)),zetas[n+1])
        constant=qbox(Fraction(0))
    ell.append(add(inv,B,constant,gamma,q[n]))

# The squared-coordinate Stieltjes function is L(s)/(2s-1), not L(s).
# With s=1+e, multiply by (1+2e)^(-1).
reduced=[]
for n in range(6):
    reduced.append(add(*(scale(Fraction((-2)**k),ell[n-k]) for k in range(n+1))))

def poly_mul(a,b,degree=5):
    out=[qbox(Fraction(0)) for _ in range(degree+1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j<=degree:out[i+j]=add(out[i+j],mul(x,y))
    return out
E=[qbox(Fraction(x)) for x in (0,1,-1,2,-5,14)]
powers=[[qbox(Fraction(1))]+[qbox(Fraction(0)) for _ in range(5)]]
for _ in range(5):powers.append(poly_mul(powers[-1],E))
S=[qbox(Fraction(0)) for _ in range(6)]
for n in range(6):
    for k in range(6):S[k]=add(S[k],mul(reduced[n],powers[n][k]))
A=[scale(Fraction((-1)**k),S[k]) for k in range(6)]

def det3(matrix):
    total=qbox(Fraction(0))
    for p in itertools.permutations(range(3)):
        inversions=sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
        term=qbox(Fraction(1))
        for i in range(3):term=mul(term,matrix[i][p[i]])
        total=add(total,term if inversions%2==0 else neg(term))
    return total
ordinary=[[A[i+j] for j in range(3)] for i in range(3)]
lower=[[A[i+j+1] for j in range(3)] for i in range(3)]
upper=[[sub(scale(Fraction(4),A[i+j]),A[i+j+1]) for j in range(3)] for i in range(3)]
dets=[det3(x) for x in (ordinary,lower,upper)]
assert A[1][0] > 0  # catches omission of the mandatory (2s-1)^(-1) factor
assert all(x[0] > 0 for x in dets)

def strings(x):return [str(x[0]),str(x[1])]
result={'moments_A0_through_A5':[strings(x) for x in A],
        'order_two_determinant_intervals':[strings(x) for x in dets],
        'signs':['positive' if x[0]>0 else 'negative' if x[1]<0 else 'unresolved' for x in dets],
        'squared_coordinate_normalization_regression_passed':True,
        'interval_certified':True,'zero_locations_used':False,'rh_proved':False}
if __name__=='__main__':
    output=Path(__file__).parents[1]/'results'/'quarter-point-order-two-interval.json'
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for key,value in result.items():print(f'{key}={value}')
