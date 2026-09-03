"""Locate the source-only escape frontier xi*(t) and compare with verification heights."""
import json,math
from pathlib import Path
import numpy as np
from scipy.integrate import quad
from scipy.special import psi as spsi
TS=[.08,.12,.16,.2,.25,.3,.4,.5,.7,1,1.5,2,3]
XI_FINE=np.arange(0,50.01,.05);XI_MID=np.arange(50.5,200,.5);XI_FAR=np.arange(201,601,1)
XS=np.concatenate((XI_FINE,XI_MID,XI_FAR));PS=[512,8192];N=2_000_000
def pp(n):
 s=np.ones(n+1,dtype=bool);s[:2]=False
 for p in range(2,math.isqrt(n)+1):
  if s[p]:s[p*p::p]=False
 a=[]
 for p in np.flatnonzero(s):
  q=int(p);lp=math.log(q)
  while q<=n:a.append((q,lp,math.log(q)));q*=int(p)
 a.sort();return np.array([z[0] for z in a]),np.array([z[1] for z in a]),np.array([z[2] for z in a])
def ub(P,t,j):
 L=math.log(P);return L**(j+1)/math.sqrt(P)*math.exp(-L*L/(4*t))+quad(lambda y:y**(j+1)*math.exp(y/2-y*y/(4*t)),L,np.inf,epsabs=1e-18)[0]
ns,vm,l=pp(N);prime_cache={}
for P in PS:
 ex=ns<=P;prime_cache[P]=(l[ex],vm[ex]/np.sqrt(ns[ex]))
def dig(t,xi):
 # g0 and g1 at (t,xi), digamma Gaussian moments over |y|<=12 with mpmath psi
 pts=np.linspace(-12,12,481)
 u=xi+pts/math.sqrt(t)
 vals=np.real(spsi(.25+.5j*u))
 w=np.exp(-pts*pts)
 q0=np.trapezoid(w*vals,pts);q1=np.trapezoid(pts*w*vals,pts)
 g0=-math.log(math.pi)/(4*math.sqrt(math.pi*t))+q0/(4*math.pi*math.sqrt(t))
 g1=q1/(2*math.pi)
 return g0,g1
rows=[]
for t in TS:
 rt=math.sqrt(t);pi=math.pi;c=1/(2*pi**0.5*rt)
 for P in PS:
  lp,base=prime_cache[P]
  lpld=lp.astype(np.longdouble);baseld=base.astype(np.longdouble)
  w=np.exp(-lpld*lpld/(4*np.longdouble(t)))*baseld
  U0=ub(P,t,0);U2=ub(P,t,2)
  bad=[];minmargin=(1e300,None)
  # vectorized over xi chunks
  for j in range(0,len(XS),100):
   x=XS[j:j+100].astype(np.longdouble)
   pref=np.exp(np.longdouble(t)/4-np.longdouble(t)*x*x);e=pref*np.cos(np.longdouble(t)*x);e1=pref*(-2*np.longdouble(t)*x*np.cos(np.longdouble(t)*x)-np.longdouble(t)*np.sin(np.longdouble(t)*x))
   g0=np.array([dig(t,float(v))[0] for v in x]);g1=np.array([dig(t,float(v))[1] for v in x])
   ph=x[:,None]*lpld
   rp=np.cos(ph)@w;ip=np.sin(ph)@(w*lpld)
   cd=np.longdouble(c);U0ld=np.longdouble(U0);U2ld=np.longdouble(U2)
   rr=(e+g0)/cd-rp;ii=(-e1-g1)/cd-ip
   m=(rr*rr/U0ld**2+ii*ii/(U0ld*U2ld)-1).astype(float)
   for k in range(len(x)):
    if m[k]<minmargin[0]:minmargin=(float(m[k]),float(x[k]))
    if m[k]<=0:bad.append((float(x[k]),float(m[k])))
  frontier=max([b[0] for b in bad],default=None)
  rows.append({'t':t,'P':P,'U0':U0,'U2':U2,'worst_margin':minmargin[0],'worst_xi':minmargin[1],'bad_point_count':len(bad),'escape_frontier_xi_star':frontier,'first_bad':bad[:5],'last_bad':bad[-5:]})
  print(f't={t} P={P} U0={U0:.2e} worst m={minmargin[0]:.3e} at xi={minmargin[1]} bad={len(bad)} frontier={frontier}')
out={'schema':'marici.escape-crossover-scout.v1','certified':False,'xi_grid':[0,600,len(XS)],'prefixes':PS,'prime_cutoff':N,'verification_heights_reference':{'computed_first20_last_ordinate':77.1448400688748,'rigorous_literature':'Platt-Trudgian verify zeta zeros to height 3e9 (order 10^9-10^12 depending on source)'},'rows':rows,'limitations':['grid is not a continuum proof','digamma quadrature is numerical','worst-case cosine alignment over intervals not bounded here','prime tail beyond 2e6 omitted']};(Path(__file__).parents[1]/'results'/'escape-crossover-scout.json').write_text(json.dumps(out,indent=2)+'\n')
