"""Extract a backward-trimmed unit-refutation DAG for locally indistinguishable but unextendable orbit10."""
from pathlib import Path
import json
D=Path(__file__).parent;system=json.loads((D/'ramsey_block_selection_repair_rules.json').read_text())[-1];moves=system['switches'];s=json.loads((D/'ramsey_local_switch_incidence_profiles.json').read_text())['representatives'][10];start=next(i for i,m in enumerate(moves) if m['removed']==s['removed'] and m['added']==s['added']);clauses=[([(j,True) for j in range(len(moves)) if head>>j&1]+[(j,False) for j in r['birth']],{'birth':r['birth'],'repairer_mask':head}) for r in system['rules'] for head in r['repairer_masks']];assign={start:True};reasons={(start,True):{'kind':'assumption','dependencies':[]}};conflict=None
while conflict is None:
 changed=False
 for i,value in list(assign.items()):
  if not value:continue
  for j,m in enumerate(moves):
   if j==i or not moves[i]['support']&m['support']:continue
   if assign.get(j) is True:conflict={'kind':'support_conflict','dependencies':[(i,True),(j,True)]};break
   if j not in assign:assign[j]=False;reasons[j,False]={'kind':'overlapping_support','dependencies':[(i,True)]};changed=True
  if conflict:break
 if conflict:break
 for clause,rule in clauses:
  if any(assign.get(i)==b for i,b in clause if i in assign):continue
  free=[(i,b) for i,b in clause if i not in assign];deps=[(i,not b) for i,b in clause if i in assign]
  if not free:conflict={'kind':'unsatisfied_repair_rule','rule':rule,'dependencies':deps};break
  if len(free)==1:
   i,b=free[0];assign[i]=b;reasons[i,b]={'kind':'repair_implication','rule':rule,'dependencies':deps};changed=True
 assert changed or conflict
needed=set()
def visit(node):
 if node in needed:return
 needed.add(node)
 for dep in reasons[node]['dependencies']:visit(tuple(dep))
for dep in conflict['dependencies']:visit(tuple(dep))
proof=[{'candidate':i,'selected':b,**reasons[i,b]} for i,b in reasons if (i,b) in needed];result={'assumed_candidate':start,'assumed_switch':moves[start],'proof':proof,'contradiction':conflict};(D/'ramsey_dead_template_refutation.json').write_text(json.dumps(result,indent=2)+'\n');print('assumed',start,'proof nodes',len(proof),'selected switches',[r['candidate'] for r in proof if r['selected']],'final',conflict)
