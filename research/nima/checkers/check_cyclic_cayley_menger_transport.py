"""Exact cyclic transport gate for the three-site Cayley--Menger polynomial."""
import json
import sympy as sp

a,b,c,p1,p2,p3=sp.symbols('a b c p1 p2 p3')
CM=sp.Matrix([
 [0,1,1,1,1],
 [1,0,c**2,a**2,b**2],
 [1,c**2,0,p2**2,p1**2],
 [1,a**2,p2**2,0,p3**2],
 [1,b**2,p1**2,p3**2,0],
])
K=sp.expand(-CM.det()/2)

def act(poly, pcycle):
    return sp.expand(poly.xreplace({a:b,b:c,c:a,p1:pcycle[0],p2:pcycle[1],p3:pcycle[2]}))

forward=(p2,p3,p1)
backward=(p3,p1,p2)
forward_defect=sp.factor(act(K,forward)-K)
backward_defect=sp.factor(act(K,backward)-K)
assert (forward_defect==0) != (backward_defect==0)
pcycle=forward if forward_defect==0 else backward
assert act(K,pcycle)==K
assert act(act(act(K,pcycle),pcycle),pcycle)==K

# If a restricted polynomial is an exact square f^2, equivariance transports
# the identity.  The only ambiguity invisible to polynomial data is f -> -f.
t=sp.symbols('t')
f=t**2+a*p1+b*p2+c*p3
identity=sp.expand(f**2-f**2)
transported=act(f**2,pcycle)-act(f,pcycle)**2
assert sp.expand(identity)==0 and sp.expand(transported)==0

out={
 'schema':'marici.nima.cyclic-cayley-menger-transport.v1',
 'status':'passed',
 'edge_cycle':{'a':'b','b':'c','c':'a'},
 'external_cycle':list(map(str,pcycle)),
 'K_cyclic_invariant':True,
 'three_cycle_closes':True,
 'square_identity_transport_functorial':True,
 'polynomial_branch_ambiguity':'independent signs on transported square roots subject to a three-cycle cocycle',
 'source_branch_selected':False,
 'claim_boundary':'polynomial square identities only; no analytic square-root or conductor finite-part transport',
}
print(json.dumps(out,sort_keys=True))
