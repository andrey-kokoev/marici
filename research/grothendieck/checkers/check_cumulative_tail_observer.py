"""Finite cumulative-mass primal/dual sandwich for the actual combined kernel.
No midpoint claim. Uses the existing finite N=1e6 evidence with hash checks.
"""
from pathlib import Path
from fractions import Fraction as Q
import json,hashlib
from flint import arb,ctx
ctx.prec=384
HERE=Path(__file__).resolve().parent;R=HERE.parent/'results'
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def aq(q):return arb(q.numerator)/q.denominator
def ends(z):return Q(str(z.lower().fmpq())),Q(str(z.upper().fmpq()))
def enc(z):return {'lower':str(z[0]),'upper':str(z[1])}
bp=R/'directed-C-only-Abel-branch.json';branch=load(bp)
for p,h in branch['bindings'].items():assert sha(Path(p))==h
E=branch['finite_pairing_evidence'];assert E['N']==1000000
psi=tuple(Q(E['psi_N'][k]) for k in ('lower','upper'))
f=load(R/'time-bin-cubic-observer.json')['filters']
ts=[Q(int(z[0]),int(z[1])) for z in f['nodes']];v=[]
for side in (0,1):
 z=f['bulk'][side];v.append([aq(Q(int(n),int(f['nodal_denominator']))/Q(int(z['normalizer'][0]),int(z['normalizer'][1]))) for n in z['nodal_numerators']])
s=arb(7)/2;b=arb(3)/2;lam=arb(4);d=arb(2);a=s-1
T=[arb(0)]*len(ts);J=[arb(0)]*len(ts)
slopes=[[(z-y)/aq(hi-lo) for lo,hi,y,z in zip(ts,ts[1:],vs,vs[1:])] for vs in v]
for i in range(len(ts)-2,-1,-1):
 lo,hi=map(aq,ts[i:i+2]);m=slopes[0][i];p,z=v[0][i:i+2]
 T[i]=T[i+1]+(-lam*lo).exp()*(p/lam+m/lam**2)-(-lam*hi).exp()*(z/lam+m/lam**2)
for i in range(len(ts)-1):
 lo,hi=map(aq,ts[i:i+2]);m=slopes[1][i];p,z=v[1][i:i+2]
 J[i+1]=J[i]+(d*hi).exp()*(z/d-m/d**2)-(d*lo).exp()*(p/d-m/d**2)
def kernel(u,i):
 p=v[0][i]+slopes[0][i]*(u-aq(ts[i]));m=v[1][i]+slopes[1][i]*(u-aq(ts[i]))
 cp=T[i+1]-(-lam*aq(ts[i+1])).exp()*(v[0][i+1]/lam+slopes[0][i]/lam**2)
 cm=J[i]-(d*aq(ts[i])).exp()*(v[1][i]/d-slopes[1][i]/d**2)
 kp=T[0]*(-s*u).exp()-(-b*u).exp()*(p/lam+slopes[0][i]/lam**2)-cp*(a*u).exp()
 km=-cm*(-s*u).exp()-(-b*u).exp()*(m/d-slopes[1][i]/d**2)
 derivative=-s*(T[0]-cm)*(-s*u).exp()+(-b*u).exp()*(b*(p/lam+slopes[0][i]/lam**2+m/d-slopes[1][i]/d**2)-slopes[0][i]/lam-slopes[1][i]/d)-a*cp*(a*u).exp()
 return kp+km,derivative
def capacity(u):return 2*arb(2).log()*u.exp()+u+arb(2).log()
# Exact rational primal/dual solution: max w.x subject to x>=0, prefix x<=c.
def solve(weights,caps):
 n=len(weights);h=[Q(0)]*n;dest=[None]*n;best=Q(0);where=None
 for i in range(n-1,-1,-1):
  if weights[i]>best:best=weights[i];where=i
  h[i]=best;dest[i]=where
 atoms=[Q(0)]*n;prev=Q(0);dual=Q(0)
 for i in range(n):
  delta=caps[i]-prev;assert delta>=0;dual+=delta*h[i]
  if dest[i] is not None:atoms[dest[i]]+=delta
  prev=caps[i]
 running=Q(0)
 for mass,cap in zip(atoms,caps):running+=mass;assert mass>=0 and running<=cap
 primal=sum(w*z for w,z in zip(weights,atoms));assert primal==dual
 assert all(h[i]>=weights[i] and h[i]>=0 and (i==n-1 or h[i]>=h[i+1]) for i in range(n))
 return primal,{'nonzero_atoms':sum(z>0 for z in atoms),'envelope_runs':1+sum(h[i]!=h[i-1] for i in range(1,n))}
