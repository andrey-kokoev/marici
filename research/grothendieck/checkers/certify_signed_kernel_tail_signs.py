"""Whole-cell sign certificate for the adverse fixed-hat kernel tails."""
from pathlib import Path
import json
from flint import arb,ctx
ctx.prec=512
R=Path(__file__).resolve().parents[1]/'results';f=json.loads((R/'time-bin-cubic-observer.json').read_text())['filters']
def rat(x):return arb(x[0])/arb(x[1])
ts=[rat(x) for x in f['nodes']];s=arb(7)/2;beta=arb(3)/2;a=s-1;lam=arb(4);d=s-beta
def vals(side):
 q=f['bulk'][side];return [arb(n)/f['nodal_denominator']/rat(q['normalizer']) for n in q['nodal_numerators']]
pv,mv=vals(0),vals(1);T=[arb(0)]*len(ts);J=[arb(0)]*len(ts)
for i in range(len(ts)-2,-1,-1):
 b=(pv[i+1]-pv[i])/(ts[i+1]-ts[i]);lo,hi=ts[i:i+2];p,z=pv[i:i+2];T[i]=T[i+1]+(-lam*lo).exp()*(p/lam+b/lam**2)-(-lam*hi).exp()*(z/lam+b/lam**2)
for i in range(len(ts)-1):
 b=(mv[i+1]-mv[i])/(ts[i+1]-ts[i]);lo,hi=ts[i:i+2];p,z=mv[i:i+2];J[i+1]=J[i]+(d*hi).exp()*(z/d-b/d**2)-(d*lo).exp()*(p/d-b/d**2)
B=T[0];cells=0
def Kplus(u,i):
 b=(pv[i+1]-pv[i])/(ts[i+1]-ts[i]);cp=T[i+1]-(-lam*ts[i+1]).exp()*(pv[i+1]/lam+b/lam**2)
 return B*(-s*u).exp()-(-beta*u).exp()*((pv[i]+b*(u-ts[i]))/lam+b/lam**2)-cp*(a*u).exp()
# Interval-evaluate every whole subcell; no point samples establish the sign.
for i in range(len(ts)-1):
 if ts[i+1]<=16 or ts[i]>=56:continue
 lo=max(ts[i],arb(16));hi=min(ts[i+1],arb(56))
 for j in range(128):
  u=(lo+(hi-lo)*j/128).union(lo+(hi-lo)*(j+1)/128)
  if not Kplus(u,i)<0:raise AssertionError(f'K_plus sign not negative on segment {i}, subcell {j}: {Kplus(u,i)}')
  cells+=1
# J(20)>0 and b_minus is positive from 20 through the terminal knot, so
# J remains positive and Kminus=-exp(-s*u)J(u) remains negative.
i20=ts.index(arb(20));assert J[i20]>0
for i in range(i20,len(ts)-1):assert mv[i]>0 and mv[i+1]>=0
# The expanded formula loses digits near 64. Use the defining stable identity
# K_plus=B0*exp(-s*u)-exp((s-1)*u)*T(u).  The last linear plus-hat segment
# is nonnegative, hence its positive weighted tail T is nonnegative.
i56=ts.index(arb(56));assert pv[i56]>=0 and pv[i56+1]>=0 and T[i56]>=0
assert B<0 and J[-1]>0
out={'passed':True,'K_plus_negative_on':[16,64],'K_minus_negative_on':[20,64],
 'post_64_signs':{'K_plus':'negative','K_minus':'negative'},
 'stable_last_segment_identity':'K_plus=B0*exp(-s*u)-exp((s-1)*u)*T(u), with B0<0 and T>=0 on [56,64]','whole_interval_K_plus_cells':cells,
 'J_at_20':J[i20].str(24),'scope':'Sign certificate only. A subsequent Stieltjes/partial-summation bound must quantify these adverse tails before replacing the symmetric prime-tail enclosure.'}
(R/'signed-kernel-tail-sign-certificate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
