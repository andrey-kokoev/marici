"""Probe natural interval-jet conditioning on the hardest central cell."""
import json
from fractions import Fraction
from pathlib import Path

import reduced_source_central_interval_chords as I

O=5;DEPTH=300
def c(x):return [I.box(x)]+[I.box(0)]*O
def cb(x):return [x]+[I.box(0)]*O
def add(*xs):return [I.add(*(x[n] for x in xs)) for n in range(O+1)]
def neg(x):return [I.neg(a) for a in x]
def sub(x,y):return add(x,neg(y))
def scale(x,q):return [I.scale(a,q) for a in x]
def mul(x,y):return [I.add(*(I.mul(x[k],y[n-k]) for k in range(n+1))) for n in range(O+1)]
def inv(x):
    out=[I.inv(x[0])]+[I.box(0)]*O
    for n in range(1,O+1):out[n]=I.neg(I.div(I.add(*(I.mul(x[k],out[n-k]) for k in range(1,n+1))),x[0]))
    return out
def div(x,y):return mul(x,inv(y))
def expj(x):
    out=[I.exp(x[0])]+[I.box(0)]*O
    for n in range(1,O+1):out[n]=I.scale(I.add(*(I.scale(I.mul(x[k],out[n-k]),k) for k in range(1,n+1))),Fraction(1,n))
    return out
def logj(x):
    derivative=[I.scale(x[n+1],n+1) for n in range(O)]+[I.box(0)];q=mul(derivative,inv(x))
    return [I.ln(x[0])]+[I.scale(q[n-1],Fraction(1,n)) for n in range(1,O+1)]
def powj(x,q):return expj(scale(logj(x),q))
def powi(x,n):
    out=c(1)
    for _ in range(n):out=mul(out,x)
    return out
def eta_pair(s):
    row=[]
    for n in range(1,DEPTH+2):
        l=I.ln(I.box(n));term=expj(neg(mul(s,cb(l))))
        row.append([term,mul(neg(cb(l)),term)])
    total=[c(0),c(0)];two=2
    for _ in range(DEPTH):
        for j in range(2):total[j]=add(total[j],mul(row[0][j],cb(I.inv(I.box(two)))))
        row=[[sub(row[i][j],row[i+1][j]) for j in range(2)] for i in range(len(row)-1)];two*=2
    return total
def digamma(z):
    correction=c(0)
    for _ in range(1000):correction=sub(correction,inv(z));z=add(z,c(1))
    value=sub(logj(z),scale(inv(z),Fraction(1,2)))
    for k,b in enumerate(I.bernoulli,1):value=sub(value,scale(inv(powi(z,2*k)),b/Fraction(2*k)))
    return add(value,correction)

t=[(I.D('1e-8'),I.D('3e-8')),I.box(1)]+[I.box(0)]*(O-1)
s=add(c(Fraction(1,2)),powj(t,Fraction(1,2)));eta,eta_s=eta_pair(s);r=expj(mul(sub(c(1),s),cb(I.log2)))
zlog=sub(div(eta_s,eta),div(mul(r,cb(I.log2)),sub(c(1),r)))
coupled=add(cb(I.neg(I.scale(I.logpi,Fraction(1,2)))),scale(digamma(scale(s,Fraction(1,2))),Fraction(1,2)),zlog)
prefactor=div(scale(mul(s,sub(s,c(1))),4),sub(scale(s,2),c(1)));f=add(c(4),mul(prefactor,coupled))
g=[I.scale(f[n+1],n+1) for n in range(O)]+[I.box(0)];g0=g[0]
result={"cell":["1e-8","3e-8"],"F_prime_natural_interval":[str(x) for x in g0],
        "F_prime_interval_crosses_zero":g0[0]<=0<=g0[1],
        "natural_interval_closes_concavity":False,
        "analytic_tails_injected":False,"conditioning_probe_only":True,"interval_certified":False,"rh_proved":False}
if __name__=='__main__':
    output=Path(__file__).parents[1]/'results'/'central-interval-jet-first-cell-probe.json'
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for key,value in result.items():print(f'{key}={value}')
