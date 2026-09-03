"""Exact conductor connecting coefficient from the q_g2 subleading wall form."""
import json
import sympy as sp
xi,k,p=sp.symbols('xi k p', nonzero=True)
sub=(k**2+4*k*xi+2*k+2*xi**2+2*xi+1)/(64*p**4*(k-1)*(k+xi)**2*(xi+1))
r_endpoint=sp.factor(sp.residue(sub,xi,-1))
r_conductor=sp.factor(sp.residue(sub,xi,-k))
r_infinity=sp.factor(-r_endpoint-r_conductor)
collision_euler=k-1
connecting=sp.factor(-(r_endpoint+r_conductor)/collision_euler)
target=-1/(32*p**4*(k-1)**2)
assert r_endpoint==1/(64*p**4*(k-1))
assert r_conductor==r_endpoint
assert sp.simplify(connecting-target)==0
# Strongest character falsifier: the opposite Kummer sign would cancel instead.
twisted_opposite=sp.factor(-(r_endpoint-r_conductor)/collision_euler)
assert twisted_opposite==0
print(json.dumps({'schema':'marici.nima.qg2-conductor-connecting-morphism.v1','status':'passed','bold_conjecture':'the oriented finite-residue sum divided by the collision Euler factor supplies the missing Cech-face coefficient','endpoint_residue':str(r_endpoint),'conductor_residue':str(r_conductor),'infinity_residue':str(r_infinity),'collision_euler_factor':str(collision_euler),'connecting_coefficient':str(connecting),'required_coefficient':str(target),'strongest_falsifier_opposite_kummer_character':str(twisted_opposite),'falsification_disposition':'survives iff the exact-square wall normalization gives trivial relative Kummer character','residual_conjecture':'the grade -1 total complex closes through a conductor connecting map with trivial normalized-wall Kummer character; ambient transport must prove that character and the inverse Euler orientation'},sort_keys=True))
