"""Exact finite-jet controls for the scalar filtered comparison contract."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
paths=[Path(__file__),HERE/'filtered-comparison-readout.md',HERE/'triangle-readout-jet.md']
def hashes():return {p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
def mul(u,v,N):return [sum((u[i]*v[n-i] for i in range(n+1)),F(0)) for n in range(N+1)]
def inv(u,N):
 assert u[0]
 v=[1/u[0]]
 for n in range(1,N+1):v.append(-sum((u[i]*v[n-i] for i in range(1,n+1)),F(0))/u[0])
 return v
before=hashes();count=0
for N in range(7):
 for lead in map(F,('-2','1/2','1','3')):
  u=[lead]+[F((-1)**i*(i+1),3) for i in range(1,N+1)]
  w=[F(2)]+[F(i,5) for i in range(1,N+1)]
  G=[F(3*i-2,7) for i in range(N+1)]
  ui=inv(u,N);wi=inv(w,N);P=mul(u,G,N)
  assert mul(ui,P,N)==G
  assert mul(w,P,N)==mul(mul(w,u,N),G,N)
  assert mul(inv(mul(w,u,N),N),mul(w,P,N),N)==G
  assert inv(mul(w,u,N),N)==mul(ui,wi,N)
  c=abs(lead);M=max([abs(x) for x in u[1:]] or [F(0)])
  assert sum(map(abs,ui))<=1/c*(1+M/c)**N
  # Missing final P coefficient cannot distinguish this perturbation.
  altered=G.copy();altered[N]+=1
  PA=mul(u,altered,N)
  assert PA[:N]==P[:N] and PA[N]-P[N]==u[0]
  if N:
   identity=[F(1)]+[F(0)]*N;changed=identity.copy();changed[N]=F(2)
   hidden=inv(changed,N)
   assert changed[:N]==identity[:N] and hidden[N]==-2
   assert mul(changed,hidden,N)==identity
  count+=1
instability=[]
for n in (10,100,1000,10000):
 x=F(1,n);G0=[F(1),F(0)];G1=[F(1),F(1)];u=[x,F(0)]
 P0=mul(u,G0,1);P1=mul(u,G1,1)
 assert max(abs(a-b) for a,b in zip(P0,P1))==x
 assert mul(inv(u,1),P1,1)[1]-mul(inv(u,1),P0,1)[1]==1
 instability.append({'x':str(x),'input_jet_difference':str(x),'readout_difference':1,'inverse_gain':n})
assert before==hashes()
report={'passed':True,'source_unchanged':True,'source_sha256':before,'jet_fixtures':count,
 'instability':instability,'contract':'Shifted finite jets recover an independently specified coefficient when the leading comparison coefficient is a unit.',
 'falsifier':'Sufficient algebraic jet order does not ensure boundary continuity when the inverse comparison is unbounded.',
 'scope':'Exact rational finite fixtures and written general proofs; no physical readout selection, source ownership transfer or automatic analytic completion.'}
(HERE/'filtered-comparison-readout.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