# A tiny strict-loss witness checks the optimization independently of kernels.
assert solve([Q(-1),Q(1)],[Q(1),Q(2)])[0]==2
# For w=(-1,1,-1), pointwise independent prefix masses give min=-5,
# whereas the feasible cumulative minimum is -3: a strict-loss control.
assert -solve([Q(1),Q(-1),Q(1)],[Q(1),Q(2),Q(3)])[0]==-3
u0=arb(1000000).log();left=ends(u0)[1];start=left;mesh=512
weights=[];points=[];caps_lo=[];caps_hi=[];box_lo=Q(0);box_hi=Q(0)
# Outward starting strip is charged absolutely, not silently dropped.
i0=next(i for i in range(len(ts)-1) if ts[i]<start<ts[i+1])
strip=u0.union(aq(start));_,dk=kernel(strip,i0)
strip_error=ends(abs(dk)*capacity(aq(start))*(aq(start)-u0))[1]
for i in range(i0,len(ts)-1):
 left=max(start,ts[i]);right=ts[i+1]
 while left<right:
  end=min(right,left+Q(1,mesh));u=aq(left).union(aq(end));k,dk=kernel(u,i)
  weights.append(ends(k));points.append(ends(kernel(aq(end),i)[0]))
  cap=ends(capacity(aq(end)));caps_lo.append(cap[0]-psi[1]);caps_hi.append(cap[1]-psi[0])
  # Relaxed minimum = -integral max(K',0) M. Interval rectangle enclosure.
  dl,dh=ends(dk);ml=ends(capacity(aq(left)))[0]-psi[1];mh=cap[1]-psi[0]
  box_lo-=(end-left)*max(Q(0),dh)*mh
  box_hi-=(end-left)*max(Q(0),dl)*ml
  left=end
assert min(caps_lo)>0
# min K = -max(-K). Outer cell upper weights give a rigorous lower bound.
outer,dualinfo=solve([-w[0] for w in weights],caps_hi)
# Exact atoms at RIGHT endpoints are feasible under the lower capacity;
# upper point weights yield a rigorous upper bound on their actual objective.
primal,primalinfo=solve([-w[1] for w in points],caps_lo)
# Tail |K|=|T0-J64| exp(-s u); total psi upper, discarding subtraction,
# bounds its Stieltjes integral even if all earlier budget is left unused.
h=arb(64);co=T[0]-J[-1];assert co<0
suffix=abs(co)*(2*arb(2).log()*s/(s-1)*((1-s)*h).exp()+(-s*h).exp()*(h+arb(2).log()+1/s))
err=ends(suffix)[1]+strip_error
joint=(-outer-err,-primal+strip_error)
# K'= -s co exp(-su)>0 on the suffix. Box integral uses M exactly there.
W=2*arb(2).log()*((1-s)*h).exp()/(s-1)+(-s*h).exp()*((h+arb(2).log()-aq(psi[0]).union(aq(psi[1])))/s+1/s**2)
wl,wh=ends(s*co*W)
relaxed=(box_lo+wl-strip_error,box_hi+wh+strip_error)
gap=joint[0]-relaxed[1]
out={'schema':'cumulative-tail-observer.v1','N':1000000,'mesh':mesh,'cells':len(weights),'joint_minimum':enc(joint),'pointwise_relaxed_minimum':enc(relaxed),'strict_gap_lower':str(gap),'strict_loss_certified':gap>0,'outer_dual':dualinfo,'feasible_primal':primalinfo,'suffix_and_start_error_upper':str(err),'bindings':{str(bp):sha(bp),str(Path(__file__)):sha(Path(__file__))},'scope':'Continuous positive measures under the same Chebyshev capacity; not a prime-realizability claim or midpoint verdict.'}
(R/'cumulative-tail-observer.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ('cells','strict_loss_certified','outer_dual','feasible_primal')},indent=2))
print('joint',*[float(z) for z in joint],'relaxed',*[float(z) for z in relaxed],'gap',float(gap))
