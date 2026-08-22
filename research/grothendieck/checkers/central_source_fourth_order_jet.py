"""Analytic fourth-order Decimal jets for H'' and H''' on central cells."""
import json
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path

D=Decimal;ORDER=5;DEPTH=132
PI=D("3.141592653589793238462643383279502884197169399375105820974944592307816406286")
BERNOULLI=[Fraction(1,6),Fraction(-1,30),Fraction(1,42),Fraction(-1,30),
           Fraction(5,66),Fraction(-691,2730),Fraction(7,6),Fraction(-3617,510)]

def const(x):
    if isinstance(x,Fraction):x=D(x.numerator)/D(x.denominator)
    else:x=D(x)
    return [x]+[D(0)]*ORDER
def add(*xs):return [sum((x[n] for x in xs),D(0)) for n in range(ORDER+1)]
def neg(x):return [-a for a in x]
def sub(x,y):return add(x,neg(y))
def scale(x,c):
    if isinstance(c,Fraction):c=D(c.numerator)/D(c.denominator)
    else:c=D(c)
    return [c*a for a in x]
def mul(x,y):return [sum((x[k]*y[n-k] for k in range(n+1)),D(0)) for n in range(ORDER+1)]
def inv(x):
    out=[1/x[0]]+[D(0)]*ORDER
    for n in range(1,ORDER+1):out[n]=-sum((x[k]*out[n-k] for k in range(1,n+1)),D(0))/x[0]
    return out
def div(x,y):return mul(x,inv(y))
def expj(x):
    out=[x[0].exp()]+[D(0)]*ORDER
    for n in range(1,ORDER+1):out[n]=sum((D(k)*x[k]*out[n-k] for k in range(1,n+1)),D(0))/D(n)
    return out
def logj(x):
    quotient=mul([D(n+1)*x[n+1] for n in range(ORDER)]+[D(0)],inv(x))
    return [x[0].ln()]+[quotient[n-1]/D(n) for n in range(1,ORDER+1)]
def powj(x,p):return expj(scale(logj(x),p))
def powi(x,n):
    out=const(1)
    for _ in range(n):out=mul(out,x)
    return out

def eta_pair_jets(s):
    row=[]
    for n in range(1,DEPTH+2):
        logn=D(n).ln();term=expj(scale(s,-logn));row.append([term,scale(term,-logn)])
    total=[const(0),const(0)];two=D(2)
    for _ in range(DEPTH):
        for j in range(2):total[j]=add(total[j],scale(row[0][j],1/two))
        row=[[sub(row[i][j],row[i+1][j]) for j in range(2)] for i in range(len(row)-1)];two*=2
    return total

def digamma_jet(z):
    correction=const(0)
    for _ in range(100):correction=sub(correction,inv(z));z=add(z,const(1))
    value=sub(logj(z),scale(inv(z),Fraction(1,2)))
    for k,b in enumerate(BERNOULLI,1):value=sub(value,scale(inv(powi(z,2*k)),b/Fraction(2*k)))
    return add(value,correction)

def source_F_jet(t0):
    t=[t0,D(1)]+[D(0)]*(ORDER-1);s=add(const(Fraction(1,2)),powj(t,Fraction(1,2)))
    eta,eta1=eta_pair_jets(s);log2=D(2).ln();r=expj(scale(sub(const(1),s),log2))
    zlog=sub(div(eta1,eta),
             div(scale(r,log2),sub(const(1),r)))
    coupled=add(const(-D("0.5")*PI.ln()),scale(digamma_jet(scale(s,Fraction(1,2))),Fraction(1,2)),zlog)
    prefactor=div(scale(mul(s,sub(s,const(1))),4),sub(scale(s,2),const(1)))
    return add(const(4),mul(prefactor,coupled))

def H_derivatives(t):
    f=source_F_jet(t)
    g=[D(n+1)*f[n+1] for n in range(ORDER)] + [D(0)]
    h=powj(g,Fraction(-1,2))
    return D(2)*h[2],D(6)*h[3]

with localcontext() as context:
    context.prec=90
    endpoints=[]
    for power in range(8,2,-1):endpoints.extend((D(f"1e-{power}"),D(f"3e-{power}")))
    endpoints.append(D("1e-2"));rows=[]
    for a,b in zip(endpoints,endpoints[1:]):
        midpoint=(a+b)/2;h2,h3=H_derivatives(midpoint)
        rows.append((a,b,h2,h3,abs(h3)*(b-a)))
    largest=max(rows,key=lambda row:row[4]);least_negative=max(rows,key=lambda row:row[2])

result={"cell_count":len(rows),"shortest_cell":[str(rows[0][0]),str(rows[0][1])],
        "shortest_cell_H_double_prime":str(rows[0][2]),"shortest_cell_H_triple_prime":str(rows[0][3]),
        "shortest_cell_oscillation_budget":str(rows[0][4]),
        "largest_oscillation_budget":str(largest[4]),"largest_oscillation_cell":[str(largest[0]),str(largest[1])],
        "least_negative_H_double_prime":str(least_negative[2]),
        "all_midpoint_H_double_prime_negative":all(row[2]<0 for row in rows),
        "analytic_fourth_order_jet":True,"finite_difference_used":False,
        "interval_certified":False,"rh_proved":False}
if __name__=='__main__':
    output=Path(__file__).parents[1]/'results'/'central-source-fourth-order-jet.json'
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for key,value in result.items():print(f'{key}={value}')
