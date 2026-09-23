"""Typed source-rooted trace-cell boundaries; critical 4-cell is NOT admitted."""
from fractions import Fraction as Q
from pathlib import Path
import json
H=Q(1,2);O=Q(1)
root={'low':(-Q(1),Q(0)),'high':(Q(1),Q(1))}
def certificate(word,c=Q(2)):
 used=sum(word,Q(0));assert used<=c
 # Fixed source S=[0,1], initial proof (0,1,c) of x<=1+c.
 return (used,Q(1)+used,c-used)
def step(word,i,kind,roots):
 if set(roots)!=set(root) or roots!=root:raise PermissionError('MISSING_PRIMITIVE_BOUND')
 assert 0<=i<len(word)-1
 pair=word[i:i+2]
 if kind=='merge':assert pair==(H,H);out=word[:i]+(O,)+word[i+2:]
 elif kind=='swap':assert pair==(H,O);out=word[:i]+(O,H)+word[i+2:]
 else:raise ValueError('UNSUPPORTED_CELL')
 assert certificate(word)==certificate(out)
 return out
w=(H,H,O);assert certificate(w)==(Q(2),Q(3),Q(0))
left=step(w,0,'merge',root);left= (left,)
right=step(w,1,'swap',root);right=step(right,0,'swap',root);right=step(right,1,'merge',root)
assert left[0]==right==(O,O)
# The paths of proposed 3-cells differ, despite matching trace and proof tips.
left_path=(('merge',0),);right_path=(('swap',1),('swap',0),('merge',1))
assert left_path!=right_path
support={'primitive-low':(),'primitive-high':(),
 'merge':('primitive-low','primitive-high'),
 'swap':('primitive-low','primitive-high'),
 'left-path':('merge',), 'right-path':('swap','merge')}
def rooted(node,links,stack=()):
 if node in stack:return False
 if node in ('primitive-low','primitive-high'):return True
 return node in links and bool(links[node]) and all(rooted(x,links,stack+(node,)) for x in links[node])
assert rooted('left-path',support) and rooted('right-path',support)
cyclic={**support,'merge':('critical-filler',),'critical-filler':('merge',)}
assert not rooted('merge',cyclic)
try:step(w,0,'merge',{'low':root['low']})
except PermissionError:missing_bound_refused=True
else:raise AssertionError('source row omitted')
# No primitive construction of a 4-cell comparing left_path and right_path.
def admit_filler(packet):
 if packet['boundary']!=(left_path,right_path):return 'wrong_boundary'
 if 'constructor' not in packet or packet['constructor']=='self-asserted':return 'missing_source_4cell'
 return 'not_verified_by_this_gate'
assert admit_filler({'boundary':(left_path,right_path),'constructor':'self-asserted'})=='missing_source_4cell'
report={'passed':True,'critical_word':['1/2','1/2','1'],'left_trace':['1','1'],'right_trace':['1','1'],'left_3cell_path':[['merge',0]],'right_3cell_path':[['swap',1],['swap',0],['merge',1]],'source_rooted_boundaries':True,'missing_source_bound_refused':missing_bound_refused,'cyclic_support_refused':True,'critical_4cell_status':'missing_source_4cell','scope':'Fixed source interval and half-unit finite grammar. Equal trace/certificate tips do not supply a higher path-interchange constructor or analytic authority.'}
out=Path(__file__).resolve().parents[1]/'results/source-rooted-trace-cells.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
