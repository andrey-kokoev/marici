"""Generic zero-column-3 iterated cyclic residue equals retained-eight top form."""
from pathlib import Path
import json
import sympy as s
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
x,y,alpha,beta=s.symbols('x y alpha beta');S,T=s.symbols('S T')
# Gauge physical columns 1 and 4 to e1,e2. Column 2=(x,y),
# disappearing column 3=(alpha,beta). Retained-eight cyclic edge 24=x.
d23=s.expand(x*beta-y*alpha);d34=alpha;d24=x
assert s.det(s.Matrix([[s.diff(d34,z) for z in (alpha,beta)],
                       [s.diff(d23,z) for z in (alpha,beta)]]))==x
inverse={alpha:S,beta:(T+y*S)/x}
assert s.simplify(d34.subs(inverse)-S)==0 and s.simplify(d23.subs(inverse)-T)==0
jac=s.det(s.Matrix([[s.diff(inverse[z],t) for t in (S,T)] for z in (alpha,beta)]));assert jac==1/x
# Shared cyclic factors and unaffected twelve source coordinates cancel.
# Compare full nine-column d(alpha) d(beta) / (Delta23 Delta34)
# to retained-eight top form multiplied by 1/(S T Delta24).
ratio=s.factor((jac/(S*T))/(1/(d24*S*T)))
assert ratio==1
# Swapping residue order reverses oriented wedge; omitting retained
# adjacency Delta24 leaves the invalid nonconstant factor 1/x.
assert s.det(s.Matrix([[s.diff(d23,z) for z in (alpha,beta)],
                       [s.diff(d34,z) for z in (alpha,beta)]]))==-x
assert jac!=1
result={'schema':'marici.nima.nine-point-zero-column-residue.v1','passed':True,
 'gauge':'C1=e1,C4=e2,C2=(x,y),C3=(alpha,beta), x!=0',
 'normal_coordinates':['S=Delta34=alpha','T=Delta23=x*beta-y*alpha'],
 'retained_replacement_edge':'Delta24=x',
 'oriented_residue_ratio_to_eight_column_top_form':'1',
 'swapped_normal_order_sign':'-1',
 'scope':'Generic algebraic source-form normalization for deleting column 3. Does not push forward the eight-column four-pair form or identify a physical history.'}
(OUT/'nine-point-zero-column-residue.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
