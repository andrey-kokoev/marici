"""Test larger exact prefixes only on the P=128 residual island."""
import json, math
from pathlib import Path
import numpy as np
from scipy.special import digamma, roots_hermite

TS=np.arange(.264,.302,.002); XS=np.arange(4.5,6.201,.005)
PREFIXES=(128,256,512,1024); NMAX=2_000_000
hn,hw=roots_hermite(256)

def pp(limit):
 s=np.ones(limit+1,dtype=bool); s[:2]=False
 for p in range(2,math.isqrt(limit)+1):
  if s[p]: s[p*p::p]=False
 a=[]
 for p in np.flatnonzero(s):
  n=int(p); lp=math.log(n)
  while n<=limit:
   a.append((n,lp,math.log(n)))
   if n>limit//int(p): break
   n*=int(p)
 a.sort(); return np.array([z[0] for z in a]),np.array([z[1] for z in a]),np.array([z[2] for z in a])

def endpoint(t,x):
 ph=t*x; p=np.exp(t/4-t*x*x); co=np.cos(ph); si=np.sin(ph)
 return p*co,p*(-2*t*x*co-t*si)
ns,vm,logs=pp(NMAX); rows=[]
for t in TS:
 w=vm/np.sqrt(ns)*np.exp(-logs*logs/(4*t)); c=1/(2*math.sqrt(math.pi*t))
 u=XS[:,None]+hn[None,:]/math.sqrt(t); q=np.real(digamma(.25+.5j*u))
 g0=-math.log(math.pi)/(4*math.sqrt(math.pi*t))+q@hw/(4*math.pi*math.sqrt(t)); g1=(q*hn)@hw/(2*math.pi)
 e0,e1=endpoint(t,XS); a0=e0+g0; a1=e1+g1
 for P in PREFIXES:
  ex=ns<=P; le=logs[ex]; we=w[ex]; lt=logs[~ex]; wt=w[~ex]
  ph=XS[:,None]*le; rp=np.cos(ph)@we; ip=np.sin(ph)@(we*le)
  m0=float(sum(wt)); m2=float(sum(wt*lt*lt)); rr=a0/c-rp; ii=-a1/c-ip
  margin=rr*rr/(m0*m0)+ii*ii/(m0*m2)-1
  mask=margin<=0; idx=int(np.argmin(margin)); sx=XS[mask]
  rows.append({"t":float(t),"prefix":P,"minimum_margin":float(margin[idx]),"minimizer_xi":float(XS[idx]),"survivor_count":int(sum(mask)),"survivor_span":[float(sx[0]),float(sx[-1])] if len(sx) else None})
out={"schema":"marici.adaptive-prefix-residual-island-scout.v1","certified":False,"t_range":[float(TS[0]),float(TS[-1])],"xi_range":[float(XS[0]),float(XS[-1])],"rows":rows,"limitations":["floating grid","unenclosed quadrature and prime tail"]}
path=Path(__file__).parents[1]/'results'/'adaptive-prefix-residual-island-scout.json'; path.write_text(json.dumps(out,indent=2)+'\n')
for P in PREFIXES:
 z=[r for r in rows if r['prefix']==P]; print(P, min(r['minimum_margin'] for r in z), sum(r['survivor_count'] for r in z), [(r['t'],r['survivor_span']) for r in z if r['survivor_count']][:8])
