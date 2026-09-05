"""Test only P=1048576 residual samples with P=4194304.

Float64 is adequate for this discovery comparison because the declared
1e-12 arithmetic guard is many orders below the P=4194304 tail moments.
"""
import json, math
from pathlib import Path
import numpy as np
from scipy.integrate import quad
from scipy.special import psi
T=3.0;P=4194304;GUARD=1e-12
XS=np.arange(63.0,801.0,1.0)
def pp(n):
 s=np.ones(n+1,dtype=bool);s[:2]=False
 for p in range(2,math.isqrt(n)+1):
  if s[p]:s[p*p::p]=False
 a=[]
 for p in np.flatnonzero(s):
  q=int(p);lp=math.log(q)
  while q<=n:a.append((q,lp,math.log(q)));q*=int(p)
 a.sort();return np.array([z[0] for z in a]),np.array([z[1] for z in a]),np.array([z[2] for z in a])
def ub(j):
 L=math.log(P);return L**(j+1)/math.sqrt(P)*math.exp(-L*L/(4*T))+quad(lambda y:y**(j+1)*math.exp(y/2-y*y/(4*T)),L,np.inf,epsabs=1e-15)[0]
ns,vm,l=pp(P);w=vm/np.sqrt(ns)*np.exp(-l*l/(4*T));ph=XS[:,None]*l;rp=np.cos(ph)@w;ip=np.sin(ph)@(w*l)
pts=np.linspace(-12,12,961);gw=np.exp(-pts*pts);c=1/(2*math.sqrt(math.pi*T));g0=[];g1=[]
for x in XS:
 vals=np.real(psi(.25+.5j*(x+pts/math.sqrt(T))));q0=np.trapezoid(gw*vals,pts);q1=np.trapezoid(pts*gw*vals,pts);g0.append(-math.log(math.pi)/(4*math.sqrt(math.pi*T))+q0/(4*math.pi*math.sqrt(T)));g1.append(q1/(2*math.pi))
g0=np.array(g0);g1=np.array(g1);pref=np.exp(T/4-T*XS*XS);e=pref*np.cos(T*XS);e1=pref*(-2*T*XS*np.cos(T*XS)-T*np.sin(T*XS));rr=(e+g0)/c-rp;ii=(-e1-g1)/c-ip;U0=ub(0);U2=ub(2)
# Guard both demand coordinates adversely before computing a lower margin.
ar=np.maximum(np.abs(rr)-GUARD,0);ai=np.maximum(np.abs(ii)-GUARD,0);margin=ar*ar/U0**2+ai*ai/(U0*U2)-1;bad=XS[margin<=0]
out={'schema':'marici.p4194304-halfline-grid-scout.v1','certified':False,'t':T,'prefix':P,'input_candidate_count':len(XS),'remaining_count':len(bad),'remaining_xi':bad.tolist(),'last_remaining_xi':float(max(bad)) if len(bad) else None,'minimum_guarded_margin':float(min(margin)),'U0':U0,'U2':U2,'float64_guard':GUARD,'limitations':['tests only prior grid candidates','digamma quadrature not interval enclosed','finite grid']};(Path(__file__).parents[1]/'results'/'p4194304-halfline-grid-scout.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ('input_candidate_count','remaining_count','last_remaining_xi','minimum_guarded_margin','U0','U2')},indent=2))
