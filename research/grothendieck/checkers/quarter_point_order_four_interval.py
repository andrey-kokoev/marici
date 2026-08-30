"""Certified degree-nine series and order-four Hausdorff determinant attempt."""
import itertools,json,math
from fractions import Fraction
from pathlib import Path
from eta_order_ten_decimal_interval import totals as eta10
from quarter_point_order_two_interval import add,sub,mul,scale,divp,powi,qbox,zeta_integer,logpi

D=9
zetas={p:(zeta_integer(p)[0][0],zeta_integer(p)[1][1]) for p in range(2,D+2)}
L=eta10[0];eta=[scale(Fraction(1,math.factorial(k)),eta10[k]) for k in range(D+2)]
etap=[scale(Fraction(k+1),eta[k+1]) for k in range(D+1)];q=[]
for n in range(D+1):
    numerator=etap[n]
    for k in range(1,n+1):numerator=sub(numerator,mul(eta[k],q[n-k]))
    q.append(divp(numerator,eta[0]))
g0=divp(add(eta[1],scale(Fraction(1,2),powi(L,2))),L)
bern={0:Fraction(1,2),1:Fraction(-1,12),3:Fraction(1,720),5:Fraction(-1,30240),7:Fraction(1,1209600),9:Fraction(-1,47900160)}
ell=[]
for n in range(D+1):
    inv=qbox(Fraction((-1)**n));B=scale(bern[n],powi(L,n+1)) if n in bern else qbox(Fraction(0))
    if n==0:
        gamma=add(scale(Fraction(-1,2),g0),scale(Fraction(-1),L));constant=scale(Fraction(-1,2),logpi)
    else:
        gamma=scale(Fraction((-1)**(n+1)*(2**(n+1)-1),2**(n+1)),zetas[n+1]);constant=qbox(Fraction(0))
    ell.append(add(inv,B,constant,gamma,q[n]))
reduced=[add(*(scale(Fraction((-2)**k),ell[n-k]) for k in range(n+1))) for n in range(D+1)]
def pmul(a,b):
    out=[qbox(Fraction(0)) for _ in range(D+1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j<=D:out[i+j]=add(out[i+j],mul(x,y))
    return out
E=[qbox(Fraction(x)) for x in (0,1,-1,2,-5,14,-42,132,-429,1430)]
powers=[[qbox(Fraction(1))]+[qbox(Fraction(0)) for _ in range(D)]]
for _ in range(D):powers.append(pmul(powers[-1],E))
S=[qbox(Fraction(0)) for _ in range(D+1)]
for n in range(D+1):
    for k in range(D+1):S[k]=add(S[k],mul(reduced[n],powers[n][k]))
A=[scale(Fraction((-1)**k),S[k]) for k in range(D+1)]
def determinant(matrix):
    size=len(matrix);total=qbox(Fraction(0))
    for p in itertools.permutations(range(size)):
        inv=sum(p[i]>p[j] for i in range(size) for j in range(i+1,size));term=qbox(Fraction(1))
        for i in range(size):term=mul(term,matrix[i][p[i]])
        total=add(total,term if inv%2==0 else scale(Fraction(-1),term))
    return total
ordinary=[[A[i+j] for j in range(5)] for i in range(5)]
lower=[[A[i+j+1] for j in range(5)] for i in range(5)]
upper=[[sub(scale(Fraction(4),A[i+j]),A[i+j+1]) for j in range(5)] for i in range(5)]
dets=[determinant(x) for x in (ordinary,lower,upper)]
signs=['positive' if x[0]>0 else 'negative' if x[1]<0 else 'unresolved' for x in dets]
assert A[1][0]>0
assert all(x[0]>0 for x in dets)
def strings(x):return [str(x[0]),str(x[1])]
result={'moments_A0_through_A9':[strings(x) for x in A],'order_four_determinant_intervals':[strings(x) for x in dets],'signs':signs,'interval_arithmetic_completed':True,'zero_locations_used':False,'rh_proved':False}
if __name__=='__main__':
    output=Path(__file__).parents[1]/'results'/'quarter-point-order-four-interval.json';output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for key,value in result.items():print(f'{key}={value}')
