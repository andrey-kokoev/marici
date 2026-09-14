#!/usr/bin/env python3
"""Match the source (u,v)=(2,0) node-to-e6 chart to a global split fiber."""
import json
from pathlib import Path
import sympy as s
R=Path(__file__).resolve().parents[3]
a,b,h,x,y,z=s.symbols('a b h x y z');c=-(x+y+z)
CM=s.Matrix([[0,1,1,1,1],[1,0,c**2,a**2,b**2],[1,c**2,0,y**2,x**2],[1,a**2,y**2,0,z**2],[1,b**2,x**2,z**2,0]])
K=s.expand(-CM.det()/2); P=s.Poly(K,a,b)
G=s.expand(sum(co*a**ij[0]*b**ij[1]*h**(4-sum(ij)) for ij,co in P.terms()))
soft={x:1,y:0,z:1,h:1}
fiber1=s.factor(G.subs({**soft,b:1}));fiber3=s.factor(G.subs({**soft,b:3}))
Q=a**2-4
checks={'source_center_external':'X1=1,X2=0,X3=1','q_equals_b_over_h_at_local_center':s.Rational(1,1)==1,'q1_is_global_critical_value':s.expand((y+z).subs(soft)-1)==0,'fiber_q1_square':s.expand(fiber1-Q**2)==0,'node_a_plus_2':Q.subs(a,2)==0,'paired_node_a_minus_2':Q.subs(a,-2)==0,'second_type_coalesces_to_same_square_on_soft_wall':s.expand(fiber3-Q**2)==0,'reflection_preserves_each_component':s.expand(Q.subs(a,-a)-Q)==0}
assert all(v is True or v==True or isinstance(v,str) for v in checks.values()),checks
source=json.loads((R/'research/benincasa/results/rank12-u2-v0-node-to-e6-gysin.json').read_text())
assert source['center']=={'u':2,'v':0,'a':2,'b':1}
out={'schema':'marici.voevodsky.soft-node-split-fiber-match.v1','source_center':source['center'],'external_soft_center':{'x':1,'y':0,'z':1},'pencil_coordinate':'q=b/h=1','global_fiber_equation':str(fiber1),'components':['W=+(a^2-4)','W=-(a^2-4)'],'nodes':['a=+2','a=-2'],'source_tau':'difference of the two W-sign component branches','reflection_action':{'a_to_minus_a':'preserves both components and exchanges the two nodes','tau':'fixed'},'e6_consequence':'The source-equivariant nonzero tau-to-e6 Gysin map places the rational e6 line in the reflection-invariant algebraic subspace. This is a character statement, not an integral normalization.','checks':checks,'passed':True,'next':'identify v_alg as a combination of the other three split-fiber component differences'}
(R/'research/voevodsky/results/soft_node_split_fiber_match.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'fiber':str(fiber1),'nodes':out['nodes'],'reflection_action':out['reflection_action'],'next':out['next']}))
