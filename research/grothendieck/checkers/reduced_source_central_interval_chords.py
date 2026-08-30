"""Directed-rounding certificate for 21 central reciprocal-slope chords."""
import json
from decimal import Decimal, Context, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction
from functools import lru_cache
from pathlib import Path

PREC, DEPTH = 90, 120
D = Decimal
down = Context(prec=PREC, rounding=ROUND_FLOOR)
up = Context(prec=PREC, rounding=ROUND_CEILING)

def box(x):
    if isinstance(x,Fraction): return qbox(x)
    x = D(x); return x, x
def add(*xs):
    z=(D(0),D(0))
    for x in xs: z=down.add(z[0],x[0]),up.add(z[1],x[1])
    return z
def neg(x): return x[1].copy_negate(),x[0].copy_negate()
def sub(x,y): return add(x,neg(y))
def mul(x,y):
    lows=[down.multiply(a,b) for a in x for b in y]; highs=[up.multiply(a,b) for a in x for b in y]
    return min(lows),max(highs)
def inv(x):
    assert x[0]>0 or x[1]<0
    return down.divide(D(1),x[1]),up.divide(D(1),x[0])
def div(x,y): return mul(x,inv(y))
def scale(x,n): return mul(x,box(n))
def sqrt(x):
    assert x[0]>=0
    return down.sqrt(x[0]),up.sqrt(x[1])
def ln(x):
    assert x[0]>0
    return down.ln(x[0]),up.ln(x[1])
def exp(x): return down.exp(x[0]),up.exp(x[1])
def powi(x,n):
    z=box(1)
    for _ in range(n): z=mul(z,x)
    return z
def qbox(q):
    return down.divide(D(q.numerator),D(q.denominator)),up.divide(D(q.numerator),D(q.denominator))

def atan_fraction(q,n):
    total=Fraction(0)
    for k in range(n): total += (-1)**k*q**(2*k+1)/(2*k+1)
    other=total+(-1)**n*q**(2*n+1)/(2*n+1)
    return min(total,other),max(total,other)
a5=atan_fraction(Fraction(1,5),100);a239=atan_fraction(Fraction(1,239),40)
pi=(down.divide(D((16*a5[0]-4*a239[1]).numerator),D((16*a5[0]-4*a239[1]).denominator)),
    up.divide(D((16*a5[1]-4*a239[0]).numerator),D((16*a5[1]-4*a239[0]).denominator)))
logpi=ln(pi);log2=ln(box(2))
bernoulli=[Fraction(1,6),Fraction(-1,30),Fraction(1,42),Fraction(-1,30),
           Fraction(5,66),Fraction(-691,2730),Fraction(7,6),Fraction(-3617,510)]

def digamma_trigamma(z):
    pc=box(0);tc=box(0)
    for _ in range(100):
        pc=sub(pc,inv(z));tc=add(tc,inv(powi(z,2)));z=add(z,box(1))
    psi=sub(ln(z),scale(inv(z),Fraction(1,2)))
    tri=add(inv(z),scale(inv(powi(z,2)),Fraction(1,2)))
    for k,b in enumerate(bernoulli,1):
        B=qbox(b)
        psi=sub(psi,div(B,scale(powi(z,2*k),2*k)))
        tri=add(tri,div(B,powi(z,2*k+1)))
    b18=qbox(Fraction(43867,798))
    psi_error=div(b18,scale(powi(z,18),18))
    tri_error=div(b18,powi(z,19))
    psi=add(psi,(psi_error[1].copy_negate(),psi_error[1]))
    tri=add(tri,(tri_error[1].copy_negate(),tri_error[1]))
    return add(psi,pc),add(tri,tc)

