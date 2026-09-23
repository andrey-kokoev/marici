"""Fail-closed aggregation of six independent local candidate-wall calculations."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];N=ROOT/'research/nima/results'
def load(name):return json.loads((N/name).read_text())
raw=[('seven-point-repair-shared-wall.json','seven-point-repair-wall-residue.json',(0,1)),
     ('seven-point-one-two-wall.json',None,(1,2)),
     ('seven-point-third-repair-wall.json','seven-point-third-wall-residue.json',(2,3)),
     ('seven-point-three-four-wall.json',None,(3,4)),
     ('seven-point-four-five-wall.json',None,(4,5)),
     ('seven-point-second-repair-wall.json',None,(0,5))]
rows=[]
for orientation,residue,edge in raw:
 x=load(orientation);y=load(residue) if residue else x
 assert x['inward_side']=='OPPOSITE' and y['source_residue_ratio']=='1'
 assert x.get('face_target_rank',x.get('shared_image_tangent_rank',x.get('face_image_tangent_rank')))==7
 assert tuple(sorted(x.get('pair',x.get('history_pair'))))==edge
 ratio=x['inward_ratio'] if 'inward_ratio' in x else x['inward_normal_ratio']
 from fractions import Fraction as Q
 assert Q(ratio)<0
 rows.append({'cells':list(edge),'target_inward_ratio':ratio,'source_residue_ratio':'1',
              'orientation_report':orientation,'residue_report':residue or orientation})
assert {tuple(x['cells']) for x in rows}=={(0,1),(1,2),(2,3),(3,4),(4,5),(0,5)}
report={'schema':'marici.nima.seven-point-local-six-cycle.v1','passed':True,'edges':rows,
 'scope':'All six proposed adjacent walls have a rank-seven common image at one rational positive point, opposite local inward sides, and symbolic source cyclic-form residue ratio one. Not a global triangulation, physical history-form identification, or arbitrary-n compiler.'}
(N/'seven-point-local-six-cycle.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
