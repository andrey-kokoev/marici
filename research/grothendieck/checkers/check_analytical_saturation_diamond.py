"""Source-backed saturation diamond and exact convex-image classification."""
from pathlib import Path
from fractions import Fraction as Q
import json,hashlib,subprocess,sys
import query_relative_tail_geometry as g
HERE=Path(__file__).resolve().parent;R=HERE.parent/'results'
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dot(a,b):return sum(x*y for x,y in zip(a,b))
subprocess.run([sys.executable,str(HERE/'verify_query_relative_tail_interface.py')],check=True)
p=R/'query-relative-tail-interface.json';own=load(p)
A=[list(map(Q,row)) for row in own['source_constraints']['A']];b=list(map(Q,own['source_constraints']['b']));c=list(map(Q,own['objective_coefficients']))
assert c[2]<c[1]<c[0]<0
contract={'schema':'analytical-saturation-diamond.v1','source_sha256':sha(p),'observers':['S=sum x_i','F=sum c_i*x_i'],'comparison':'S_F(S_S(C)) versus S_S(S_F(C)), relative to each explicitly restricted source','restrictions':['none','S<=B3/2','S=B3/2','small observable rectangle with lifted corners'],'scope':'Convex affine-restricted owning moment relaxation. Constructed restrictions are admissible control slices, not newly acquired actual-prime evidence.'}
cp=R/'analytical-saturation-diamond-contract.json';cp.write_text(json.dumps(contract,indent=2)+'\n')
a=Q(1000);start=(Q(0),a,Q(0));middle=(a,Q(0),Q(0));end=(Q(0),Q(0),a*c[0]/c[2])
for x in (start,middle,end):assert all(dot(row,x)<=v for row,v in zip(A,b))
def image(x):return sum(x),dot(c,x)
s0,f0=image(start);sm,fm=image(middle);s1,f1=image(end)
assert s0==sm and fm==f1
# The missing reverse middle would have (S,F)=(s1,f0). Every source point
# satisfies F>=c3*S because masses are nonnegative and c3 is smallest.
slack=f0-c[2]*s1;assert slack<0
B=Q(load(R/'ternary-tail-budget-dpc.json')['prefix_budget_upper'][-1])
# Construct an interior rectangle via actual source lifts, not membership
# inferred from separate ranges. Fix x3=1000 and vary S,F around the center.
center=(Q(1000),)*3;S,F=image(center);ds=Q(1);df=(c[0]-c[1])/10
corners=[]
for s in (S-ds,S+ds):
 for f in (F-df,F+df):
  x3=Q(1000);x1=(f-c[2]*x3-c[1]*(s-x3))/(c[0]-c[1]);x2=s-x3-x1;x=(x1,x2,x3)
  assert image(x)==(s,f) and all(dot(row,x)<=v for row,v in zip(A,b))
  corners.append({'observable':[str(s),str(f)],'source_lift':list(map(str,x))})
# All rectangle corners have lifts; convexity proves the complete rectangle
# belongs to the source image. Restricting to it therefore has that exact image.
cases={'none':[], 'S<=B3/2':[((Q(1),Q(0)),B/2)], 'S=B3/2':[((Q(1),Q(0)),B/2),((Q(-1),Q(0)),-B/2)],
 'rectangle':[((Q(1),Q(0)),S+ds),((Q(-1),Q(0)),-S+ds),((Q(0),Q(1)),F+df),((Q(0),Q(-1)),-F+df)]}
results=[]
for name,frames in cases.items():
 AA=list(A);bb=list(b)
 for n,d in frames:AA.append([n[0]+n[1]*v for v in c]);bb.append(d)
 poly=g.project(AA,bb,c);pts=[z for z,x in poly]
 assert pts
 dim=0 if len(pts)==1 else 1 if len(pts)==2 else 2
 box={(s,f) for s in (min(z[0] for z in pts),max(z[0] for z in pts)) for f in (min(z[1] for z in pts),max(z[1] for z in pts))}
 rectangular=box.issubset(set(pts));commutes=dim<2 or rectangular
 results.append({'name':name,'frames':[{'normal':list(map(str,n)),'upper':str(d)} for n,d in frames],'image':[{'observable':list(map(str,z)),'source_lift':list(map(str,x))} for z,x in poly],'affine_dimension':dim,'rectangular':rectangular,'commutes':commutes})
assert [v['commutes'] for v in results]==[False,False,True,True]
# A simple upper-total tightening does not repair the exhibited obstruction.
assert max(map(sum,(start,middle,end)))<=B/2
out={'schema':'analytical-saturation-diamond-result.v1','contract_sha256':sha(cp),'diamond':{'start':list(map(str,start)),'S_middle':list(map(str,middle)),'end':list(map(str,end)),'missing_reverse_observable':[str(s1),str(f0)],'nonnegative_source_row':{'coefficients':list(map(str,[v-c[2] for v in c])),'required_lower':'0','candidate_value':str(slack)}},'rectangle_corners':corners,'cases':results,'bindings':{str(t):sha(t) for t in (Path(__file__),HERE/'query_relative_tail_geometry.py',cp,p)},'scope':'Classification uses the compact convex image theorem proved in the accompanying note; finite slices do not prove the theorem by sampling.'}
(R/'analytical-saturation-diamond.json').write_text(json.dumps(out,indent=2)+'\n')
print([(v['name'],v['affine_dimension'],v['commutes']) for v in results])
