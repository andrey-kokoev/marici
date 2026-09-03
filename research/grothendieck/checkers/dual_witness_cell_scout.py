"""Freeze dual tail-cone witnesses and test them across neighboring grid cells."""
import json, math
from pathlib import Path
import numpy as np
from scipy.integrate import quad
from scipy.special import digamma, roots_hermite
TS=np.arange(.264,.302,.002); XS=np.arange(4.5,6.201,.005); P=512
hn,hw=roots_hermite(256)
def primes(n):
 s=np.ones(n+1,dtype=bool);s[:2]=False
 for p in range(2,math.isqrt(n)+1):
  if s[p]:s[p*p::p]=False
 return np.flatnonzero(s)
def terms(P):
 a=[]
 for p in primes(P):
  n=int(p);lp=math.log(n)
  while n<=P:a.append((n,lp,math.log(n)));n*=int(p)
 a.sort();return np.array([q[0] for q in a]),np.array([q[1] for q in a]),np.array([q[2] for q in a])
def ub(t,j):
 L=math.log(P);f=L**(j+1)/math.sqrt(P)*math.exp(-L*L/(4*t));return f+quad(lambda y:y**(j+1)*math.exp(y/2-y*y/(4*t)),L,np.inf,epsabs=1e-25)[0]
ns,vm,l=terms(P); RR=[];II=[];U0=[];U2=[]
for t in TS:
 w=vm/np.sqrt(ns)*np.exp(-l*l/(4*t));c=1/(2*math.sqrt(math.pi*t));u=XS[:,None]+hn[None,:]/math.sqrt(t);q=np.real(digamma(.25+.5j*u));g0=-math.log(math.pi)/(4*math.sqrt(math.pi*t))+q@hw/(4*math.pi*math.sqrt(t));g1=(q*hn)@hw/(2*math.pi);ph=t*XS;pf=np.exp(t/4-t*XS*XS);e0=pf*np.cos(ph);e1=pf*(-2*t*XS*np.cos(ph)-t*np.sin(ph));phase=XS[:,None]*l;rp=np.cos(phase)@w;ip=np.sin(phase)@(w*l);RR.append((e0+g0)/c-rp);II.append(-(e1+g1)/c-ip);U0.append(ub(t,0));U2.append(ub(t,2))
RR=np.array(RR);II=np.array(II);U0=np.array(U0);U2=np.array(U2)
cells=[]; worst=1e300
for i in range(len(TS)-1):
 for j in range(len(XS)-1):
  # Witness from the bilinear cell-center approximation.
  rc=float(np.mean(RR[i:i+2,j:j+2]));ic=float(np.mean(II[i:i+2,j:j+2]));u0c=float(np.mean(U0[i:i+2]));u2c=float(np.mean(U2[i:i+2]))
  a=rc/u0c**2;b=ic/(u0c*u2c);h=math.sqrt(a*a*u0c**2+b*b*u0c*u2c);a/=h;b/=h
  vals=[]
  for di,dj in ((0,0),(0,1),(1,0),(1,1)):
   k=i+di;m=j+dj;support=math.sqrt(a*a*U0[k]**2+b*b*U0[k]*U2[k]);vals.append(a*RR[k,m]+b*II[k,m]-support)
  low=min(vals);worst=min(worst,low)
  if low<=0:cells.append({'t':float(TS[i]),'xi':float(XS[j]),'corner_min_dual_margin':low})
out={'schema':'marici.dual-witness-cell-scout.v1','certified':False,'prefix':P,'cell_size':[.002,.005],'cell_count':(len(TS)-1)*(len(XS)-1),'failed_cell_count':len(cells),'minimum_corner_margin':worst,'failed_cells':cells[:100],'limitations':['corner tests are not continuum Taylor bounds','floating source quadrature and majorant integral']};(Path(__file__).parents[1]/'results'/'dual-witness-cell-scout.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ('cell_count','failed_cell_count','minimum_corner_margin')},indent=2))
