"""Audit-preserving middle-fiber obstruction and coherent product-slice repair."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import json,hashlib,subprocess,sys
HERE=Path(__file__).resolve().parent;R=HERE.parent/'results'
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dot(a,b):return sum(x*y for x,y in zip(a,b))
subprocess.run([sys.executable,str(HERE/'verify_analytical_saturation_diamond.py')],check=True)
source_path=R/'query-relative-tail-interface.json';source=load(source_path)
A=[list(map(Q,row)) for row in source['source_constraints']['A']];b=list(map(Q,source['source_constraints']['b']));c=list(map(Q,source['objective_coefficients']))
assert c[1]!=c[2]
contract={'schema':'query-preserving-filling-transport.v1','source_sha256':sha(source_path),'base_observables':['S=sum x','F=sum c_i*x_i'],'witness_audits':'all rational threshold predicates x1<=r, with their exact truth values','negative_scope':'middle fibers of a commuting rectangle in the owning moment carrier','positive_scope':'an explicitly constructed affine product slice inside the same carrier, with a common nondegenerate x1 interval','transport':'preserve raw x1 and replace the base (S,F); no renormalization of witness audits','boundary':'The positive slice is a controlled restriction, not evidence that actual prime masses lie there. Bin2/bin3 audits are outside this transport contract.'}
cp=R/'query-preserving-filling-transport-contract.json';cp.write_text(json.dumps(contract,indent=2)+'\n')
def inverse(S,F,h):
 x2=(F-c[2]*S-(c[0]-c[2])*h)/(c[1]-c[2]);return h,x2,S-h-x2
def obs(x):return sum(x),dot(c,x)
def admitted(x):return all(dot(a,x)<=v for a,v in zip(A,b))
# Exact inverse matrix, columns corresponding to S,F,h.
columns=[inverse(Q(1),Q(0),Q(0)),inverse(Q(0),Q(1),Q(0)),inverse(Q(0),Q(0),Q(1))]
for j,col in enumerate(columns):assert (*obs(col),col[0])==tuple(Q(int(i==j)) for i in range(3))
def fiber(z):
 const=inverse(*z,Q(0));direction=columns[2];lower=[];upper=[]
 for i,(a,v) in enumerate(zip(A,b)):
  coeff=dot(a,direction);rhs=v-dot(a,const)
  if coeff<0:lower.append((rhs/coeff,i))
  elif coeff>0:upper.append((rhs/coeff,i))
  else:assert rhs>=0
 lo,li=max(lower);hi,ui=min(upper);assert lo<=hi
 assert admitted(inverse(*z,lo)) and admitted(inverse(*z,hi))
 return {'base':list(map(str,z)),'lower':str(lo),'upper':str(hi),'lower_source_row':li,'upper_source_row':ui,'endpoint_lifts':[list(map(str,inverse(*z,t))) for t in (lo,hi)]}
diamond=load(R/'analytical-saturation-diamond.json');corners=[tuple(map(Q,v['observable'])) for v in diamond['rectangle_corners']]
# Start=(S_low,F_low), end=(S_high,F_high). Middle fibers are the other corners.
assert corners[0][0]==corners[1][0] and corners[0][1]==corners[2][1]
assert corners[3][0]==corners[2][0] and corners[3][1]==corners[1][1]
fibers=[fiber(z) for z in (corners[1],corners[2])]
los=list(map(lambda f:Q(f['lower']),fibers));assert los[0]!=los[1]
small=0 if los[0]<los[1] else 1;large=1-small;threshold=sum(los)/2
witness=inverse(*map(Q,fibers[small]['base']),los[small]);assert witness[0]<=threshold<los[large]
negative={'outer_start':diamond['rectangle_corners'][0],'outer_end':diamond['rectangle_corners'][3],'middle_fibers':fibers,'audit_upper':str(threshold),'audit_feasible_fiber':small,'audit_infeasible_fiber':large,'feasible_source_witness':list(map(str,witness)),'reason':'Every audit-preserving bijection must preserve x1 exactly; the two x1 intervals differ.'}
# Product slice: all three coordinates S,F,h vary independently in a box
# around a strictly admitted source point. Choose a certified common radius
# using all transformed source inequalities, not representative lifts alone.
center_x=(Q(1000),)*3;S,F=obs(center_x);center=(S,F,Q(1000));assert admitted(center_x)
base_radii=(Q(1),(c[0]-c[1])/10,Q(1));assert min(base_radii)>0
rho=Q(1);row_guards=[]
for a,v in zip(A,b):
 slack=v-dot(a,center_x);assert slack>0
 coeff=[dot(a,col) for col in columns];variation=sum(abs(z)*w for z,w in zip(coeff,base_radii))
 if variation:rho=min(rho,slack/(2*variation))
 row_guards.append((coeff,slack,variation))
radii=tuple(rho*w for w in base_radii);assert min(radii)>0
box=[(z-r,z+r) for z,r in zip(center,radii)]
for (coeff,slack,variation) in row_guards:assert sum(abs(z)*r for z,r in zip(coeff,radii))<=slack/2
corner_lifts=[]
for y in product(*box):
 x=inverse(*y);assert admitted(x) and (*obs(x),x[0])==y
 corner_lifts.append({'coordinates':list(map(str,y)),'source_lift':list(map(str,x))})
# P* = P intersect { (S,F,h) in box }; guards imply it is exactly the inverse
# image of that entire box. Every base fiber has the same raw-h interval.
bases=list(product(box[0],box[1]))+[(center[0],center[1])];tags=[box[2][0],center[2],box[2][1]]
def transport(x,target):return inverse(*target,x[0])
checks=0
for u,v,w in product(bases,repeat=3):
 for h in tags:
  x=inverse(*u,h);uv=transport(x,v);vw=transport(uv,w);uw=transport(x,w)
  assert vw==uw and transport(uv,u)==x and uv[0]==h and admitted(vw)
  checks+=1
out={'schema':'query-preserving-filling-transport-result.v1','contract_sha256':sha(cp),'negative':negative,'positive':{'inverse_columns':[list(map(str,col)) for col in columns],'center':list(map(str,center)),'base_radii':list(map(str,base_radii)),'scale':str(rho),'box':[[str(a),str(b)] for a,b in box],'row_guards':[{'coefficients':list(map(str,a)),'slack':str(s),'unscaled_variation':str(v)} for a,s,v in row_guards],'corner_lifts':corner_lifts,'triangle_checks':checks,'identity':'T_(v,w)(T_(u,v)(x))=inverse(w,x1)=T_(u,w)(x)','audit_preservation':'x1 unchanged exactly for all transported witnesses'},'status':'OBSTRUCTION_ON_FULL_RECTANGLE_AND_COHERENT_TRANSPORT_ON_PRODUCT_SLICE','bindings':{str(p):sha(p) for p in (Path(__file__),cp,source_path,R/'analytical-saturation-diamond.json')},'scope':'No impossibility claim for query-forgetting transports. Positive repair changes the admitted carrier, not just coordinates on the negative carrier.'}
(R/'query-preserving-filling-transport.json').write_text(json.dumps(out,indent=2)+'\n')
print('Certified unequal middle audit fibers; exact product-slice transport;',checks,'triangle controls.')
