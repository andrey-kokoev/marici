"""Explain viable/dead local twins by immediate repair feasibility: can their own defects be hit by any mutually disjoint candidate repairers, before checking those repairers' defects?"""
from pathlib import Path
from itertools import combinations
import json
D=Path(__file__).parent;system=json.loads((D/'ramsey_block_selection_repair_rules.json').read_text())[-1];moves=system['switches'];reps=json.loads((D/'ramsey_local_switch_incidence_profiles.json').read_text())['representatives'];results=[]
for orbit in (10,12):
 s=reps[orbit];bad=s['bad'];heads=[]
 for I in bad:heads.append([j for j,t in enumerate(moves) if not s['support']&t['support'] and any(I>>u&1 and I>>v&1 for u,v in t['added'])])
 def cover(required,used=s['support'],selected=()):
  if not required:return selected
  options={k:[j for j in heads[k] if not moves[j]['support']&used] for k in required};k=min(options,key=lambda k:len(options[k]))
  for j in options[k]:
   remaining=[i for i in required if j not in heads[i]];ans=cover(remaining,used|moves[j]['support'],selected+(j,))
   if ans is not None:return ans
  return None
 full=cover(list(range(len(bad))));minimal=None
 if full is None:
  for size in range(1,len(bad)+1):
   minimal=next((ids for ids in combinations(range(len(bad)),size) if cover(list(ids)) is None),None)
   if minimal is not None:break
 row={'orbit':orbit,'defect_count':len(bad),'repairer_counts':list(map(len,heads)),'immediate_disjoint_cover':full,'minimal_unrepairable_subset':minimal,'defects':[{'vertices':[v for v in range(22) if I>>v&1],'repairers':heads[k]} for k,I in enumerate(bad)]};results.append(row);print(row)
(D/'ramsey_local_symmetry_repair_obstruction.json').write_text(json.dumps(results,indent=2)+'\n')
