"""Independent LOCAL row anchor verifies rotation proof DAG, not execution."""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json
# Explicit locally trusted mathematical source manifest. This anchor is a
# checker assumption; it is NOT an authenticated provider or operator act.
TRUSTED={'low-x':((-1,0),0),'high-x':((1,0),1),'low-y':((0,-1),0),'high-y':((0,1),1)}
def digest(row):return sha256(json.dumps(row,separators=(',',':')).encode()).hexdigest()
anchors={name:digest(row) for name,row in TRUSTED.items()}
leaf={'a':((1,2,0,0),(1,0),2),'b':((0,0,1,2),(0,1),2),
      'c':((0,1,0,0),(1,0),1),'d':((0,0,0,1),(0,1),1)}
def verify_leaf(name,rows):
 if set(rows)!=set(TRUSTED):return False
 if any(digest(rows[k])!=anchors[k] for k in anchors):return False
 m,v,T=leaf[name];items=[rows[k] for k in TRUSTED]
 return all(z>=0 for z in m) and tuple(sum(items[i][0][j]*m[i] for i in range(4)) for j in range(2))==v and sum(items[i][1]*m[i] for i in range(4))==T
def support(node,deps,rows,stack=()):
 if node in stack:return False
 if node in leaf:return verify_leaf(node,rows)
 return node in deps and bool(deps[node]) and all(support(k,deps,rows,stack+(node,)) for k in deps[node])
D={'rotation-1':('a','b','c','d'),'rotation-2':('rotation-1','a','b','c','d'),
   'paired-record':('rotation-2','a','b','c','d')}
assert support('paired-record',D,TRUSTED)
forged={**TRUSTED,'high-x':((1,0),2)}
assert not support('paired-record',D,forged)
assert not support('paired-record',D,{k:v for k,v in TRUSTED.items() if k!='low-y'})
cycle={**D,'rotation-1':('rotation-2',)}
assert not support('paired-record',cycle,TRUSTED)
assert not support('paired-record',{'paired-record':('unknown-root',)},TRUSTED)
report={'passed':True,'four_leaf_farkas_certificates_verified':True,'locally_anchored_primitive_row_digests':True,'rotation_support_dag_reaches_rows':True,'refused':['changed-row-bound-with-same-id','omitted-row','cyclic-support','unknown-root'],'trust_boundary':'Embedded local mathematical source manifest; digest checks integrity against this assumption, NOT independent provider authentication or actual execution authority.'}
out=Path(__file__).resolve().parents[1]/'results/evidence-rooted-rotation.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
