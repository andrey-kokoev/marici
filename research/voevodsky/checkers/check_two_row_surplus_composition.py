"""Two labelled redundant bounds: staged and direct Farkas composition with surplus."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
base=(Q(0),Q(1))
def mv(M,v):return tuple(sum(Q(a)*Q(b) for a,b in zip(row,v)) for row in M)
def mm(A,B):return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))) for i in range(len(A)))
def stage(rows):
 bounds=list(base);surplus=[Q(0),Q(0)];labels=['low','base']
 for label,k in rows:
  k=Q(k);assert k>=0 and label not in labels
  bounds.append(Q(1)+k);surplus.append(k);labels.append(label)
 return {'labels':labels,'bounds':bounds,'surplus':surplus,'normals':[-1]+[1]*(len(labels)-1)}
def canon(state):
 return {label:(normal,bound,c) for label,normal,bound,c in zip(state['labels'],state['normals'],state['bounds'],state['surplus'])}
checked=0
for k,l in product((Q(0),Q(1,2),Q(1),Q(2)),repeat=2):
 first=stage([('a',k),('b',l)]);reverse=stage([('b',l),('a',k)])
 direct={'low':(-1,Q(0),Q(0)),'base':(1,Q(1),Q(0)),'a':(1,Q(1)+k,k),'b':(1,Q(1)+l,l)}
 assert canon(first)==canon(reverse)==direct
 # Actual Farkas composition (N M, N c + d), not just a list append.
 M=((1,0),(0,1),(0,1));N=((1,0,0),(0,1,0),(0,0,1),(0,1,0))
 composite=mm(N,M);c1=(Q(0),Q(0),k);c2=(Q(0),Q(0),Q(0),l)
 assert composite==((1,0),(0,1),(0,1),(0,1))
 assert mv(composite,base)==(0,1,1,1)
 assert tuple(a+b for a,b in zip(mv(N,c1),c2))==tuple(first['surplus'])
 assert first['surplus']==[0,0,k,l] and reverse['surplus']==[0,0,l,k]
 assert all(c>=0 for c in first['surplus'])
 checked+=1
# Without labels, reordered proof packets are not equal when margins differ.
a=stage([('a',1),('b',2)]);b=stage([('b',2),('a',1)])
assert a['bounds']!=b['bounds'] and canon(a)==canon(b)
# Plain coarse projection loses both independent margins; one retained scalar
# e.g. sum cannot reconstruct their labelled allocation.
x=stage([('a',0),('b',2)]);y=stage([('a',1),('b',1)])
assert sum(x['surplus'])==sum(y['surplus']) and canon(x)!=canon(y)
assert x['bounds'][:2]==y['bounds'][:2]==list(base)
report={'passed':True,'checked_labelled_pairs':checked,'direct_equals_staged_after_explicit_permutation':True,'raw_order_not_identical':True,'single_total_surplus_not_faithful':True,'retained_grade':'two labelled nonnegative margins k,l','scope':'Two append-only redundant x-bounds on one interval, fixed chart. No general Farkas category equivalence or analytic cone.'}
out=Path(__file__).resolve().parents[1]/'results/two-row-surplus-composition.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
