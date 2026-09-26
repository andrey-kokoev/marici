"""Source-character obstruction and the limited effect of an orientation twist."""
from pathlib import Path
import ast,hashlib,json
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
physical=ROOT/'research/voevodsky/check_physical_derived_pullback_after_transform.py'
tate=ROOT/'research/nima/checkers/check_rs2_canonical_c3_tate_bridge.py'
paths=[Path(__file__),HERE/'readout-orientation-obstruction.md',physical,tate,ROOT/'research/nima/polarity-orientation-twist.md']
def hashes():return {p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
def constants(nodes,names):
 result={}
 for node in nodes:
  if isinstance(node,ast.Assign) and len(node.targets)==1 and isinstance(node.targets[0],ast.Name) and node.targets[0].id in names:
   result[node.targets[0].id]=ast.literal_eval(node.value)
 return result
before=hashes()
main=next(n for n in ast.parse(physical.read_text(encoding='utf-8')).body if isinstance(n,ast.FunctionDef) and n.name=='main')
p=constants(main.body,{'road_reflection','polarity_reflection'})
q=constants(ast.parse(tate.read_text(encoding='utf-8')).body,{'reflection_scalar','rotation_scalar'})
source_sign=p['road_reflection']*p['polarity_reflection'];target_sign=q['reflection_scalar']
assert source_sign==1 and target_sign==2 and q['rotation_scalar']==1
maps=lambda sign:[a for a in range(3) if (a*sign-target_sign*a)%3==0]
assert maps(source_sign)==[0]
assert maps(-source_sign)==[0,1,2]
assert [twist for twist in (-1,1) if len(maps(source_sign*twist))>1]==[-1]
for n in range(-12,13):
 for orientation in (-1,1):
  reading=(n*orientation)%3
  reflected=(n*(-orientation))%3
  assert reflected==(-reading)%3
  assert (-3*n*orientation)%3==0
for rotation_power in range(3):
 # Both rotations are trivial on the two one-dimensional quotients.
 assert (q['rotation_scalar']**rotation_power*target_sign)%3==2
assert before==hashes()
report={'passed':True,'source_unchanged':True,'source_sha256':before,'physical_loaded_reflection':1,'tate_reflection_mod3':2,'untwisted_equivariant_map_values':[0],'odd_twisted_equivariant_map_values':[0,1,2],'nonzero_twisted_choices':2,'character_correcting_twist':-1,'orientation_twist_repairs_scalar_trace_mod3_loss':False,'scope':'Actual source character data under declared D3 generator comparison. Character repair is not a source-authorized geometric bridge or physical parity identification.'}
(HERE/'readout-orientation-obstruction.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
