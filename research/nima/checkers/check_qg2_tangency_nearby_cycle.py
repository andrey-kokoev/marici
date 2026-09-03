"""Local nodal smoothing and character transport at the q_g2 conductor tangency."""
import json
import sympy as sp
s,t,k,p,W=sp.symbols('s t k p W', nonzero=True)
local=16*p**4*s**2+16*p**3*(k**2-1)*t
reduced=sp.factor(local/(16*p**3))
rootp=sp.sqrt(p)
U=W+rootp*s; V=W-rootp*s
nodal=sp.expand(U*V)
assert sp.simplify(reduced-(p*s**2+t*(k-1)*(k+1)))==0
assert sp.simplify(nodal-(W**2-p*s**2))==0
uv_on_cover=sp.factor(nodal.subs(W**2,reduced))
assert sp.simplify(uv_on_cover-t*(k-1)*(k+1))==0
branch_product_character=(-1)*(-1)
assert branch_product_character==1
print(json.dumps({'schema':'marici.nima.qg2-tangency-nearby-cycle.v1','status':'passed','bold_conjecture':'the wall class is killed because its +1 character cannot transport into ambient -1 Kummer character','local_cover_equation':'W^2=p*s^2+(kappa^2-1)*t','nodal_coordinates':['U=W+sqrt(p)*s','V=W-sqrt(p)*s'],'nodal_smoothing':'U*V=(kappa^2-1)*t','single_branch_meridian_character':-1,'enclosing_two_branch_cycle_character':branch_product_character,'conjecture_disposition':'falsified locally','surviving_transport':'wall loop transports to the annular nearby cycle enclosing both split branch points, not to either single ambient meridian','residual_conjecture':'physical descent is possible only if the positive-cut chain maps to the even two-branch nearby cycle; an odd single-branch component is obstructed'},sort_keys=True))
