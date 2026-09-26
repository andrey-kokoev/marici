"""Check the explicit successor dependency plan, not scientific adequacy."""
from pathlib import Path
import hashlib,json
HERE=Path(__file__).resolve().parent
paths=[Path(__file__),HERE/'project-readout-dependency-plan.json',HERE/'project-readout-dependency-correction.md']
def hashes():return {p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
before=hashes();plan=json.loads(paths[1].read_text(encoding='utf-8'))
nodes={n['stem']+':v'+str(n['version']):n for n in plan['nodes']}
assert len(nodes)==len(plan['nodes'])==10
assert all(n['version']==n['previous_version']+1 for n in nodes.values())
selected=[name for name,n in nodes.items() if n['state']=='selected']
assert selected==['completion-stable-observability:v2']
assert all(nodes[selected[0]]['score']>n['score'] for name,n in nodes.items() if name!=selected[0])
edges=plan['dependencies'];assert len(edges)==len(set(map(tuple,edges)))==4
assert all(a in nodes and b in nodes for a,b in edges)
def ancestors(node,active=frozenset()):
 assert node not in active,'dependency cycle'
 found=set()
 for a,b in edges:
  if a==node:found.add(b);found.update(ancestors(b,active|{node}))
 return found
for node in nodes:ancestors(node)
required=ancestors(selected[0])
assert required=={'typed-observation-pairing:v2','source-law-contract:v2'}
assert required.isdisjoint(plan['not_universal_prerequisites'])
assert before==hashes()
report={'passed':True,'source_unchanged':True,'source_sha256':before,'successor_nodes':len(nodes),'dependency_edges':len(edges),'selected':selected[0],'selected_dependencies':sorted(required),'historical_edges_deleted':False,'owner_trees_mutated':False,'scope':'Acyclic priority/dependency plan only; actual admission is separately reported by the graph surface.'}
(HERE/'project-readout-dependency-check.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
