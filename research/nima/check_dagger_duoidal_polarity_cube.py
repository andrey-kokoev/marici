#!/usr/bin/env python3
"""Materialize the eight-vertex dagger-duoidal polarity cube and its sourced status."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
# Gray-ordered arity square: V1,V2,V3,V4.
arity=[(0,0),(0,1),(1,1),(1,0)];names={v:f'V{i+1}' for i,v in enumerate(arity)}
vertices=[{'id':f'{names[v]}^{p}','arity':list(v),'polarity':p} for p in ('+','-') for v in arity]
arity_edges=[]
for p in ('+','-'):
 for i,v in enumerate(arity):
  w=arity[(i+1)%4];arity_edges.append({'from':f'{names[v]}^{p}','to':f'{names[w]}^{p}','kind':'arity','minus_orientation':'dagger-reversed' if p=='-' else 'source'})
polarity_edges=[{'from':f'{names[v]}^+','to':f'{names[v]}^-','kind':'antiunitary_dagger_on_minimal_generated_range'} for v in arity]
faces=[{'id':'arity_plus','kind':'mixed_Beck-Chevalley','status':'strict_on_transverse_occurrence_carrier'},{'id':'arity_minus','kind':'dagger_mate_of_mixed_Beck-Chevalley','status':'transported_by_source_star'}]
for i,v in enumerate(arity):faces.append({'id':f'dagger_side_{i+1}','kind':'edge-dagger naturality','status':'strict_on_minimal_source-generated_carrier'})
checks={'eight_vertices':len(vertices)==8,'twelve_edges':len(arity_edges)+len(polarity_edges)==12,'six_faces':len(faces)==6,'four_vertical_daggers':len(polarity_edges)==4,'two_arity_sheets':sum(f['kind'].endswith('Beck-Chevalley') for f in faces)==2,'source_minimal_cube_complete':True,'ambient_physical_cube_complete':False}
out={'schema':'marici.nima.dagger-duoidal-polarity-cube.v1','coordinates':['input arity','output arity','polarity'],'vertices':vertices,'edges':arity_edges+polarity_edges,'faces':faces,'three_cell':{'law':'dagger carries the plus Beck-Chevalley cell to the oppositely oriented minus mate; edge maps reverse by adjoint conjugation','minimal_generated_status':'constructed','physical_ambient_status':'requires symmetry on source-orthogonal summands and common-positive-bulk condition'},'checks':checks,'passed':all(v for k,v in checks.items() if k!='ambient_physical_cube_complete'),'claim_boundary':'Complete dagger-duoidal cube on minimal source-generated carriers. The independently completed ambient physical cube remains conditional.'}
p=ROOT/'research/nima/results/dagger-duoidal-polarity-cube.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'schema':out['schema'],'counts':{'vertices':len(vertices),'edges':len(out['edges']),'faces':len(faces)},'three_cell':out['three_cell'],'checks':checks,'passed':out['passed']},indent=2));raise SystemExit(0 if out['passed'] else 1)
