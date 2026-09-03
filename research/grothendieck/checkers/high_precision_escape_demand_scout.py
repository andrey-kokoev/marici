"""Repair float64 cancellation in escape-demand discovery with 50-digit arithmetic.

Discovery only: fixed Gauss-Hermite quadrature and a finite xi grid are not
interval certificates. The arithmetic itself retains 50 decimal digits.
"""
import json, math
from pathlib import Path
import mpmath as mp
mp.mp.dps = 50
P = 8192
SLICES = [
    (mp.mpf('.3'), mp.mpf('6'), mp.mpf('.1')),
    (mp.mpf('.4'), mp.mpf('8'), mp.mpf('.1')),
    (mp.mpf('.5'), mp.mpf('10'), mp.mpf('.1')),
    (mp.mpf('.7'), mp.mpf('12'), mp.mpf('.1')),
    (mp.mpf('1'), mp.mpf('16'), mp.mpf('.1')),
    (mp.mpf('1.5'), mp.mpf('40'), mp.mpf('.2')),
    (mp.mpf('2'), mp.mpf('140'), mp.mpf('.5')),
    (mp.mpf('3'), mp.mpf('650'), mp.mpf('1')),
]

def prime_powers(limit):
    sieve = bytearray(b'\x01') * (limit + 1); sieve[:2] = b'\x00\x00'
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]: sieve[p*p:limit+1:p] = b'\x00' * (((limit-p*p)//p)+1)
    out=[]
    for p in range(2,limit+1):
        if sieve[p]:
            lp=mp.log(p); n=p
            while n<=limit:
                ln=mp.log(n); out.append((lp/mp.sqrt(n),ln)); n*=p
    return out

def ub(P,t,j):
    L=mp.log(P)
    f=L**(j+1)/mp.sqrt(P)*mp.exp(-L*L/(4*t))
    return f+mp.quad(lambda y:y**(j+1)*mp.exp(y/2-y*y/(4*t)),[L,mp.inf])

terms=prime_powers(P)
nodes,weights=mp.gauss_quadrature(96,'hermite')
rows=[]
for t,xmax,step in SLICES:
    c=1/(2*mp.sqrt(mp.pi*t)); rt=mp.sqrt(t)
    pw=[(a*mp.exp(-ln*ln/(4*t)),ln) for a,ln in terms]
    U0=ub(P,t,0); U2=ub(P,t,2)
    bad=[]; worst=None; x=mp.mpf(0)
    while x<=xmax:
        q0=mp.fsum(weights[k]*mp.re(mp.digamma(mp.mpf('.25')+mp.j*(x+nodes[k]/rt)/2)) for k in range(len(nodes)))
        q1=mp.fsum(weights[k]*nodes[k]*mp.re(mp.digamma(mp.mpf('.25')+mp.j*(x+nodes[k]/rt)/2)) for k in range(len(nodes)))
        g0=-mp.log(mp.pi)/(4*mp.sqrt(mp.pi*t))+q0/(4*mp.pi*rt); g1=q1/(2*mp.pi)
        pref=mp.exp(t/4-t*x*x); e=pref*mp.cos(t*x); e1=pref*(-2*t*x*mp.cos(t*x)-t*mp.sin(t*x))
        rp=mp.fsum(w*mp.cos(x*ln) for w,ln in pw); ip=mp.fsum(w*ln*mp.sin(x*ln) for w,ln in pw)
        rr=(e+g0)/c-rp; ii=-(e1+g1)/c-ip
        margin=rr*rr/(U0*U0)+ii*ii/(U0*U2)-1
        rec=(margin,x,rr,ii)
        if worst is None or margin<worst[0]: worst=rec
        if margin<=0: bad.append(rec)
        x+=step
    rows.append({'t':mp.nstr(t,15),'xi_step':mp.nstr(step,15),'xi_max':mp.nstr(xmax,15),'bad_count':len(bad),'bad_frontier':mp.nstr(max((r[1] for r in bad),default=mp.nan),20),'worst_margin':mp.nstr(worst[0],30),'worst_xi':mp.nstr(worst[1],20),'worst_rr':mp.nstr(worst[2],30),'worst_ii':mp.nstr(worst[3],30),'U0':mp.nstr(U0,30),'U2':mp.nstr(U2,30)})
    print(json.dumps(rows[-1]))
out={'schema':'marici.high-precision-escape-demand-scout.v1','certified':False,'decimal_digits':50,'prefix':P,'gauss_hermite_nodes':96,'rows':rows,'limitations':['finite xi grid','fixed Gauss-Hermite quadrature is not interval enclosed','frontier beyond each xi_max is not tested']}
(Path(__file__).parents[1]/'results'/'high-precision-escape-demand-scout.json').write_text(json.dumps(out,indent=2)+'\n')
