"""Parameterized contractions of actual analytical middle-witness fibers.

Continuum certificate: bilinear section is a convex combination of four
owning source lifts; straight-line contraction preserves each affine fiber.
Exact samples check implementation, not the continuum theorem by extrapolation.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import subprocess
import sys
import json
import hashlib
ROOT=Path(__file__).resolve().parents[3];G=ROOT/'research/grothendieck';OUT=ROOT/'research/voevodsky/results'
p=G/'results/analytical-saturation-diamond.json';tail=G/'results/ternary-tail-budget-dpc.json'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,x):p.write_text(json.dumps(x,indent=2)+'\n')
cp=OUT/'convex-filling-coherence-contract.json'
save(cp,{'diamond_sha256':sha(p),'tail_sha256':sha(tail),
 'source':'Owning convex moment carrier restricted to its certified interior (S,F) rectangle.',
 'witness_identity':'Ordinary topological paths inside fixed (S,F) source fibers; no discrete identity assumption.',
 'section':'Bilinear convex interpolation of the four independently certified corner lifts.',
 'contraction':'H(x,t)=(1-t)x+t section(S(x),F(x)).',
 'prediction':'Continuous fiberwise contractions yield continuous homotopy equivalences between opposite middle fibers; center-based comparison composites admit coherent fillers.',
 'scope':'S,F observations preserved during each fiber contraction. Additional bin-level audits need not descend.'})
subprocess.run([sys.executable,str(G/'checkers/verify_analytical_saturation_diamond.py')],check=True,capture_output=True,text=True)
d=json.loads(p.read_text());t=json.loads(tail.read_text())
caps=list(map(Q,t['atom_capacity_upper']));budgets=list(map(Q,t['prefix_budget_upper']));c=[Q(w['lower']) for w in t['weights']]
corner={tuple(map(Q,v['observable'])):tuple(map(Q,v['source_lift'])) for v in d['rectangle_corners']}
S=sorted({s for s,f in corner});F=sorted({f for s,f in corner});assert len(S)==len(F)==2 and len(corner)==4

def obs(x):return sum(x),sum(a*b for a,b in zip(c,x))
def admitted(x):
 s,f=obs(x)
 return all(0<=a<=b for a,b in zip(x,caps)) and all(sum(x[:i+1])<=budgets[i] for i in range(3)) and S[0]<=s<=S[1] and F[0]<=f<=F[1]
def section(s,f):
 u=(s-S[0])/(S[1]-S[0]);v=(f-F[0])/(F[1]-F[0])
 weights=((1-u)*(1-v),(1-u)*v,u*(1-v),u*v)
 assert all(w>=0 for w in weights) and sum(weights)==1
 verts=[corner[S[i],F[j]] for i,j in product((0,1),repeat=2)]
 x=tuple(sum(w*y[k] for w,y in zip(weights,verts)) for k in range(3))
 assert obs(x)==(s,f)
 return x
for z,x in corner.items():assert admitted(x) and obs(x)==z
# Explicit affine identity: the kernel direction fixes both declared observables.
k=(c[1]-c[2],c[2]-c[0],c[0]-c[1]);scale=max(map(abs,k));k=tuple(v/scale for v in k)
assert sum(k)==0 and sum(a*b for a,b in zip(c,k))==0 and k[0]!=0

def blend(x,y,q):return tuple((1-q)*a+q*b for a,b in zip(x,y))
def H(x,q):return blend(x,section(*obs(x)),q)
parameters=(Q(0),Q(1,2),Q(1))
centers=[];sample_checks=0;witnesses=[]
for u,v in product(parameters,repeat=2):
 z=(S[0]+u*(S[1]-S[0]),F[0]+v*(F[1]-F[0]))
 center=section(*z);centers.append(center)
 for sign in (-1,0,1):
  x=tuple(a+Q(sign,2)*b for a,b in zip(center,k))
  assert admitted(x) and obs(x)==z;witnesses.append(x)
  for q in parameters:
   hx=H(x,q);assert admitted(hx) and obs(hx)==z
   assert H(center,q)==center
   sample_checks+=1
  assert H(x,0)==x and H(x,1)==center
# For fixed outer source points a,b the two middle spaces lie over crossed
# coordinates. Constant-to-center maps are homotopy inverses, not bijections.
diamond_checks=0
for a,b in product(centers,repeat=2):
 sa,fa=obs(a);sb,fb=obs(b)
 u=section(sa,fb);v=section(sb,fa)
 assert admitted(u) and admitted(v)
 # f:U->V is constantly v; g:V->U constantly u. H is the explicit gf~id.
 for q in parameters:
  for sign in (-1,1):
   x=tuple(uu+Q(sign,2)*kk for uu,kk in zip(u,k))
   y=tuple(vv+Q(sign,2)*kk for vv,kk in zip(v,k))
   assert obs(H(x,q))==(sa,fb) and obs(H(y,q))==(sb,fa)
   diamond_checks+=1
# A 2-parameter filler between pointwise paths in the SAME fiber is convex.
# Formula preserves a common boundary wherever the two inputs agree.
filler_checks=0
for center in centers:
 x=tuple(a+k0/2 for a,k0 in zip(center,k));y=tuple(a-k0/2 for a,k0 in zip(center,k))
 for s,q in product(parameters,repeat=2):
  hx=H(x,s);hy=H(y,s);filler=blend(hx,hy,q)
  assert admitted(filler) and obs(filler)==obs(center)
  if s==1:assert filler==center
  filler_checks+=1
# Demonstrate nonpreservation of an undeclared bin read along a valid contraction.
center=centers[4];x=tuple(a+b/2 for a,b in zip(center,k))
assert x[0]!=center[0] and obs(x)==obs(center)
assert sha(p)==json.loads(cp.read_text())['diamond_sha256'] and sha(tail)==json.loads(cp.read_text())['tail_sha256']
report={'passed':True,'contract_sha256':sha(cp),
 'certified_corner_lifts':4,'sampled_fiber_contraction_checks':sample_checks,
 'sampled_parameterized_diamond_checks':diamond_checks,'sampled_two_parameter_filler_checks':filler_checks,
 'continuum_proof':'Bilinear nonnegative weights sum to one and reproduce (S,F); source convexity gives a continuous section. Convex interpolation with that section contracts each fiber continuously, fixing the section. These identities hold for all real parameters.',
 'coherence_construction':'Comparisons between nonempty fibers factor through their chosen centers. Positive-length comparison composites are the same target-center map. Identity comparisons have the explicit contraction homotopy. Compatible higher boundary homotopies in a fixed convex fiber admit continuous cone extensions using its center.',
 'reversal':'Exchange the two middle-fiber roles and the two center maps; the contractions supply both homotopy-inverse laws.',
 'observation_boundary':'Only S,F and their functions are guaranteed to descend. The explicit kernel-direction perturbation changes x1 along a valid fiber contraction.',
 'scope':'Ordinary topological homotopy of this convex source restriction; does not authorize bin-audit erasure, physical backward execution, or claim a fully formalized infinity-categorical coherence package.'}
save(OUT/'convex-filling-coherence.json',report)
print(json.dumps(report,indent=2))
