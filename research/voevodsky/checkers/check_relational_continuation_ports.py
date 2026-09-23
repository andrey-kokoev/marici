"""Finite port/congruence controls on owner-produced coupled graph; not source authentication."""
import json
from collections import defaultdict
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
states=json.loads((ROOT/'research/nima/results/actual-source-evidence-coupling.json').read_text())['states']
assert len(states)==638
labels={tuple(label) for s in states for label,_ in s['transitions']}
assert {('acquire',),('deliver',),('issue',0),('issue',1)} <= labels
assert any(label[0]=='source' for label in labels)
by_enriched=defaultdict(list);by_current=defaultdict(list)
for s in states:
 edges={tuple(label):states[j]['enriched_class'] for label,j in s['transitions']}
 assert len(edges)==len(s['transitions'])
 by_enriched[s['enriched_class']].append(edges)
 by_current[s['current_class']].append((s,edges))
assert all(all(e==group[0] for e in group) for group in by_enriched.values())
collisions=[]
for group in by_current.values():
 for i,(s,e) in enumerate(group):
  for t,f in group[i+1:]:
   if any(label[0]=='issue' for label in set(e)^set(f)):
    collisions.append({'current_class':s['current_class'],'left_issued':s['issued'],'right_issued':t['issued'],'different_labels':sorted(map(str,set(e)^set(f)))})
    break
  if collisions:break
 if collisions:break
assert collisions and any('issue' in x for x in collisions[0]['different_labels'])
report={'schema':'marici.voevodsky.relational-ports.v1','passed':True,'state_count':len(states),'label_count':len(labels),'enriched_class_count':len(by_enriched),'source_only_rejection_hostile':collisions[0], 'scope':'Finite transitions of owner-produced JSON; does not independently verify owner guards, source truth or physical acquisition.'}
out=ROOT/'research/voevodsky/results/relational-continuation-ports.json'
out.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report))
