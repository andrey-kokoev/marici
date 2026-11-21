"""Construct the Hall191 co-extendability graph by logical propagation, NOT by looking up completed coalitions. Express the result as six cyclic switch templates and allowed relative phases."""
from pathlib import Path
from itertools import combinations
from collections import defaultdict
import json
from ramsey_repair_cyclic_phase import key,transport
D=Path(__file__).parent;system=json.loads((D/'ramsey_block_selection_repair_rules.json').read_text())[-1];assert system['source']==191;moves=system['switches'];clauses=[(head,sum(1<<i for i in r['birth'])) for r in system['rules'] for head in r['repairer_masks']];conflicts=[sum(1<<j for j,t in enumerate(moves) if i!=j and s['support']&t['support']) for i,s in enumerate(moves)]
def refutes(selected):
 T=sum(1<<i for i in selected);F=0
 while True:
  old=(T,F);m=T
  while m:
   b=m&-m;m^=b;F|=conflicts[b.bit_length()-1]
  if T&F:return True
  for p,n in clauses:
   if p&T or n&F:continue
   left=(p|n)&~(T|F)
   if not left:return True
   if not left&(left-1):
    if p&left:T|=left
    else:F|=left
  if old==(T,F):return False
vertices=[i for i in range(len(moves)) if not refutes((i,))];edges={tuple(sorted((i,j))) for i,j in combinations(vertices,2) if not moves[i]['support']&moves[j]['support'] and not refutes((i,j))};assert len(vertices)==30 and len(edges)==40
p=json.loads((D/'ramsey_repair_cyclic_phase.json').read_text())[-1]['unique_C5_generator'];lookup={key(s):i for i,s in enumerate(moves)};todo=set(lookup);orbits=[];coordinates={}
while todo:
 q=min(todo);o=[]
 while q not in o:o.append(q);q=transport(q,p)
 orbit=[lookup[k] for k in o];todo-=set(o)
 for phase,i in enumerate(orbit):coordinates[i]=(len(orbits),phase)
 orbits.append(orbit)
active=[j for j,o in enumerate(orbits) if set(o)<=set(vertices)];assert sum(len(orbits[j]) for j in active)==len(vertices)
phase_edges=defaultdict(set)
for a,b in edges:
 i,x=coordinates[a];j,y=coordinates[b]
 if i>j:i,j,x,y=j,i,y,x
 phase_edges[i,j].add((y-x)%5)
 if i==j:phase_edges[i,j].add((x-y)%5)
# Reconstruct all40 edges from phase templates alone.
reconstructed=set()
for (i,j),deltas in phase_edges.items():
 for x in range(5):
  for delta in deltas:
   a=orbits[i][x];b=orbits[j][(x+delta)%5]
   if a!=b:reconstructed.add(tuple(sorted((a,b))))
assert reconstructed==edges
result={'active_orbits':active,'templates':[{'orbit':j,'representative_removed':moves[orbits[j][0]]['removed'],'representative_added':moves[orbits[j][0]]['added'],'candidate_indices_in_phase_order':orbits[j]} for j in active],'phase_edges':[{'orbits':[i,j],'allowed_phase_differences':sorted(ds)} for (i,j),ds in sorted(phase_edges.items())],'vertices':vertices,'edges':sorted(edges),'construction':'single/pair unit propagation of necessary repair rules; no model list used'};(D/'ramsey_phase_compatibility_templates.json').write_text(json.dumps(result,indent=2)+'\n');print('active orbits',active);print('phase edges',result['phase_edges']);print('templates',result['templates'])
