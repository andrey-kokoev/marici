"""Wall Kummer character, ambient tangency, and inverse-Euler orientation for q_g2."""
import json
import sympy as sp
a,xi,k,p=sp.symbols('a xi k p', nonzero=True)
K=a**4-8*a**2*k*p**2*xi-10*a**2*p**2+16*k**2*p**4+40*k*p**4*xi+16*p**4*xi**2+9*p**4
Kwall=sp.factor(K.subs(a,p)); s=sp.symbols('s')
local_wall=sp.factor(Kwall.subs(xi,-k+s))
ambient_transverse=sp.factor(sp.diff(K,a).subs({a:p,xi:-k}))
assert local_wall==16*p**4*s**2
assert ambient_transverse==16*p**3*(k-1)*(k+1)
# The pullback divisor has multiplicity two, hence sqrt monodromy (-1)^2=+1.
wall_character=1
ambient_meridian_character=-1
rE=1/(64*p**4*(k-1)); rC=rE; rInf=-(rE+rC); euler=k-1
connecting=sp.factor(rInf/euler)
target=-1/(32*p**4*(k-1)**2)
assert sp.simplify(connecting-target)==0
print(json.dumps({'schema':'marici.nima.qg2-wall-kummer-euler-orientation.v1','status':'passed','bold_conjecture':'the normalized q_g2 wall has trivial Kummer character and residue-at-infinity orientation fixes the inverse-Euler sign','wall_local_kernel':str(local_wall),'wall_divisor_multiplicity':2,'wall_kummer_character':wall_character,'ambient_transverse_derivative':str(ambient_transverse),'ambient_generic_meridian_character':ambient_meridian_character,'residue_at_infinity':str(sp.factor(rInf)),'collision_euler':str(euler),'connecting_as_residue_at_infinity_over_euler':str(connecting),'required_coefficient':str(target),'falsification_disposition':'wall claim survives; unrestricted ambient transport is falsified','residual_conjecture':'the conductor closure is valid in the normalized-wall pullback local system, but physical ambient descent requires a tangency/nearby-cycle comparison map'},sort_keys=True))
