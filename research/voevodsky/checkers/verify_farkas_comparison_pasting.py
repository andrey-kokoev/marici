"""Independent endpoint replay for two postweakening pastings; not equality of 2-cell paths."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
V=Path(__file__).resolve().parents[1]/'results';prior=json.loads((V/'farkas-comparison-whiskering.json').read_text());assert prior['passed']
# Keep proof triple (a,b,c). Independent direct equations for source [0,1].
def certified(p,target):
 a,b,c=map(Q,p);return min(a,b,c)>=0 and b-a==1 and b+c==Q(target)
def normalize(p,target,source_bound=Q(1)):
 if Q(source_bound)!=1:raise ValueError('PRIMITIVE_BOUND_MISMATCH')
 assert certified(p,target)
 a,b,c=map(Q,p);return (a+c,b+c,Q(0))
def weaken(p,t,u):
 assert Q(u)>=Q(t) and certified(p,t)
 a,b,c=map(Q,p);return (a,b,c+Q(u)-Q(t))
checks=0;different_paths=0
for t,u,v in product((Q(1),Q(3,2),Q(2),Q(3),Q(4)),repeat=3):
 if not t<=u<=v:continue
 # Choose a valid proof with surplus t-1.
 p=(Q(0),Q(1),t-1);assert certified(p,t)
 direct=normalize(weaken(p,t,v),v)
 staged_mid=normalize(weaken(p,t,u),u)
 staged_end=normalize(weaken(staged_mid,u,v),v)
 assert direct==staged_end==(v-1,v,Q(0))
 # The complete derivation strings are distinct whenever the intermediate
 # step is nontrivial; equal endpoints are NOT equality of 2-cell histories.
 path1=('weaken',str(t),str(v),'normalize')
 path2=('weaken',str(t),str(u),'normalize','weaken',str(u),str(v),'normalize')
 if path1!=path2:different_paths+=1
 checks+=1
assert checks>20 and different_paths>0
# The original proof p=(1,2,1) has target 3; direct and staged 3->4->5.
p=(Q(1),Q(2),Q(1));assert certified(p,3)
assert normalize(weaken(p,3,5),5)==normalize(weaken(normalize(weaken(p,3,4),4),4,5),5)==(Q(4),Q(5),Q(0))
try:normalize(p,3,source_bound=Q(2))
except ValueError:bound_refused=True
else:raise AssertionError('changed primitive bound accepted')
# Postweaken changes public target only, not proof/history authority; labels
# for comparison steps must remain rooted in same primitive rows.
report={'passed':True,'two_step_pastings_checked':checks,'distinct_derivation_strings':different_paths,'endpoint_coherence':True,'proof_path_coherence':'unsupported; no declared 3-cell','changed_source_bound_refused':bound_refused,'scope':'Independent rational endpoint replay, fixed primitive interval and positive target weakenings. No live authority, higher proof equality or analytic functor.'}
(V/'farkas-comparison-pasting-verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
