"""Tagged candidate records preserve exact paths, but do not equate them."""
from pathlib import Path
import json
roots=('x-low','x-high','y-low','y-high')
short=((),());long=((0,),(),(1,))
packet=('1','3','1','3');leaves=('a','b','c','d')
def answer(control,root_ids,route):
 if tuple(root_ids)!=roots:raise PermissionError('MISSING_PRIMITIVE_ROOT')
 if route not in (short,long):raise ValueError('UNREGISTERED_ASSOCIATOR_PATH')
 if control=='public_packet':return packet
 if control=='leaf_tags':return leaves
 if control=='replay_exact_rotations':return route
 if control=='declare_equal_histories':raise PermissionError('NO_PENTAGON_HIGHER_FILLER')
 raise ValueError('UNDECLARED_CONTROL')
assert answer('public_packet',roots,short)==answer('public_packet',roots,long)
assert answer('leaf_tags',roots,short)==answer('leaf_tags',roots,long)
assert answer('replay_exact_rotations',roots,short)!=answer('replay_exact_rotations',roots,long)
try:answer('declare_equal_histories',roots,short)
except PermissionError as e:assert str(e)=='NO_PENTAGON_HIGHER_FILLER'
else:raise AssertionError('unsupported history equality')
try:answer('public_packet',roots[:-1],short)
except PermissionError:pass
else:raise AssertionError('missing source root')
report={'passed':True,'public_packet_equal':True,'ordered_leaf_tags_equal':True,'exact_rotation_replay_distinguishes_paths':True,'history_equality_refused_without_higher_filler':True,'missing_root_refused':True,'scope':'Bounded four-leaf tagged Farkas presentation. A record/control contract, not a global proof higher category or semantic authority to identify historical events.'}
out=Path(__file__).resolve().parents[1]/'results/tagged-relation-control-contract.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
