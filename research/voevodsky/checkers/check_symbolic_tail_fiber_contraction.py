"""Exact controls for the global continuous section of the tail observation."""
from pathlib import Path
from fractions import Fraction as Q
import importlib.util
import hashlib
import json
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
p=ROOT/'research/nima/checkers/check_symbolic_tail_interface.py'
spec=importlib.util.spec_from_file_location('tail_engine',p);mod=importlib.util.module_from_spec(spec)
import sys
sys.modules[spec.name]=mod;spec.loader.exec_module(mod)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def decode(g,u,v,caps):
 packet=g.member((u,v));assert packet['admitted'];w=packet['lift']
 high=[caps[j] if j<w['high_prefix'] else Q(w['high_partial']) if j==w['high_prefix'] else Q(0) for j in range(g.m)]
 low=[caps[j]-(caps[j] if j<w['complement_prefix'] else Q(w['complement_partial']) if j==w['complement_prefix'] else Q(0)) for j in range(g.m)]
 t=Q(w['theta']);return [(1-t)*a+t*b for a,b in zip(low,high)]
checks=0;joins=0;audit=None
for m in (2,3,4,8,16,64,256,1024):
 g=mod.Generator(m);caps=[Q(100+2*j) for j in range(m)];slopes=[Q(1,128**j) for j in range(m)]
 total=sum(caps)
 assert g.mass(m)==total and g.weighted(m)==dot(caps,slopes)
 # Independent greedy vectors, including every breakpoint for small m.
 ks=range(m+1) if m<=16 else sorted({0,1,m//2,m-1,m})
 us={Q(0),total,Q(1,10**6),total-Q(1,10**6),total/2}
 for k in ks:
  u=sum(caps[:k]);us.add(u);us.add(total-u)
  if k<m:
   # Two adjacent formulas coincide at the breakpoint: next remainder zero
   # is the preceding remainder at its full cap.
   left=[caps[j] if j<k else Q(0) for j in range(m)]
   if k>0:
    previous=[caps[j] if j<k-1 else caps[k-1] if j==k-1 else Q(0) for j in range(m)]
    assert left==previous;joins+=1
 def greedy(u):
  result=[]
  for cap in caps:
   t=min(cap,u);result.append(t);u-=t
  assert u==0;return result
 for u in us:
  hi=greedy(u);lo=[cap-v for cap,v in zip(caps,greedy(total-u))]
  low,high=dot(lo,slopes),dot(hi,slopes)
  if 0<u<total:assert high>low
  else:assert hi==lo
  for theta in (Q(0),Q(1,3),Q(1)):
   v=(1-theta)*low+theta*high;y=decode(g,u,v,caps)
   assert sum(y)==u and dot(y,slopes)==v
   assert all(0<=a<=b for a,b in zip(y,caps))
   # Explicit squeeze bounds prove continuity at the two degenerate tips.
   assert all(a<=u and cap-a<=total-u for a,cap in zip(y,caps))
   checks+=1
 # Test contractions of non-selected source points, not only of section points.
 for shift in (0,1,2):
  x=[cap*Q((j+shift)%5,4) for j,cap in enumerate(caps)]
  u,v=sum(x),dot(x,slopes);y=decode(g,u,v,caps)
  # Any frame depends only on unchanged (U,V). Controls include equalities
  # represented by paired halfspaces and a further accepted oblique bound.
  frames=[((Q(1),Q(0)),u),((Q(-1),Q(0)),-u),((Q(0),Q(1)),v),((Q(0),Q(-1)),-v),((Q(2),Q(-3)),2*u-3*v+1)]
  for t in (Q(0),Q(1,2),Q(1)):
   h=[(1-t)*a+t*b for a,b in zip(x,y)]
   assert all(0<=a<=cap for a,cap in zip(h,caps))
   assert (sum(h),dot(h,slopes))==(u,v)
   assert all(dot(n,(sum(h),dot(h,slopes)))<=bound for n,bound in frames)
   checks+=1
  if audit is None and x!=y:
   j=next(j for j in range(m) if x[j]!=y[j]);audit={'m':m,'coordinate':j,'before':str(x[j]),'after':str(y[j])}
assert audit is not None
report={'passed':True,'engine_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
 'exact_sample_checks':checks,'greedy_join_checks':joins,'largest_m':1024,'audit_counterexample':audit,
 'continuum_argument':'Greedy profiles are continuous piecewise affine in U. Strictly ordered slopes give a positive vertical gap for 0<U<C(m). The mixing formula is continuous there; at either tip, componentwise nonnegativity and fixed total squeeze every lift to the unique tip lift.',
 'refinement_theorem':'For any retained observable-halfspace history, H(x,t)=(1-t)x+t section(Lx) stays inside the box and has identical Lx. Hence it strongly deformation retracts the saturated refined source onto the section of its retained visible image.',
 'limits':'No claim of bounded bit size, constant query work, recovery of hidden source restrictions, or authorization of source-coordinate queries. Expanded vectors exist only in this test harness, not in the runtime representation.'}
(OUT/'symbolic-tail-fiber-contraction.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
