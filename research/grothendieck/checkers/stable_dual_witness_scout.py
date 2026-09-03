"""Generate dual witnesses stably from zero-side values, for discovery only."""
import json,math
from pathlib import Path
import mpmath as mp
import numpy as np
from scipy.integrate import quad
TS=np.arange(.264,.302,.002);XS=np.arange(4.5,6.201,.005);P=512;N=2_000_000
mp.mp.dps=30; zeros=np.array([float(mp.im(mp.zetazero(k))) for k in range(1,61)])
def pp(n):
 s=np.ones(n+1,dtype=bool);s[:2]=False
 for p in range(2,math.isqrt(n)+1):
  if s[p]:s[p*p::p]=False
 a=[]
 for p in np.flatnonzero(s):
  q=int(p);lp=math.log(q)
  while q<=n:a.append((q,lp,math.log(q)));q*=int(p)
 a.sort();return np.array([z[0] for z in a]),np.array([z[1] for z in a]),np.array([z[2] for z in a])
def ub(t,j):
 L=math.log(P);return L**(j+1)/math.sqrt(P)*math.exp(-L*L/(4*t))+quad(lambda y:y**(j+1)*math.exp(y/2-y*y/(4*t)),L,np.inf)[0]
ns,vm,l=pp(N);tail=ns>P; l=l[tail];base=vm[tail]/np.sqrt(ns[tail]);RR=[];II=[];U0=[];U2=[]
for t in TS:
 w=base*np.exp(-l*l/(4*t)); ph=XS[:,None]*l;rt=np.cos(ph)@w;it=np.sin(ph)@(w*l);gm=zeros[:,None];xx=XS[None,:];em=np.exp(-t*(gm-xx)**2);ep=np.exp(-t*(gm+xx)**2);theta=np.sum((em+ep)/2,axis=0);dtheta=np.sum(t*((gm-xx)*em-(gm+xx)*ep),axis=0);c=1/(2*math.sqrt(math.pi*t));RR.append(rt+theta/c);II.append(it-dtheta/c);U0.append(ub(t,0));U2.append(ub(t,2))
RR=np.array(RR);II=np.array(II);U0=np.array(U0);U2=np.array(U2);failed=[];worst=1e300;worst_record=None
for i in range(len(TS)-1):
 for j in range(len(XS)-1):
  rc=np.mean(RR[i:i+2,j:j+2]);ic=np.mean(II[i:i+2,j:j+2]);u0=np.mean(U0[i:i+2]);u2=np.mean(U2[i:i+2]);a=rc/u0**2;b=ic/(u0*u2);h=math.sqrt(a*a*u0*u0+b*b*u0*u2);a/=h;b/=h;vals=[]
  for di,dj in ((0,0),(0,1),(1,0),(1,1)):
   k=i+di;m=j+dj;vals.append(a*RR[k,m]+b*II[k,m]-math.sqrt(a*a*U0[k]**2+b*b*U0[k]*U2[k]))
  low=min(vals)
  if low<worst:
   worst=low;worst_record={'t_lower':float(TS[i]),'xi_lower':float(XS[j]),'alpha':a,'beta':b,'corner_margins':vals}
  if low<=0:failed.append([float(TS[i]),float(XS[j]),low])
out={'schema':'marici.stable-dual-witness-scout.v1','certified':False,'uses_zero_side_for_witness_discovery':True,'cell_count':(len(TS)-1)*(len(XS)-1),'failed_cell_count':len(failed),'minimum_corner_margin':worst,'worst_cell':worst_record,'failed_cells':failed[:100],'limitations':['zeros are discovery data, not certificate evidence','corner tests are not continuum bounds','prime tail cutoff unenclosed']};(Path(__file__).parents[1]/'results'/'stable-dual-witness-scout.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ('cell_count','failed_cell_count','minimum_corner_margin','worst_cell')},indent=2))
