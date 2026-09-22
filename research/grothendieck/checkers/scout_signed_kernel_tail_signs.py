"""Interval sign reconnaissance for the fixed-hat post-cutoff kernels; not a tail certificate."""
from pathlib import Path
import json
from flint import arb,ctx
ctx.prec=160
R=Path(__file__).resolve().parents[1]/'results';f=json.loads((R/'time-bin-cubic-observer.json').read_text())['filters']
def rat(x):return arb(x[0])/arb(x[1])
ts=[rat(x) for x in f['nodes']];s=arb(7)/2;beta=arb(3)/2;a=s-1;lam=arb(4);d=s-beta
v=[]
for side in (0,1):
 q=f['bulk'][side];v.append([arb(n)/f['nodal_denominator']/rat(q['normalizer']) for n in q['nodal_numerators']])
T=[arb(0)]*len(ts);J=[arb(0)]*len(ts)
for i in range(len(ts)-2,-1,-1):
 b=(v[0][i+1]-v[0][i])/(ts[i+1]-ts[i]);lo,hi=ts[i:i+2];p,z=v[0][i:i+2]
 T[i]=T[i+1]+(-lam*lo).exp()*(p/lam+b/lam**2)-(-lam*hi).exp()*(z/lam+b/lam**2)
for i in range(len(ts)-1):
 b=(v[1][i+1]-v[1][i])/(ts[i+1]-ts[i]);lo,hi=ts[i:i+2];p,z=v[1][i:i+2]
 J[i+1]=J[i]+(d*hi).exp()*(z/d-b/d**2)-(d*lo).exp()*(p/d-b/d**2)
B=T[0]
def kp(u):
 i=next(j for j in range(len(ts)-1) if ts[j]<=u<=ts[j+1]);b=(v[0][i+1]-v[0][i])/(ts[i+1]-ts[i]);cp=T[i+1]-(-lam*ts[i+1]).exp()*(v[0][i+1]/lam+b/lam**2)
 return B*(-s*u).exp()-(-beta*u).exp()*((v[0][i]+b*(u-ts[i]))/lam+b/lam**2)-cp*(a*u).exp()
rows=[]
for x in (14,16,20,24,32,40,64):
 u=arb(x);rows.append({'u':x,'K_plus':kp(u).str(18),'J_minus':J[next(i for i,z in enumerate(ts) if z==u)].str(18),'K_minus_sign':'positive' if J[next(i for i,z in enumerate(ts) if z==u)]<0 else 'negative'})
assert J[ts.index(arb(16))]<0<J[ts.index(arb(20))] and kp(arb(14))>0>kp(arb(16))
out={'certified':False,'purpose':'Locate sign-change intervals for a future knotwise Stieltjes-tail proof; point/knot signs are not a proof between knots.',
 'post_log_1e6':'13.815510557964274','B0':B.str(18),'rows':rows,
 'candidate_one_sided_lower_strategy':'Discard positive K contributions before their proved sign changes; bound only negative K_plus after 16 and K_minus after the J crossing in (16,20).'}
(R/'signed-kernel-tail-sign-scout.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
