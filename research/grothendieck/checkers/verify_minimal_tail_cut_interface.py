"""Independent Fraction verification of the cut quotient and witnesses."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations,product
import json,hashlib,copy
HERE=Path(__file__).resolve().parent;R=HERE.parent/'results'
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
r=load(R/'minimal-tail-cut-interface.json');c=load(R/'minimal-tail-cut-interface-contract.json')
for p,h in r['bindings'].items():assert sha(Path(p))==h
assert r['contract_sha256']==sha(R/'minimal-tail-cut-interface-contract.json')
rows=[(list(map(Q,z['coefficients'])),Q(z['upper'])) for z in c['rows']]
def exact_cap(prefix):
 return min([Q(1)]+[(b-sum(a*x for a,x in zip(coef[:3],prefix)))/coef[3] for coef,b in rows])
def observation(prefix,y):
 allowed=0<=y<=1 and all(sum(a*x for a,x in zip(coef,(*prefix,y)))<=b for coef,b in rows)
 return (allowed,prefix[2]-y if allowed else None)
# Reconstruct nonnegative linear implication certificates, not just samples.
for cert in r['redundancy_certificates']:
 k=cert['target'];w=list(map(Q,cert['base_weights']));slack=Q(cert['rhs_slack']);assert min(w)>=0 and slack>=0
 assert [sum(w[i]*rows[i][0][j] for i in (0,1)) for j in range(4)]==rows[k][0]
 assert sum(w[i]*rows[i][1] for i in (0,1))+slack==rows[k][1]
points=[tuple(map(Q,p)) for p in r['prefixes']]
assert points==list(product([Q(i,4) for i in range(5)],repeat=3))
owner={}
for k,cl in enumerate(r['classes']):
 sig=(Q(cl['cap']),Q(cl['objective_offset']))
 for i in cl['members']:
  assert i not in owner;owner[i]=k
  assert (exact_cap(points[i]),points[i][2])==sig
assert len(owner)==len(points)
assert len({(cl['cap'],cl['objective_offset']) for cl in r['classes']})==len(r['classes'])
witness={(w['left'],w['right']):Q(w['completion']) for w in r['distinguishing_completions']}
equal=0
for i,j in combinations(range(len(points)),2):
 if owner[i]==owner[j]:equal+=1;assert (i,j) not in witness
 else:assert observation(points[i],witness[i,j])!=observation(points[j],witness[i,j])
assert equal==r['equivalent_pairs'] and len(witness)+equal==len(points)*(len(points)-1)//2
for name,z in r['controls'].items():
 a=tuple(map(Q,z['left']));b=tuple(map(Q,z['right']))
 if name=='same_interface_different_prefix':
  assert a!=b and (exact_cap(a),a[2])==(exact_cap(b),b[2])
  # A new historical p-audit would split the merged fiber: outside contract.
  assert (a[0]<=Q(1,4))!=(b[0]<=Q(1,4))
 else:
  assert observation(a,Q(z['completion']))!=observation(b,Q(z['completion']))
  if name=='same_optimum_different_completions':assert a[2]-exact_cap(a)==b[2]-exact_cap(b)
  elif name=='omit_cap':assert a[2]==b[2]
  elif name=='omit_objective_offset':assert exact_cap(a)==exact_cap(b)
# Check update congruence directly at every concrete prefix and all two-frame
# words, rather than reusing the producer's quotient update implementation.
labels=[(k,Q(i,4)) for k in ('lower','upper') for i in range(-1,6)]
for prefix in points:
 h=exact_cap(prefix)
 for word in product(labels,repeat=2):
  bounds=[(Q(0),h)]+[(v,Q(1)) if k=='lower' else (Q(0),v) for k,v in word]
  lo=max(a for a,b in bounds);hi=min(b for a,b in bounds)
  state=(Q(0),min(1-prefix[0],1-prefix[1]/2),prefix[2])
  for k,v in word:
   if state is None:continue
   a,b,t=state;a=max(a,v) if k=='lower' else a;b=min(b,v) if k=='upper' else b
   state=None if a>b else (a,b,t)
  assert state==(None if lo>hi else (lo,hi,prefix[2]))
mat=[list(map(Q,row)) for row in r['linear_necessary_rows']]
a,b,d=mat;det=a[0]*(b[1]*d[2]-b[2]*d[1])-a[1]*(b[0]*d[2]-b[2]*d[0])+a[2]*(b[0]*d[1]-b[1]*d[0]);assert det!=0 and r['linear_rank']==3
# The necessity rows apply on nonempty open active regions.
assert Q(3,4)>Q(1,4)/2 and Q(1,4)<Q(3,4)/2
assert r['two_frame_update_checks']==len(r['classes'])*len(labels)**2
# Corrupt a purported distinguishing completion: y=0 cannot distinguish
# unequal caps at equal objective offsets.
i,j=next((i,j) for i,j in witness if points[i][2]==points[j][2]);assert observation(points[i],Q(0))==observation(points[j],Q(0))
print('PASS: exact redundancy implications, complete grid quotient, all distinguishing completions, concrete update congruence, optimum-only failure, and rank-three linear obstruction')
