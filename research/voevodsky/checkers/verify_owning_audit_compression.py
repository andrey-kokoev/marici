"""Independent owning dictionary, projection coverage and removal certificates."""
from fractions import Fraction as Q
from pathlib import Path
import json
from verify_certified_linear_audit_elimination import verify
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
def main():
 if not __debug__:raise RuntimeError('Assertions required')
 packets=json.loads((OUT/'owning-audit-compression.json').read_text())['packets'];assert len(packets)==3
 total=0
 for m,p in zip((3,4,8),packets):
  assert p['m']==m
  slopes=[Q(1,128**j) for j in range(m)];caps=[100+2*j for j in range(m)]
  expected=[(Q(0),Q(0),Q(-1),Q(0)),(Q(0),Q(0),Q(1),Q(100))]
  for j in range(1,m):
   for sign in (-1,1):
    a,b=-sign*slopes[j],Q(sign)
    expected.append((a,b,-a-b,sum(caps[k]*max(Q(0),a+b*slopes[k]) for k in range(1,m))))
  for sign in (-1,1):expected.append((Q(sign),Q(0),Q(-sign),Q(sum(caps[1:]) if sign==1 else 0)))
  expected += [(Q(1),Q(0),Q(-1),Q(0)),(Q(-1),Q(0),Q(1),Q(0)),(Q(0),Q(0),Q(1),Q(1))]
  verify(expected,p)
  rows=[tuple(map(Q,r['row'])) for r in p['summary']];active=set(range(len(rows)))
  for step in p['removals']:
   i=step['removed'];assert i in active;w=step['weights']
   assert len({j for j,v in w})==len(w)
   assert all(j in active and j!=i and Q(v)>=0 for j,v in w)
   combined=[sum(Q(v)*rows[j][k] for j,v in w) for k in range(3)]
   assert tuple(combined[:2])==rows[i][:2] and combined[2]<=rows[i][2]
   active.remove(i);total+=1
  assert sorted(active)==p['retained_indices']
  # Source-relative semantic identification: U=h and source nonnegativity
  # force all free atoms zero, hence V=U and 0<=U<=1. Conversely (U,0,...)
  # lifts every point of that segment. Confirm returned summary includes
  # precisely that segment by independent planar vertices and boundedness.
  # Bounds on U,V are inherited from verified equivalence to bounded source.
  from itertools import combinations
  vertices=set()
  for i,j in combinations(active,2):
   a,b,c=rows[i];d,e,f=rows[j];det=a*e-b*d
   if det:
    u,v=(c*e-b*f)/det,(a*f-c*d)/det
    if all(rows[k][0]*u+rows[k][1]*v<=rows[k][2] for k in active):vertices.add((u,v))
  assert vertices=={(Q(0),Q(0)),(Q(1),Q(1))}
 result={'passed':True,'owning_cases':3,'certified_removals':total,
 'source_lift':'(U,0,...,0) for 0<=U<=1, V=U',
 'scope':'Exact projection plus sequential redundancy certificates; migration proof retained separately from compact public summary.'}
 (OUT/'owning-audit-compression-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
