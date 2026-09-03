"""Numerical preflight for the normalized theta-Schwartz Weil Gram pair.

This is not interval certification.  It records cutoff drift and deliberate
convention residuals so a later interval implementation has frozen targets.
"""
from __future__ import annotations
import json
from pathlib import Path
import mpmath as mp

mp.mp.dps = 35
PI = mp.pi
A = mp.log(2)
OUT = Path(__file__).parents[1] / "results" / "theta_schwartz_weil_gram.json"

def f(u):
    return mp.exp(-PI * (mp.exp(2*u) + mp.exp(-2*u)))

def corr(x):
    return mp.quad(lambda u: f(u) * f(u-x), [-mp.inf, mp.inf])

def F(t):
    return mp.besselk(0.5j*t, 2*PI)

def arch(shift):
    integrand = lambda t: F(t)**2 * mp.cos(shift*t) * (mp.re(mp.digamma(mp.mpf('0.25') + 0.5j*t)) - mp.log(PI))
    return mp.re(mp.quad(integrand, [0, 2, 5, 10, 20]) / PI)

def primes_upto(n):
    ans=[]
    for p in range(2,n+1):
        if all(p%d for d in range(2,int(p**0.5)+1)):
            ans.append(p)
    return ans

def prime_term(shift, cutoff, sign=-1, omit_two=False, rival_2pi=False):
    total=mp.mpf('0')
    for p in primes_upto(cutoff):
        power=p
        while power<=cutoff:
            if not (omit_two and power==2):
                x=mp.log(power)/(2*PI) if rival_2pi else mp.log(power)
                total += mp.log(p)/mp.sqrt(power) * (corr(x+shift)+corr(shift-x))
            power*=p
    return sign*total

def values(cutoff, sign=-1, omit_two=False, rival_2pi=False):
    b=mp.besselk(mp.mpf('0.25'),2*PI)**2
    q=2*b+arch(0)+prime_term(0,cutoff,sign,omit_two,rival_2pi)
    c=(mp.exp(A/2)+mp.exp(-A/2))*b+arch(A)+prime_term(A,cutoff,sign,omit_two,rival_2pi)
    return q,c,q-abs(c)

def enc(x): return mp.nstr(x,25)
base40=values(40); base80=values(80)
flip=values(80,sign=1); omit=values(80,omit_two=True); rival=values(80,rival_2pi=True)
result={
 "schema":"marici.nima.theta-schwartz-weil-gram-preflight.v1",
 "certified":False,
 "normalization":"K(t)=H(1/2+it), k(u)=(2pi)^-1 integral K(t)e^-itu dt",
 "cutoff_40":{"q":enc(base40[0]),"c":enc(base40[1]),"margin":enc(base40[2])},
 "cutoff_80":{"q":enc(base80[0]),"c":enc(base80[1]),"margin":enc(base80[2])},
 "cutoff_drift":{"q":enc(base80[0]-base40[0]),"c":enc(base80[1]-base40[1]),"margin":enc(base80[2]-base40[2])},
 "deliberate_failures":{
   "prime_sign_margin":enc(flip[2]),
   "omit_p2_margin":enc(omit[2]),
   "rival_2pi_margin":enc(rival[2]),
   "prime_sign_residual":enc(flip[2]-base80[2]),
   "omit_p2_residual":enc(omit[2]-base80[2]),
   "rival_2pi_residual":enc(rival[2]-base80[2])},
 "limitation":"mpmath quadrature and cutoff drift are numerical preflight, not rigorous enclosures"
}
OUT.parent.mkdir(parents=True,exist_ok=True)
OUT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
