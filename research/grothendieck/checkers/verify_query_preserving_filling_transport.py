"""Independent rational replay of query-preserving fiber transport claims."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import json,hashlib
HERE=Path(__file__).resolve().parent;R=HERE.parent/'results'
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dot(a,b):return sum(x*y for x,y in zip(a,b))
r=load(R/'query-preserving-filling-transport.json')
for p,h in r['bindings'].items():assert sha(Path(p))==h
assert sha(R/'query-preserving-filling-transport-contract.json')==r['contract_sha256']
own=load(R/'query-relative-tail-interface.json')
for p,h in own['bindings'].items():assert sha(Path(p))==h
A=[list(map(Q,row)) for row in own['source_constraints']['A']];b=list(map(Q,own['source_constraints']['b']));c=list(map(Q,own['objective_coefficients']))
M=[[Q(1)]*3,c,[Q(1),Q(0),Q(0)]]
columns=[list(map(Q,col)) for col in r['positive']['inverse_columns']];N=[list(row) for row in zip(*columns)]
I=[[Q(int(i==j)) for j in range(3)] for i in range(3)]
assert [[dot(row,col) for col in columns] for row in M]==I
assert [[dot(row,col) for col in zip(*M)] for row in N]==I
# Exact coefficient identities authorize all subsequent affine calculations.
def inverse(y):return tuple(dot(row,y) for row in N)
def observe(x):return tuple(dot(row,x) for row in M)
def admitted(x):return all(dot(row,x)<=v for row,v in zip(A,b))
negative=r['negative'];bounds=[]
for f in negative['middle_fibers']:
 S,F=map(Q,f['base']);lo=Q(f['lower']);hi=Q(f['upper']);low=[];high=[]
 for i,(row,v) in enumerate(zip(A,b)):
  coeff=[dot(row,col) for col in columns];rhs=v-coeff[0]*S-coeff[1]*F
  if coeff[2]<0:low.append((rhs/coeff[2],i))
  elif coeff[2]>0:high.append((rhs/coeff[2],i))
  else:assert rhs>=0
 assert lo==max(a for a,i in low)<min(a for a,i in high)==hi
 assert (lo,f['lower_source_row']) in low and (hi,f['upper_source_row']) in high
 for raw,h in zip(f['endpoint_lifts'],(lo,hi)):
  x=tuple(map(Q,raw));assert admitted(x) and observe(x)==(S,F,h)
 bounds.append((lo,hi))
start=tuple(map(Q,negative['outer_start']['source_lift']));end=tuple(map(Q,negative['outer_end']['source_lift']))
assert admitted(start) and admitted(end)
u,v=[tuple(map(Q,f['base'])) for f in negative['middle_fibers']]
assert u==(observe(start)[0],observe(end)[1]) and v==(observe(end)[0],observe(start)[1])
i=negative['audit_feasible_fiber'];j=negative['audit_infeasible_fiber'];threshold=Q(negative['audit_upper']);assert {i,j}=={0,1}
witness=tuple(map(Q,negative['feasible_source_witness']));assert admitted(witness)
assert observe(witness)[:2]==tuple(map(Q,negative['middle_fibers'][i]['base'])) and witness[0]<=threshold<bounds[j][0]
# Normalizing interval position gives an inverse/coherent set transport, but
# its endpoint map already fails the declared raw-x1 audit. This guards the
# scope: impossibility is query-relative, not a cardinality obstruction.
assert bounds[i][0]<=threshold and bounds[j][0]>threshold
p=r['positive'];center=tuple(map(Q,p['center']));base_radii=tuple(map(Q,p['base_radii']));rho=Q(p['scale']);box=[tuple(map(Q,z)) for z in p['box']]
assert rho>0 and all(v>0 for v in base_radii)
assert box==[(v-rho*d,v+rho*d) for v,d in zip(center,base_radii)]
assert inverse(center)==(Q(1000),)*3
assert len(p['row_guards'])==len(A)
for row,bound,guard in zip(A,b,p['row_guards']):
 coeff=[dot(row,col) for col in columns];slack=bound-dot(row,inverse(center));variation=sum(abs(v)*d for v,d in zip(coeff,base_radii))
 assert coeff==list(map(Q,guard['coefficients'])) and slack==Q(guard['slack'])>0 and variation==Q(guard['unscaled_variation'])
 assert rho*variation<=slack/2
assert len(p['corner_lifts'])==8
for raw,y in zip(p['corner_lifts'],product(*box)):
 x=tuple(map(Q,raw['source_lift']));assert y==tuple(map(Q,raw['coordinates']))==observe(x) and admitted(x)
# The inverse maps the entire coordinate box into P by the row guards.
# Therefore P intersect this box is exactly the product parameterization.
bases=list(product(box[0],box[1]))+[center[:2]];tags=[box[2][0],center[2],box[2][1]];count=0
for u,v,w in product(bases,repeat=3):
 for h in tags:
  x=inverse((*u,h));uv=inverse((*v,x[0]));vw=inverse((*w,uv[0]));uw=inverse((*w,x[0]))
  assert vw==uw and inverse((*u,uv[0]))==x and uv[0]==h
  assert all(admitted(t) for t in (x,uv,vw));count+=1
assert count==p['triangle_checks']==375
# Corruption control for the claimed audit equality: the original feasible
# witness cannot be mapped to the other fiber's lower endpoint with same audit.
assert (bounds[i][0]<=threshold)!=(bounds[j][0]<=threshold)
print('PASS: exact unequal fiber intervals, audit-preserving impossibility, affine inverse identities, whole product-slice admission, raw-audit preservation and coherent transport')
