"""Reduce the14 endpoint-link motifs by stripping attached trees and suppressing degree-two paths. Verify five small kernel families."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json
D=Path(__file__).parent;data=json.loads((D/'ramsey_single_link_motifs.json').read_text());rows=[]
for index,motif in enumerate(data['motifs']):
 A=motif['adjacency'];core=set(range(len(A)))
 while True:
  low={v for v in core if sum(A[v]>>w&1 for w in core)<2}
  if not low:break
  core-=low
 N={v:{w for w in core if A[v]>>w&1} for v in core};branches=sorted(v for v in core if len(N[v])!=2);seen=set();paths=[]
 for b in branches:
  for w in N[b]:
   if frozenset((b,w)) in seen:continue
   path=[b,w];seen.add(frozenset((b,w)))
   while path[-1] not in branches:
    z,=N[path[-1]]-{path[-2]};seen.add(frozenset((path[-1],z)));path.append(z)
   paths.append({'ends':[branches.index(b),branches.index(path[-1])],'length':len(path)-1,'vertices':path})
 if not core:family='forest'
 elif not branches:assert len(core)==5;family='pentagon'
 elif len(branches)==2:
  assert all(set(p['ends'])=={0,1} for p in paths);assert len(paths) in (3,4);family=f'{len(paths)} parallel paths'
 else:
  assert len(branches)==4 and {frozenset(p['ends']) for p in paths}=={frozenset(e) for e in combinations(range(4),2)} and len(paths)==6;family='subdivided K4'
 rows.append({'motif':index,'family':family,'core_vertices':sorted(core),'branch_vertices':branches,'paths':paths,'five_sets':len(motif['five_sets']),'occurrences':motif['count']})
result={'families':dict(Counter(r['family'] for r in rows)),'motifs':rows};(D/'ramsey_link_kernel_classification.json').write_text(json.dumps(result,indent=2)+'\n');print(result['families'])
