"""Test whether transported port labels can be an isomorphism-natural invariant of graph+pointwise marked square. Fixed-center matching moves transport ports identically, but endpoints may be square-preservingly isomorphic with a nontrivial port permutation."""
from pathlib import Path
from itertools import combinations
import json
from ramsey_frame_loop_search import C,four,D
from ramsey_regular_two_switch import iso,relation
from ramsey_hall_center_conjecture import independent
Q={0,1,3,11};ports=[2,4,5,6]
def anchored(A):
 R,S,_=relation(A);S=[(s,i if i in Q else -1) for i,s in enumerate(S)];return R,S,tuple(sorted(S))
def changes(A,B):
 return {'removed':[(i,j) for i,j in combinations(range(22),2) if A[i]>>j&1 and not B[i]>>j&1],'added':[(i,j) for i,j in combinations(range(22),2) if B[i]>>j&1 and not A[i]>>j&1]}
start=tuple(C);a=anchored(start);tested=0;found=None
for B in four(start,0):
 for E in four(B,0):
  if E==start:continue
  tested+=1;mapping=iso(start,E,a,anchored(E))
  if mapping is not None and any(mapping[v]!=v for v in ports):
   assert all(mapping[q]==q for q in Q);assert {mapping[v] for v in ports}==set(ports);found={'start':start,'intermediate':B,'endpoint':E,'moves':[changes(start,B),changes(B,E)],'square_preserving_isomorphism':mapping,'transported_ports':ports,'isomorphic_images_of_ports':[mapping[v] for v in ports],'port_permutation':[ports.index(mapping[v]) for v in ports]};break
 if found:break
if found:
 for G in (found['start'],found['intermediate'],found['endpoint']):
  assert all(x.bit_count()==6 for x in G) and all(not(G[i]&G[j]) for i,j in combinations(range(22),2) if G[i]>>j&1) and not independent(G,(1<<22)-1,7)
 pairings=[frozenset((frozenset((0,1)),frozenset((2,3)))),frozenset((frozenset((0,2)),frozenset((1,3)))),frozenset((frozenset((0,3)),frozenset((1,2))))];p=found['port_permutation'];found['pairing_permutation']=[pairings.index(frozenset(frozenset(p[i] for i in pair) for pair in partition)) for partition in pairings]
result={'two_step_paths_tested':tested,'counterexample':found};(D/'ramsey_intrinsic_port_label_test.json').write_text(json.dumps(result,indent=2)+'\n');print('paths tested',tested,'found',found is not None,'port permutation',None if found is None else found['port_permutation'])
