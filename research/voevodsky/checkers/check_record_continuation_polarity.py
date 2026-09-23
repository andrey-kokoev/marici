"""Finite continuation-polarity witness; no operator-algebra commutant asserted."""
from itertools import combinations
from pathlib import Path
import json
H=('direct-zero','staged-one')
# Both valid proof histories have the same source/target relation and public
# answer; proof replay remains path-bound. No actual-history selector inferred.
controls={'public_inclusion':{'direct-zero':True,'staged-one':True},
          'public_target_residual':{'direct-zero':'5/2','staged-one':'5/2'},
          'replay_bound_proof':{'direct-zero':'(2,3);c=0','staged-one':'(1,2);c=1'}}
pairs={(x,y) for x in H for y in H}
def compatible(E):return frozenset(name for name,f in controls.items() if all(f[x]==f[y] for x,y in E))
def indistinguishable(C):return frozenset((x,y) for x,y in pairs if all(controls[name][x]==controls[name][y] for name in C))
all_E=[set(k) for n in range(len(pairs)+1) for k in combinations(sorted(pairs),n)]
all_C=[set(k) for n in range(len(controls)+1) for k in combinations(sorted(controls),n)]
checks=0
for E in all_E:
 for C in all_C:
  assert (E<=set(indistinguishable(C)))==(C<=set(compatible(E)))
  checks+=1
coarse=frozenset(pairs);fine=frozenset((x,x) for x in H)
assert compatible(coarse)==frozenset({'public_inclusion','public_target_residual'})
assert compatible(fine)==frozenset(controls)
assert indistinguishable({'public_inclusion','public_target_residual'})==coarse
assert indistinguishable(controls)==fine
# Proof DAG: compare two distinct proof tips only with source-rooted support.
roots={'source-interval':'primitive','source-target-row':'primitive'}
deps={'direct-proof':('source-interval','source-target-row'),
      'staged-proof':('source-interval','source-target-row'),
      'comparison':('direct-proof','staged-proof')}
def rooted(node,links,seen=()):
 if node in seen:return False
 if node in roots:return True
 return node in links and bool(links[node]) and all(rooted(x,links,seen+(node,)) for x in links[node])
assert rooted('comparison',deps)
assert not rooted('comparison',{'comparison':('direct-proof',),'direct-proof':('comparison',)})
assert not rooted('comparison',{'comparison':('unsupported-proof',)})
report={'passed':True,'histories':list(H),'galois_equivalences_checked':checks,'public_only_equivalence':'one two-history class','proof_replay_equivalence':'two singleton classes','comparison_source_rooted':True,'refusals':['cyclic-support','unsupported-proof'],'scope':'Finite output-factorization polarity and proof-support DAG; no literal double commutant, proof-path equivalence, source authentication or analytic role map.'}
out=Path(__file__).resolve().parents[1]/'results/record-continuation-polarity.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
