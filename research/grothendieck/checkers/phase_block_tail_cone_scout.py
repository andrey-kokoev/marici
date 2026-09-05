"""Test whether phase-local tail blocks tighten the global moment ellipse."""
import json,math
from pathlib import Path
import numpy as np
from scipy.integrate import quad
from scipy.special import psi
T=3.;P=8192;N=2_000_000;XS=np.arange(0,151,1.);PHIS=np.linspace(0,2*math.pi,181)[:-1]
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
 L=math.log(P);return L**(j+1)/math.sqrt(P)*math.exp(-L*L/(4*T))+quad(lambda y:y**(j+1)*math.exp(y/2-y*y/(4*T)),L,np.inf)[0]
ns,vm,l=pp(N);w=vm/np.sqrt(ns)*np.exp(-l*l/(4*T));pre=ns<=P;tail=~pre;U0=ub(0);U2=ub(2);scale=math.sqrt(U0*U2)
pts=np.linspace(-12,12,961);gw=np.exp(-pts*pts);c=1/(2*math.sqrt(math.pi*T));excluded=0;feasible=0;records=[]
for x in XS:
 vals=np.real(psi(.25+.5j*(x+pts/math.sqrt(T))));q0=np.trapezoid(gw*vals,pts);q1=np.trapezoid(pts*gw*vals,pts);g0=-math.log(math.pi)/(4*math.sqrt(math.pi*T))+q0/(4*math.pi*math.sqrt(T));g1=q1/(2*math.pi);p=math.exp(T/4-T*x*x);e=p*math.cos(T*x);e1=p*(-2*T*x*math.cos(T*x)-T*math.sin(T*x));rp=np.cos(x*l[pre])@w[pre];ip=np.sin(x*l[pre])@(w[pre]*l[pre]);r=(e+g0)/c-rp;i=-(e1+g1)/c-ip
 ell=r*r/U0**2+i*i/(U0*U2)-1
 if ell>0:continue
 feasible+=1;lt=l[tail];wt=w[tail]
 # Phase width pi/8; each block keeps exact actual mass but relaxes positions inside its cell.
 keys=np.floor(x*lt/(math.pi/8)).astype(np.int64) if x else np.arange(len(lt),dtype=np.int64)//256
 starts=np.r_[0,np.flatnonzero(np.diff(keys))+1];mass=np.add.reduceat(wt,starts);best=-1e300
 for ph in PHIS:
  a=math.cos(ph)/U0;b=math.sin(ph)/scale;atom=a*np.cos(x*lt)+b*lt*np.sin(x*lt);sup=np.sum(mass*np.maximum.reduceat(atom,starts));best=max(best,a*r+b*i-sup)
 if best>0:excluded+=1
 else:records.append({'xi':float(x),'ellipse_margin':float(ell),'best_block_margin':float(best),'blocks':len(starts)})
out={'schema':'marici.phase-block-tail-cone-scout.v1','certified':False,'t':T,'prefix':P,'tail_cutoff':N,'ellipse_feasible':feasible,'block_cone_excluded':excluded,'block_cone_remaining':len(records),'remaining':records,'limitations':['uses actual block masses through finite cutoff','omits tail beyond cutoff','integer xi grid','direction grid']};(Path(__file__).parents[1]/'results'/'phase-block-tail-cone-scout.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ('ellipse_feasible','block_cone_excluded','block_cone_remaining')},indent=2))
