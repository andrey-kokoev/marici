"""Compress the complete regular repair systems into extendability faces. Test whether pairwise co-extendability suffices, distinct from validity of a partial coalition."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json
from ramsey_closed_repair_conjecture import disjoint_collections
D=Path(__file__).parent;data=json.loads((D/'ramsey_block_selection_repair_rules.json').read_text());report=[]
for record in data:
 moves=record['switches'];rules={tuple(r['birth']):r['repairer_masks'] for r in record['rules']};models=[]
 for size in range(1,6):
  for selected in disjoint_collections(moves,size):
   mask=sum(1<<i for i in selected)
   if all(all(head&mask for head in rules.get(birth,())) for arity in (1,2) for birth in combinations(selected,arity)):models.append(frozenset(selected))
 faces={frozenset()}
 for model in models:
  for size in range(1,len(model)+1):faces.update(frozenset(s) for s in combinations(model,size))
 vertices=sorted(set().union(*models)) if models else [];edges={tuple(pair) for pair in combinations(vertices,2) if frozenset(pair) in faces};adj={i:{j for j in vertices if tuple(sorted((i,j))) in edges} for i in vertices};missing=[]
 def search(clique,remaining):
  F=frozenset(clique)
  if F not in faces:
   if all(F-{v} in faces for v in F):missing.append(sorted(F))
   return
  for k,v in enumerate(remaining):search(clique+[v],[w for w in remaining[k+1:] if w in adj[v]])
 search([],vertices)
 incompatible=[(i,j) for i,j in combinations(vertices,2) if (i,j) not in edges];disjoint_incompatible=[(i,j) for i,j in incompatible if not moves[i]['support']&moves[j]['support']];facets=[sorted(m) for m in models if not any(m<n for n in models)];row={'source':record['source'],'candidate_switches':len(moves),'participating_switches':vertices,'excluded_singletons':len(moves)-len(vertices),'valid_models':[sorted(m) for m in models],'maximal_completions':facets,'extendability_faces_by_size':dict(sorted(Counter(map(len,faces)).items())),'pair_incompatibilities':len(incompatible),'disjoint_pair_incompatibilities':len(disjoint_incompatible),'minimal_higher_obstructions':missing,'pairwise_extendability_sufficient':not missing};report.append(row);print({k:v for k,v in row.items() if k not in ('participating_switches','valid_models','maximal_completions')})
(D/'ramsey_completion_compatibility_complex.json').write_text(json.dumps(report,indent=2)+'\n')
