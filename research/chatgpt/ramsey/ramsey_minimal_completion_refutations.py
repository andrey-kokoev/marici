"""Check whether all minimal extendability obstructions have direct unit-propagation certificates from lower-order repair rules."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json
D=Path(__file__).parent;systems=json.loads((D/'ramsey_block_selection_repair_rules.json').read_text());complexes={r['source']:r for r in json.loads((D/'ramsey_completion_compatibility_complex.json').read_text())};results=[]
for system in systems:
 moves=system['switches'];c=complexes[system['source']];participating=set(c['participating_switches']);facets=[set(f) for f in c['maximal_completions']];conflict=[sum(1<<j for j,t in enumerate(moves) if i!=j and s['support']&t['support']) for i,s in enumerate(moves)];clauses=[(head,sum(1<<i for i in r['birth'])) for r in system['rules'] for head in r['repairer_masks']]
 def refutes(selected,forbidden=()):
  T=sum(1<<i for i in selected);F=sum(1<<i for i in forbidden)
  while True:
   old=(T,F);mask=T
   while mask:
    b=mask&-mask;mask^=b;F|=conflict[b.bit_length()-1]
   if T&F:return True
   for p,n in clauses:
    if p&T or n&F:continue
    left=(p|n)&~(T|F)
    if not left:return True
    if not left&(left-1):
     if p&left:T|=left
     else:F|=left
   if old==(T,F):return False
 stats=Counter();unproved=[]
 for i in range(len(moves)):
  if i in participating:continue
  stats['excluded_singletons']+=1
  if refutes((i,)):stats['singletons_unit_refuted']+=1
  else:unproved.append([i])
 for i,j in combinations(sorted(participating),2):
  if moves[i]['support']&moves[j]['support'] or any({i,j}<=f for f in facets):continue
  stats['disjoint_incompatible_pairs']+=1
  if refutes((i,j)):stats['pairs_unit_refuted']+=1
  else:unproved.append([i,j])
 splits=[]
 for selected in unproved:
  witness=next((j for j in range(len(moves)) if j not in selected and refutes(tuple(selected)+(j,)) and refutes(selected,(j,))),None)
  splits.append({'assumed':selected,'split_variable':witness})
 row={'source':system['source'],'stats':dict(stats),'unproved_by_units':unproved,'one_split_certificates':splits};results.append(row);print(row)
(D/'ramsey_minimal_completion_refutations.json').write_text(json.dumps(results,indent=2)+'\n')
