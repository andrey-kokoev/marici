"""Compare actual truncated tail moments with all-integer majorants in the corridor."""
import json,math
from pathlib import Path
import mpmath as mp
import numpy as np
from scipy.integrate import quad
TS=[.4,.6,.8,1,1.5,2,3];XS=np.linspace(0,25,501);PS=[128,256,512,1024,2048,4096,8192,16384,32768,65536];N=2_000_000
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
 L=math.log(P);return L**(j+1)/math.sqrt(P)*math.exp(-L*L/(4*t))+quad(lambda y:y**(j+1)*math.exp(y/2-y*y/(4*t)),L,np.inf)[0]
ns,vm,l=pp(N);base=vm/np.sqrt(ns);rows=[]
for t in TS:
 w=base*np.exp(-l*l/(4*t));R=np.empty_like(XS);I=np.empty_like(XS)
 for j in range(0,len(XS),25):
  z=min(j+25,len(XS));ph=XS[j:z,None]*l;R[j:z]=np.cos(ph)@w;I[j:z]=np.sin(ph)@(w*l)
 gm=zeros[:,None];xx=XS[None,:];em=np.exp(-t*(gm-xx)**2);ep=np.exp(-t*(gm+xx)**2);theta=np.sum((em+ep)/2,axis=0);dtheta=np.sum(t*((gm-xx)*em-(gm+xx)*ep),axis=0);c=1/(2*math.sqrt(math.pi*t));pa=np.zeros(len(XS),int);pi=np.zeros(len(XS),int)
 ratios={}
 for P in PS:
  ex=ns<=P;tail=~ex;ph=XS[:,None]*l[ex];rp=np.cos(ph)@w[ex];ip=np.sin(ph)@(w[ex]*l[ex]);rr=R-rp+theta/c;ii=I-ip-dtheta/c;ma0=float(sum(w[tail]));ma2=float(sum(w[tail]*l[tail]**2));ui0=ub(P,t,0);ui2=ub(P,t,2);ea=rr*rr/ma0**2+ii*ii/(ma0*ma2)-1;ei=rr*rr/ui0**2+ii*ii/(ui0*ui2)-1;pa[(pa==0)&(ea>0)]=P;pi[(pi==0)&(ei>0)]=P;ratios[str(P)]=[ui0/ma0,ui2/ma2]
 rows.append({'t':t,'actual_tail_unresolved':int(sum(pa==0)),'integer_tail_unresolved':int(sum(pi==0)),'actual_tail_max_prefix':int(max(pa)) if all(pa) else None,'integer_tail_max_prefix':int(max(pi)) if all(pi) else None,'actual_unresolved_span':[float(XS[pa==0][0]),float(XS[pa==0][-1])] if any(pa==0) else None,'integer_unresolved_span':[float(XS[pi==0][0]),float(XS[pi==0][-1])] if any(pi==0) else None,'majorant_to_actual_ratios':ratios})
out={'schema':'marici.actual-vs-integer-tail-corridor.v1','certified':False,'prime_cutoff':N,'rows':rows,'limitations':['actual tail moments omit n>2e6','zero-side discovery only','grid scout']};(Path(__file__).parents[1]/'results'/'actual-vs-integer-tail-corridor.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps([{k:r[k] for k in ('t','actual_tail_unresolved','integer_tail_unresolved','actual_tail_max_prefix','actual_unresolved_span')} for r in rows],indent=2))
