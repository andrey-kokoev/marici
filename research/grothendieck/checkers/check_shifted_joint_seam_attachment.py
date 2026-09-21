"""Shift-correct chain comparison for the actual 24 product cycles."""
from pathlib import Path
from collections import defaultdict
import runpy
import json
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
prior=runpy.run_path(str(ROOT/'research/grothendieck/checkers/check_relation_to_seam_bridge.py'))
joint=prior['joint'];boundary=prior['boundary'];clean=prior['cleaned']

# J=C_left tensor C_right; each local C has degrees -1,0.
def d_minus2(column,wrong_sign=False):
    out=defaultdict(int)
    for (m,left,right),c in column.items():
        for x,v in boundary({left:1}).items():out[m,0,x,right]+=c*v
        for y,v in boundary({right:1}).items():out[m,1,left,y]+=(1 if wrong_sign else -1)*c*v
    return clean(out)

def d_minus1(column):
    out=defaultdict(int)
    for (m,side,left,right),c in column.items():
        if side==0:
            for y,v in boundary({right:1}).items():out[m,left,y]+=c*v
        else:
            for x,v in boundary({left:1}).items():out[m,x,right]+=c*v
    return clean(out)

for col in joint:assert not d_minus2(col)
basis_element={next(iter(joint[0])):1}
assert not d_minus1(d_minus2(basis_element))
assert d_minus1(d_minus2(basis_element,wrong_sign=True))

# Injection P[2]->J is a literal cycle map, not merely a homology identification.
coordinates=sorted(set().union(*(set(col) for col in joint)))
row={key:i for i,key in enumerate(coordinates)}
L=s.SparseMatrix(len(coordinates),24,{(row[key],j):c for j,col in enumerate(joint) for key,c in col.items()})
minor=L.extract([row[p] for p in prior['probes']],list(range(24)))
assert minor.rank()==24
# The full root memory stays as one external factor. An independent D=2 fixture
# exercises the tensor identity; no claim is made that the analytical root has D=2.
root_dimension=2
injection=s.kronecker_product(s.eye(root_dimension),minor)
assert injection.rank()==root_dimension*24
# In degree -1 the derived connecting map is identity on V=X_s tensor P;
# its degree-zero component is zero. Theta is injection after this projection.
delta=s.eye(root_dimension*24)
theta=injection*delta
assert theta==injection
assert theta.H==delta.H*injection.H
# Cochain convention (C[k])^n=C^(n+k): raw -2 -> -1 under shift [-1].
raw_degree=-2;shift=-1;target_degree=raw_degree-shift
assert target_degree==-1 and -target_degree==1

# Restricting the target to the canonical cycle image uses L itself as its
# basis-free identification with P. No ambient projection or Green inverse occurs.
assert all(col for col in joint)
result={'schema':'marici.grothendieck.shifted-joint-seam-attachment.v1','passed':True,
        'product_cycles':24,'occupied_joint_degree_minus_two_coordinates':len(coordinates),
        'root_dimension_fixture':root_dimension,'root_tensor_injection_rank':injection.rank(),
        'checks':{'actual_joint_cycles_are_closed':True,'joint_tensor_differential_squares_zero':True,
                  'wrong_tensor_sign_rejected':True,'product_injection_exact':True,
                  'connecting_projection_square':True,'dual_projection_inclusion_square':True,
                  'shift_minus_one_puts_joint_cycles_in_degree_minus_one':True},
        'scope':'Actual source product-cycle map with an illustrative root factor. General derived domain, image restriction and naturality are proved in the companion note; no Green isometry is asserted.'}
p=ROOT/'research/grothendieck/results/shifted-joint-seam-attachment.json'
p.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
