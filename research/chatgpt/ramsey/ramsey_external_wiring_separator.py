"""Locate a small external-edge obstruction to the apparent symmetry exchanging viable/dead switches on the same support. Outside classes are defined solely by their neighborhoods in the marked core."""
from pathlib import Path
from itertools import combinations_with_replacement,combinations
from collections import defaultdict
import json
from ramsey_hall_center_conjecture import decode
D=Path(__file__).parent;A=decode((D/'pauli-realization-catalogues'/'r37_22.g6').read_bytes().splitlines()[190]);core={0,1,2,12,13,16};swap={v:v for v in core};swap[12]=13;swap[13]=12;classes=defaultdict(list)
for v in range(22):
 if v not in core:classes[tuple(u for u in sorted(core) if A[v]>>u&1)].append(v)
def image(signature):return tuple(sorted(swap[u] for u in signature))
assert all(len(classes[s])==len(classes[image(s)]) for s in classes)
def edges(s,t):
 return [(u,v) for u in classes[s] for v in classes[t] if (u<v or s!=t) and A[u]>>v&1]
violations=[]
for s,t in combinations_with_replacement(sorted(classes),2):
 e=edges(s,t);f=edges(image(s),image(t))
 if len(e)!=len(f):violations.append({'source_signatures':[s,t],'source_classes':[classes[s],classes[t]],'source_edges':e,'image_signatures':[image(s),image(t)],'image_classes':[classes[image(s)],classes[image(t)]],'image_edges':f})
violations.sort(key=lambda r:sum(len(c) for c in r['source_classes']+r['image_classes']))
# Identify the third/fourth chart blocks involved using the known C5 generator.
p=json.loads((D/'ramsey_repair_cyclic_phase.json').read_text())[-1]['unique_C5_generator'];result={'core':sorted(core),'core_swap':swap,'outside_signature_classes':[{'signature':s,'vertices':vs} for s,vs in sorted(classes.items())],'violations':violations};(D/'ramsey_external_wiring_separator.json').write_text(json.dumps(result,indent=2)+'\n');print('class sizes',[len(v) for v in classes.values()]);print('violations',len(violations));print('smallest',violations[:2])
