"""Test an elementary all-integer majorant for the prime-power tail."""
import json, math
from pathlib import Path
import numpy as np
from scipy.integrate import quad
from scipy.special import digamma, roots_hermite
TS=np.arange(.264,.302,.002); XS=np.arange(4.5,6.201,.005); PS=(256,512,1024); N=2000000
hn,hw=roots_hermite(256)
def pp(limit):
 s=np.ones(limit+1,dtype=bool);s[:2]=False
 for p in range(2,math.isqrt(limit)+1):
  if s[p]:s[p*p::p]=False
 a=[]
 for p in np.flatnonzero(s):
  n=int(p);lp=math.log(n)
  while n<=limit:
   a.append((n,lp,math.log(n)))
   if n>limit//int(p):break
   n*=int(p)
 a.sort();return np.array([z[0] for z in a]),np.array([z[1] for z in a]),np.array([z[2] for z in a])
def ub(P,t,j):
 L=math.log(P); f=L**(j+1)/math.sqrt(P)*math.exp(-L*L/(4*t))
 return f+quad(lambda y:y**(j+1)*math.exp(y/2-y*y/(4*t)),L,np.inf,epsabs=1e-25)[0]
def ep(t,x):
 q=t*x;p=np.exp(t/4-t*x*x);return p*np.cos(q),p*(-2*t*x*np.cos(q)-t*np.sin(q))
ns,vm,l=pp(N);rows=[]
for t in TS:
 w=vm/np.sqrt(ns)*np.exp(-l*l/(4*t));c=1/(2*math.sqrt(math.pi*t));u=XS[:,None]+hn[None,:]/math.sqrt(t);q=np.real(digamma(.25+.5j*u));g0=-math.log(math.pi)/(4*math.sqrt(math.pi*t))+q@hw/(4*math.pi*math.sqrt(t));g1=(q*hn)@hw/(2*math.pi);e0,e1=ep(t,XS);a0=e0+g0;a1=e1+g1
 for P in PS:
  ex=ns<=P;le=l[ex];we=w[ex];ph=XS[:,None]*le;rp=np.cos(ph)@we;ip=np.sin(ph)@(we*le);m0=ub(P,t,0);m2=ub(P,t,2);rr=a0/c-rp;ii=-a1/c-ip;margin=rr*rr/m0**2+ii*ii/(m0*m2)-1;i=int(np.argmin(margin));rows.append({'t':float(t),'prefix':P,'tail_M0_upper':m0,'tail_M2_upper':m2,'minimum_margin':float(margin[i]),'minimizer_xi':float(XS[i]),'excluded_fraction':float(np.mean(margin>0))})
out={'schema':'marici.integer-majorant-tail-scout.v1','certified':False,'rows':rows,'majorant':'Lambda(n)<=log(n), sum<=first term+integral after monotonicity threshold','limitations':['quadrature and margin floating, not interval enclosed']};(Path(__file__).parents[1]/'results'/'integer-majorant-tail-scout.json').write_text(json.dumps(out,indent=2)+'\n')
for P in PS:
 z=[r for r in rows if r['prefix']==P];print(P,min(r['minimum_margin'] for r in z),min(r['excluded_fraction'] for r in z))
