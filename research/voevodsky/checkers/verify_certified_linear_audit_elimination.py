"""Independent implication identities AND full pair coverage verification."""
from fractions import Fraction as Q
from pathlib import Path
from itertools import product
from copy import deepcopy
import json
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
def canonical(row):
 s=next((abs(v) for v in row[:2] if v),abs(row[2]) if row[2] else Q(1))
 return tuple(v/s for v in row)
def verify(expected,p):
 rows=[tuple(map(Q,r)) for r in expected]
 assert p['original']==[[str(v) for v in r] for r in rows]
 got=set()
 for item in p['summary']:
  r=tuple(map(Q,item['row']));assert len(r)==3 and canonical(r)==r
  w=item['weights'];assert len({i for i,v in w})==len(w)
  assert all(type(i) is int and 0<=i<len(rows) and Q(v)>=0 for i,v in w)
  combined=tuple(sum(Q(v)*rows[i][k] for i,v in w) for k in range(4))
  assert combined==(r[0],r[1],0,r[2]);got.add(r)
 required=set()
 for a,b,c,d in rows:
  if c==0:required.add(canonical((a,b,d)))
 lowers=[r for r in rows if r[2]<0];uppers=[r for r in rows if r[2]>0]
 for a,b,c,d in lowers:
  for e,f,g,h in uppers:
   required.add(canonical((e/g-a/c,f/g-b/c,h/g-d/c)))
 assert got==required and len(got)==len(p['summary'])
 # Rational controls of constructive reverse lift; coverage is the general proof.
 tests=0
 for u,v in product([Q(k,2) for k in range(-2,9)],repeat=2):
  if not all(a*u+b*v<=d for a,b,d in got):continue
  lower=[(d-a*u-b*v)/c for a,b,c,d in lowers]
  upper=[(d-a*u-b*v)/c for a,b,c,d in uppers]
  h=max(lower) if lower else min(upper) if upper else Q(0)
  assert all(a*u+b*v+c*h<=d for a,b,c,d in rows);tests+=1
 return tests
def main():
 if not __debug__:raise RuntimeError('Assertions required')
 expected=[[[1,0,-1,0],[-1,0,1,0],[0,0,-1,0],[0,0,1,1],[1,-1,0,0],[-1,1,0,0]],
 [[i,1,-1,2+i] for i in range(3)]+[[1,j,1,5+j] for j in range(3)]+[[1,0,0,3],[-1,0,0,0],[0,1,0,3],[0,-1,0,0]]]
 packets=json.loads((OUT/'certified-linear-audit-elimination.json').read_text())['packets'];assert len(packets)==2
 checks=sum(verify(e,p) for e,p in zip(expected,packets));rejected=0
 for mode in ('omit','corrupt'):
  p=deepcopy(packets[0])
  if mode=='omit':p['summary'].pop()
  else:p['summary'][0]['weights'][0][1]='-1'
  try:verify(expected[0],p)
  except AssertionError:rejected+=1
  else:raise AssertionError('invalid summary accepted')
 # For the source-relative segment fixture the reverse lift is (U,0,...).
 # Rows imply V=U and 0<=U<=1; every such lift meets the owning atom caps.
 result={'passed':True,'presentations':2,'rational_reverse_lift_controls':checks,'attacks_rejected':rejected,
 'completeness_gate':'Every zero-coefficient row and every negative/positive pair is retained modulo positive scaling and deduplication.',
 'scope':'Exact one-variable linear projection. General source compatibility needs source inequalities or a separate lift proof; only the segment control supplies an owning-source lift here.'}
 (OUT/'certified-linear-audit-elimination-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
