"""Generate Hall191 valid coalitions from four cyclic recipes, not a model list. Verify each output and distinguish recipes from mere extendability cliques."""
from pathlib import Path
from itertools import combinations
import json
from ramsey_hall_center_conjecture import decode,independent
from ramsey_mutual_repair_conjecture import apply
D=Path(__file__).parent;templates=json.loads((D/'ramsey_phase_compatibility_templates.json').read_text());system=json.loads((D/'ramsey_block_selection_repair_rules.json').read_text())[-1];moves=system['switches'];orbits={t['orbit']:t['candidate_indices_in_phase_order'] for t in templates['templates']};A=decode((D/'pauli-realization-catalogues'/'r37_22.g6').read_bytes().splitlines()[190]);recipes=[]
for i in range(5):
 recipes.extend([('pair',[orbits[6][i],orbits[14][(i+2)%5]]),('extended_triangle',[orbits[5][i],orbits[6][(i+4)%5],orbits[14][(i+1)%5]]),('irreducible_triangle',[orbits[12][i],orbits[13][(i+1)%5],orbits[13][(i+2)%5]])])
recipes.append(('full_orbit',orbits[11]));assert len({frozenset(ids) for _,ids in recipes})==16
outputs=[]
for kind,ids in recipes:
 assert all(not moves[i]['support']&moves[j]['support'] for i,j in combinations(ids,2));B=A[:]
 for i in ids:B=apply(B,moves[i]['removed'],moves[i]['added'])
 assert all(n.bit_count()==6 for n in B) and all(not(B[i]&B[j]) for i,j in combinations(range(22),2) if B[i]>>j&1) and not independent(B,(1<<22)-1,7);outputs.append({'kind':kind,'switches':ids,'output_adjacency':B})
(D/'ramsey_phase_coalition_constructor.json').write_text(json.dumps(outputs,indent=2)+'\n');print('constructed and verified',len(outputs),'nonempty coalitions from four cyclic recipes')
