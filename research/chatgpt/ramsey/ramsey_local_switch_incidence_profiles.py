"""Test whether immediate incidence around a switch, with center/hub marked, distinguishes viable C5 templates. Stronger profile includes all pairwise common-neighbor counts in that marked local diagram."""
from pathlib import Path
from itertools import permutations,combinations
from collections import defaultdict
import json
from ramsey_hall_center_conjecture import decode
from ramsey_repair_cyclic_phase import key,transport
D=Path(__file__).parent;A=decode((D/'pauli-realization-catalogues'/'r37_22.g6').read_bytes().splitlines()[190]);system=json.loads((D/'ramsey_block_selection_repair_rules.json').read_text())[-1];moves=system['switches'];p=json.loads((D/'ramsey_repair_cyclic_phase.json').read_text())[-1]['unique_C5_generator'];lookup={key(s):s for s in moves};todo=set(lookup);reps=[]
while todo:
 q=min(todo);o=[]
 while q not in o:o.append(q);q=transport(q,p)
 todo-=set(o);reps.append(lookup[o[0]])
active=set(json.loads((D/'ramsey_phase_compatibility_templates.json').read_text())['active_orbits'])
def profile(s,strong=False,full_traces=False):
 support={v for e in s['removed'] for v in e};removed={frozenset(e) for e in s['removed']};added={frozenset(e) for e in s['added']};candidates=[]
 for order in permutations(support):
  vertices=list(order)+[v for v in (0,1) if v not in support];roles=tuple(1 if v==0 else 2 if v==1 else 0 for v in vertices);matrix=[]
  for i,j in combinations(vertices,2):
   edge=frozenset((i,j));matrix.append((A[i]>>j&1,int(edge in removed),int(edge in added),(A[i]&A[j]).bit_count() if strong else 0))
  traces=tuple(sorted(sum(1<<k for k,v in enumerate(vertices) if A[w]>>v&1) for w in range(22) if w not in vertices)) if full_traces else ()
  candidates.append((roles,tuple(matrix),traces))
 return min(candidates)
results=[]
for strong,full_traces in ((False,False),(True,False),(True,True)):
 groups=defaultdict(list)
 for i,s in enumerate(reps):groups[profile(s,strong,full_traces)].append(i)
 mixed=[ids for ids in groups.values() if any(i in active for i in ids) and any(i not in active for i in ids)];results.append({'include_common_neighbor_counts':strong,'include_full_external_traces':full_traces,'profile_classes':list(groups.values()),'mixed_viability_classes':mixed});print(results[-1])
(D/'ramsey_local_switch_incidence_profiles.json').write_text(json.dumps({'profiles':results,'active_orbits':sorted(active),'representatives':reps},indent=2)+'\n')
