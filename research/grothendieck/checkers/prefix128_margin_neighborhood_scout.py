"""Map the P=128 positive-tail ellipse margin near the validated t slice."""
import json, math
from pathlib import Path
import numpy as np
from scipy.special import digamma, roots_hermite

TS=np.linspace(.26,.29,16); XS=np.linspace(0,25,2501); NMAX=2_000_000; PREFIX=128
hn,hw=roots_hermite(256)

def terms(limit):
 s=np.ones(limit+1,dtype=bool); s[:2]=False
 for p in range(2,math.isqrt(limit)+1):
  if s[p]: s[p*p::p]=False
 ns=[]; vm=[]
 for p in np.flatnonzero(s):
  n=int(p); lp=math.log(n)
  while n<=limit:
   ns.append(n); vm.append(lp)
   if n>limit//int(p): break
   n*=int(p)
 o=np.argsort(ns); return np.asarray(ns,float)[o],np.asarray(vm)[o]

def end(t,x):
 ph=t*x; p=np.exp(t/4-t*x*x); co=np.cos(ph); si=np.sin(ph)
 return p*co,p*(-2*t*x*co-t*si)
ns,vm=terms(NMAX); logs=np.log(ns); exact=ns<=PREFIX
rows=[]; global_min=None
for t in TS:
 w=vm/np.sqrt(ns)*np.exp(-logs*logs/(4*t)); we=w[exact]; le=logs[exact]; wt=w[~exact]; lt=logs[~exact]
 m0=float(sum(wt)); m2=float(sum(wt*lt*lt)); c=1/(2*math.sqrt(math.pi*t))
 u=XS[:,None]+hn[None,:]/math.sqrt(t); q=np.real(digamma(.25+.5j*u))
 g0=-math.log(math.pi)/(4*math.sqrt(math.pi*t))+q@hw/(4*math.pi*math.sqrt(t)); g1=(q*hn)@hw/(2*math.pi)
 e0,e1=end(t,XS); a0=e0+g0; a1=e1+g1
 rp=np.empty_like(XS); ip=np.empty_like(XS)
 for j in range(0,len(XS),200):
  z=min(j+200,len(XS)); ph=XS[j:z,None]*le
  rp[j:z]=np.cos(ph)@we; ip[j:z]=np.sin(ph)@(we*le)
 rr=a0/c-rp; ii=-a1/c-ip
 margin=rr*rr/(m0*m0)+ii*ii/(m0*m2)-1
 i=int(np.argmin(margin)); row={"t":float(t),"minimum_margin":float(margin[i]),"minimizer_xi":float(XS[i]),"minimum_margin_xi_ge_0_1":float(np.min(margin[XS>=.1])),"minimum_margin_xi_ge_1":float(np.min(margin[XS>=1])),"excluded_fraction":float(np.mean(margin>0))}
 rows.append(row)
 if global_min is None or row['minimum_margin']<global_min['minimum_margin']: global_min=row
out={"schema":"marici.prefix128-margin-neighborhood-scout.v1","certified":False,"prefix":PREFIX,"t_range":[.26,.29],"xi_range":[0,25],"rows":rows,"global_minimum":global_min,"limitations":["floating-point grid","quadrature and tail not interval enclosed"]}
p=Path(__file__).parents[1]/'results'/'prefix128-margin-neighborhood-scout.json'; p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
