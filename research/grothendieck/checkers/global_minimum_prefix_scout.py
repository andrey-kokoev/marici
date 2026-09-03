"""Global scout for the minimum exact prefix separating each grid point.

Uses computed critical-line zeros only to stabilize discovery. No zero-side
quantity is admissible certificate evidence.
"""
import json,math
from pathlib import Path
import mpmath as mp
import numpy as np
from scipy.integrate import quad
TS=np.geomspace(.08,3,48);XS=np.linspace(0,25,501);PREFIXES=[128,256,512,1024,2048,4096,8192,16384,32768,65536];N=2_000_000
mp.mp.dps=30;zeros=np.array([float(mp.im(mp.zetazero(k))) for k in range(1,81)])
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
 L=math.log(P);f=L**(j+1)/math.sqrt(P)*math.exp(-L*L/(4*t));return f+quad(lambda y:y**(j+1)*math.exp(y/2-y*y/(4*t)),L,np.inf,epsabs=1e-20)[0]
ns,vm,l=pp(N);base=vm/np.sqrt(ns);rows=[];global_unresolved=[]
for t in TS:
 w=base*np.exp(-l*l/(4*t));R=np.empty_like(XS);I=np.empty_like(XS)
 for j in range(0,len(XS),25):
  z=min(j+25,len(XS));ph=XS[j:z,None]*l;R[j:z]=np.cos(ph)@w;I[j:z]=np.sin(ph)@(w*l)
 gm=zeros[:,None];xx=XS[None,:];em=np.exp(-t*(gm-xx)**2);ep=np.exp(-t*(gm+xx)**2);theta=np.sum((em+ep)/2,axis=0);dtheta=np.sum(t*((gm-xx)*em-(gm+xx)*ep),axis=0);c=1/(2*math.sqrt(math.pi*t));pmin=np.zeros(len(XS),int);margin_at=np.full(len(XS),np.nan)
 for P in PREFIXES:
  target=(pmin==0);tail=ns>P;rt=R.copy();it=I.copy(); # subtract omitted n>N only through discovery cutoff
  ex=~tail;ph=XS[:,None]*l[ex];rp=np.cos(ph)@w[ex];ip=np.sin(ph)@(w[ex]*l[ex]);rr=R-rp+theta/c;ii=I-ip-dtheta/c;u0=ub(P,t,0);u2=ub(P,t,2);margin=rr*rr/u0**2+ii*ii/(u0*u2)-1;hit=target&(margin>0);pmin[hit]=P;margin_at[hit]=margin[hit]
 unresolved=np.flatnonzero(pmin==0);global_unresolved.extend((float(t),float(XS[k])) for k in unresolved)
 counts={str(P):int(np.sum(pmin==P)) for P in PREFIXES};rows.append({'t':float(t),'counts_by_minimum_prefix':counts,'unresolved_count':len(unresolved),'unresolved_span':[float(XS[unresolved[0]]),float(XS[unresolved[-1]])] if len(unresolved) else None,'maximum_required_prefix':int(max(pmin)) if not len(unresolved) else None,'minimum_margin_at_selected_prefix':float(np.nanmin(margin_at))})
out={'schema':'marici.global-minimum-prefix-scout.v1','certified':False,'grid':{'t':[float(TS[0]),float(TS[-1]),len(TS)],'xi':[0,25,len(XS)]},'prefixes':PREFIXES,'prime_discovery_cutoff':N,'zero_count_for_stable_discovery':len(zeros),'rows':rows,'global_unresolved_count':len(global_unresolved),'first_unresolved':global_unresolved[:100],'limitations':['zero side used only for discovery','prime tail beyond two million omitted from contact-demand discovery','grid does not prove uniform boundedness','all-integer tail integral numerical']};(Path(__file__).parents[1]/'results'/'global-minimum-prefix-scout.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'global_unresolved_count':len(global_unresolved),'max_prefix_over_resolved':max(r['maximum_required_prefix'] or 0 for r in rows),'rows_with_unresolved':[(r['t'],r['unresolved_count'],r['unresolved_span']) for r in rows if r['unresolved_count']]},indent=2))
