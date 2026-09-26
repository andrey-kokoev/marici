"""Cyclic re-anchoring of the complete source sum, retaining physical chi labels."""
from nine_point_source_r import Kinematics
from pathlib import Path
import sympy as s
import json,random
root=Path(__file__).resolve().parents[1]
histories=json.loads((root/'results/nine-point-source-history-contract.json').read_text())['records']
components=[((3,5),)*4,((2,5),)*4,((1,5),)*4,((1,3),(2,5),(4,7),(6,9)),((1,9),(2,8),(3,7),(4,6))]
rng=random.Random(904)
fixtures=[{'parameters':list(ts),'rows':[(1,t,t*t,t**3) for t in ts]} for ts in (range(1,10),(1,2,4,7,11,16,22,29,37))]
fixtures.append({'parameters':None,'rows':[tuple(rng.randint(-30,30) for _ in range(4)) for i in range(9)]})
results=[];comparisons=0
for fixture in fixtures:
 parameters=fixture['parameters'];physical=fixture['rows'];anchor_values=[]
 for shift in range(9):
  labels=list(range(1,10));labels=labels[shift:]+labels[:shift]
  local={physical_label:i+1 for i,physical_label in enumerate(labels)}
  kin=Kinematics([physical[i-1] for i in labels]);sums=[s.S.Zero]*len(components)
  for h in histories:
   a1,b1=h['outer_pair'];a,b=h['inner_pair'];A,p=kin.ordinary(a1,b1);B,q=kin.inner(a1,b1,a,b,h['branch'])
   for index,pairs in enumerate(components):
    # Do not sort the relabelled pair: preserve the physical Grassmann order.
    value=p*q
    for i,j in pairs:
     u,v=local[i],local[j];value*=A[u]*B[v]-A[v]*B[u]
    sums[index]+=value
  anchor_values.append([s.factor(v) for v in sums])
 baseline=anchor_values[0]
 for values in anchor_values[1:]:
  for a,b in zip(values,baseline):assert s.factor(a-b)==0;comparisons+=1
 results.append({'parameters':parameters,'twistor_rows':physical,'cyclic_anchors':9,'components':[{'physical_flavor_pairs':pairs,'coefficient':str(value)} for pairs,value in zip(components,baseline)]})
report={'passed':True,'history_products_evaluated':len(fixtures)*9*50,'nonbaseline_component_comparisons':comparisons,'witnesses':results,'scope':'Exact cyclic invariance for five physical Grassmann components at three rational inputs (two moment-curve, one seeded general configuration); same source formula re-anchored, not independent recursion or universal identity proof.'}
(root/'results/nine-point-cyclic-tree.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
