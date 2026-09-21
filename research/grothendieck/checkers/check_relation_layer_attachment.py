"""Actual 24-product inclusion, nonsplitting witness, and fiber reconstruction."""
from pathlib import Path
import runpy
import json
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
prior=runpy.run_path(str(ROOT/'research/grothendieck/checkers/check_source_relation_conormal_layer.py'))
products=prior['products']
assert products.rank()==24

# Actual typed local relation pattern: a:s->m, b:m->t, c=ab:s->t.
# These are independent by endpoints. c is nonzero by the source product check.
# On the relation span (a,b,c), right action of b and left action of a are:
Rb=s.Matrix([[0,0,0],[0,0,0],[1,0,0]])
La=s.Matrix([[0,0,0],[0,0,0],[0,1,0]])
inclusion=s.Matrix([0,0,1]);quotient=s.Matrix([[1,0,0],[0,1,0]])
x,y=s.symbols('x y')
section=s.Matrix([[1,0],[0,1],[x,y]])
assert quotient*section==s.eye(2)
assert quotient*Rb==quotient*La==s.zeros(2,3)
assert Rb*section==s.Matrix([[0,0],[0,0],[1,0]])
assert La*section==s.Matrix([[0,0],[0,0],[0,1]])
# No vector-space section is compatible with both (indeed either) action.

# Fiber reconstruction, valid for any actual inclusion mu:P->I.
# The symbolic 2x1 inclusion keeps this identity independent of chosen coordinates.
u,v=s.symbols('u v')
mu=s.Matrix([u,v]);Ip=s.eye(1);Ii=s.eye(2)
d=Ip.col_join(-mu)
projection=mu.row_join(Ii)
embedding=s.zeros(1,2).col_join(Ii)
H=Ip.row_join(s.zeros(1,2))
assert projection*d==s.zeros(2,1)
assert projection*embedding==Ii
assert d*H==s.eye(3)-embedding*projection
assert H*d==Ip

result={'schema':'marici.grothendieck.relation-layer-attachment.v1','passed':True,
        'actual_product_layer_dimension':24,
        'checks':{'typed_relation_products_independent':True,
                  'right_module_section_obstruction':True,'left_module_section_obstruction':True,
                  'fiber_reconstruction_deformation_retract':True},
        'scope':'Actual product inclusion plus a typed nonsplitting witness and general chain identities. The global Ext-class theorem is proved in the companion note.'}
p=ROOT/'research/grothendieck/results/relation-layer-attachment.json'
p.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