def eta_triple(s):
    row=[]
    for n in range(1,DEPTH+2):
        lnn=ln(box(n));term=exp(neg(mul(s,lnn)))
        row.append([term,neg(mul(lnn,term)),mul(powi(lnn,2),term)])
    sums=[box(0),box(0),box(0)];two=box(2)
    for _ in range(DEPTH):
        for j in range(3): sums[j]=add(sums[j],div(row[0][j],two))
        row=[[sub(row[i][j],row[i+1][j]) for j in range(3)] for i in range(len(row)-1)]
        two=scale(two,2)
    b0=qbox(Fraction(1,2**DEPTH))
    b1=qbox((Fraction(3,DEPTH)+Fraction(1,DEPTH**2))/2**DEPTH)
    b2=qbox((Fraction(26,DEPTH)+Fraction(4,DEPTH**2)+Fraction(2,DEPTH**3))/2**DEPTH)
    sums[0]=add(sums[0],(D(0),b0[1]))
    sums[1]=add(sums[1],(b1[1].copy_negate(),b1[1]))
    sums[2]=add(sums[2],(b2[1].copy_negate(),b2[1]))
    return sums

@lru_cache(maxsize=None)
def height(text):
    t=box(text);q=sqrt(t);s=add(box(Fraction(1,2)),q)
    eta,eta1,eta2=eta_triple(s);r=exp(mul(sub(box(1),s),log2))
    one_minus_r=sub(box(1),r)
    zlog=sub(div(eta1,eta),div(mul(log2,r),one_minus_r))
    zlog1=add(sub(div(eta2,eta),powi(div(eta1,eta),2)),
              div(mul(powi(log2,2),r),powi(one_minus_r,2)))
    psi,tri=digamma_trigamma(scale(s,Fraction(1,2)))
    coupled=add(neg(scale(logpi,Fraction(1,2))),scale(psi,Fraction(1,2)),zlog)
    coupled1=add(scale(tri,Fraction(1,4)),zlog1)
    prefactor=sub(scale(q,2),scale(inv(q),Fraction(1,2)))
    prefactor1=add(box(2),scale(inv(powi(q,2)),Fraction(1,2)))
    slope=div(add(mul(prefactor1,coupled),mul(prefactor,coupled1)),scale(q,2))
    assert slope[0]>0
    return inv(sqrt(slope))

endpoints=[]
for power in range(8,2,-1):
    endpoints.extend((D(f"1e-{power}"),D(f"3e-{power}")))
endpoints.append(D("1e-2"))
rows=[]
for i,x in enumerate(endpoints):
    for y in endpoints[i+1:]:
        m=(x+y)/2
        gap=sub(height(str(m)),scale(add(height(str(x)),height(str(y))),Fraction(1,2)))
        rows.append((gap,x,m,y))
minimum=min(rows,key=lambda row:row[0][0]);maximum_width=max(row[0][1]-row[0][0] for row in rows)
all_positive=all(row[0][0]>0 for row in rows)
curvature_rows=[]
for gap,a,midpoint,b in rows:
    chord_width=b-a
    average=(down.divide(down.multiply(D(-8),gap[1]),down.multiply(chord_width,chord_width)),
             up.divide(up.multiply(D(-8),gap[0]),up.multiply(chord_width,chord_width)))
    curvature_rows.append((average,a,midpoint,b))
closest_to_zero=max(curvature_rows,key=lambda row:row[0][1])
result={"chord_count":len(rows),"minimum_gap_interval":[str(x) for x in minimum[0]],
        "minimum_chord":[str(x) for x in minimum[1:]],"maximum_gap_interval_width":str(maximum_width),
        "closest_to_zero_average_curvature_interval":[str(x) for x in closest_to_zero[0]],
        "closest_to_zero_average_curvature_chord":[str(x) for x in closest_to_zero[1:]],
        "all_chords_strictly_positive":all_positive,"directed_decimal_rounding":True,
        "analytic_tail_bounds_included":True,"interval_certified":all_positive,
        "zero_locations_used":False,"rh_proved":False}
if __name__=='__main__':
    output=Path(__file__).parents[1]/'results'/'reduced-source-central-interval-chords.json'
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for key,value in result.items():print(f'{key}={value}')
