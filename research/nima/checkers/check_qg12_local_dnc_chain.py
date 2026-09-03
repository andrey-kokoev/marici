"""First-jet DNC test for the q_g1/q_g2 relative face and collision locus."""
import json
import sympy as sp
x,xi,k,a,p=sp.symbols('x xi k a p')
# Independent strict-transform wall coordinates on the exceptional surface.
u=xi+1; v=a-p
J_strict=sp.Matrix([[sp.diff(u,xi),sp.diff(u,a)],[sp.diff(v,xi),sp.diff(v,a)]])
# Unresolved original exceptional/collision equations.
f=x*(xi+1); g=x*(k-1)
J_collision=sp.Matrix([[sp.diff(f,x),sp.diff(f,xi),sp.diff(f,k)],[sp.diff(g,x),sp.diff(g,xi),sp.diff(g,k)]])
J_exceptional=J_collision.subs(x,0)
J_collision_node=J_exceptional.subs({xi:-1,k:1})
required=-1/(32*p**4*(k-1)**2)
assert J_strict.det()==1
assert J_exceptional.rank()==1
assert J_collision_node.rank()==0
assert sp.simplify(required-1)!=0 and sp.simplify(required+1)!=0
print(json.dumps({'schema':'marici.nima.qg12-local-dnc-chain.v1','status':'passed','bold_conjecture':'local DNC first-jet data constructs both the ordered face Gamma and its required rational boundary coefficient','strict_transform_conormal_determinant':str(J_strict.det()),'collision_conormal_generic_exceptional_rank':J_exceptional.rank(),'collision_conormal_rank_at_endpoint_collision':J_collision_node.rank(),'required_boundary_coefficient':str(required),'conjecture_disposition':'falsified','surviving_scope':'strict-transform normals construct an oriented unweighted local face generator away from the collision, but collision conormals lose rank and first-jet incidence does not determine the rational coefficient','residual_conjecture':'the chain generator and coefficient have different sources: DNC incidence supplies Gamma, while a lower-point factorization or physical relative-chain map must supply its coefficient'},sort_keys=True))
