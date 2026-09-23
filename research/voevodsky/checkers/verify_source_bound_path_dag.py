"""Independent Farkas path DAG replay with exact row support and generation."""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json
old=(((-1,0),0),((1,0),1),((0,-1),0),((0,1),1));names=('x-low','x-high','y-low','y-high')
P=(Q(1),Q(2),Q(0),Q(0));Qp=(Q(0),Q(1),Q(1),Q(1));k=tuple(Qp[i]-P[i] for i in range(4))
def digest(rows):return sha256(repr(rows).encode()).hexdigest()
def implied(m,rows):return tuple(sum(Q(rows[i][0][j])*m[i] for i in range(4)) for j in (0,1)),sum(Q(rows[i][1])*m[i] for i in range(4))
def required_support(m):return {names[i] for i,x in enumerate(m) if x}
expected={'P':required_support(P),'Q':required_support(Qp),'edgePQ':required_support(k)|{'P','Q'},'edgeQP':required_support(k)|{'P','Q'},'path':{'edgePQ','edgeQP'}}
assert expected['edgePQ']==set(names)|{'P','Q'}
def check(rows,claimed_generation,dag):
 if claimed_generation!=digest(rows):return 'STALE_SOURCE_GENERATION'
 if any(set(dag.get(key,()))!=need for key,need in expected.items()):return 'INCOMPLETE_OR_EXTRA_SUPPORT'
 def rooted(node,stack=()):
  if node in stack:return False
  if node in names:return True
  return node in dag and all(rooted(t,stack+(node,)) for t in dag[node])
 if not rooted('path'):return 'CYCLIC_OR_UNKNOWN_SUPPORT'
 if implied(P,rows)!=((Q(1),Q(0)),Q(2)):return 'INVALID_ENDPOINT'
 if implied(Qp,rows)!=((Q(1),Q(0)),Q(2)):return 'INVALID_INTERMEDIATE'
 if implied(k,rows)!=((Q(0),Q(0)),Q(0)):return 'INVALID_EDGE_SYZYGY'
 if min((*P,*Qp))<0:return 'NEGATIVE_PROOF_MULTIPLIER'
 return 'ARCHIVED_MATHEMATICAL_PATH_VERIFIED'
D={k:tuple(v) for k,v in expected.items()}
assert check(old,digest(old),D)=='ARCHIVED_MATHEMATICAL_PATH_VERIFIED'
changed=list(old);changed[3]=(changed[3][0],2);changed=tuple(changed)
assert check(changed,digest(old),D)=='STALE_SOURCE_GENERATION'
assert check(changed,digest(changed),D)=='INVALID_INTERMEDIATE'
missing={**D,'edgePQ':tuple(expected['edgePQ']-{'y-high'})}
assert check(old,digest(old),missing)=='INCOMPLETE_OR_EXTRA_SUPPORT'
cyclic={**D,'edgePQ':tuple(expected['edgePQ']|{'path'})}
assert check(old,digest(old),cyclic)=='INCOMPLETE_OR_EXTRA_SUPPORT'
report={'passed':True,'archived_old_generation_math_valid':True,'changed_generation_old_record_refused':'STALE_SOURCE_GENERATION','changed_source_rebound_record_refused':'INVALID_INTERMEDIATE','omitted_y_high_refused':True,'self_cycle_refused':True,'path_support':sorted(set(names)),'scope':'Independent exact mathematical replay under fixed old and hypothetical changed source; equality of source digest is NOT issuer authentication or live authorization.'}
out=Path(__file__).resolve().parents[1]/'results/source-bound-path-dag-verification.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
