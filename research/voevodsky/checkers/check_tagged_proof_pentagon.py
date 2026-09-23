"""Four-leaf formal associator pentagon; maps commute, histories differ."""
from fractions import Fraction as Q
from pathlib import Path
import json
root=('x-low','x-high','y-low','y-high')
proofs={'a':(Q(1),Q(2),Q(0),Q(0)),'b':(Q(0),Q(0),Q(1),Q(2)),
        'c':(Q(0),Q(1),Q(0),Q(0)),'d':(Q(0),Q(0),Q(0),Q(1))}
def leaves(tree):return (tree,) if isinstance(tree,str) else leaves(tree[0])+leaves(tree[1])
def packet(tree):
 ids=leaves(tree);return tuple(sum((proofs[x][i] for x in ids),Q(0)) for i in range(4))
def rotate(tree,path=()):
 if not path:
  left,z=tree;x,y=left;return (x,(y,z))
 head,*tail=path;assert head in (0,1)
 q=list(tree);q[head]=rotate(q[head],tuple(tail));return tuple(q)
def supported(tree,roots):
 if tuple(roots)!=root:raise PermissionError('MISSING_PRIMITIVE_ROOT')
 ids=leaves(tree)
 if len(ids)!=len(set(ids)) or any(x not in proofs for x in ids):raise ValueError('BAD_LEAF_PROVENANCE')
 return True
start=((('a','b'),'c'),'d');goal=('a',('b',('c','d')))
assert supported(start,root)
short1=rotate(start);short2=rotate(short1)
long1=rotate(start,(0,));long2=rotate(long1);long3=rotate(long2,(1,))
assert short1==(('a','b'),('c','d')) and short2==goal
assert long3==goal and long1!=short1 and long2!=short2
assert all(packet(t)==packet(goal) for t in (start,short1,short2,long1,long2,long3))
assert leaves(start)==leaves(goal)==('a','b','c','d')
short_steps=((),());long_steps=((0,),(),(1,));assert short_steps!=long_steps
try:supported(start,root[:-1])
except PermissionError:missing_refused=True
else:raise AssertionError('missing root')
try:supported(((('a','a'),'c'),'d'),root)
except ValueError:duplicate_refused=True
else:raise AssertionError('duplicate leaf ids')
report={'passed':True,'four_leaf_associator_short_steps':2,'four_leaf_associator_long_steps':3,'same_labelled_goal':True,'same_packet_tip':list(map(str,packet(goal))),'different_associator_histories':True,'missing_root_refused':missing_refused,'duplicate_leaf_id_refused':duplicate_refused,'scope':'Formal leaf-preserving associator of four tagged Farkas proofs on fixed primitive square. Pentagon equality as functions of tree labels; NOT equality of 2-cell path histories or independently sourced higher coherence.'}
out=Path(__file__).resolve().parents[1]/'results/tagged-proof-pentagon.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
