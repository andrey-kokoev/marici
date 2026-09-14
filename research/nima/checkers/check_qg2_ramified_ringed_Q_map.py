"""Construct the exact quadratic ramified Q-algebra carrying conductor branches."""
import json
import sympy as s
x,k,p,xi,d=s.symbols('x k p xi d');a=p-x*(k/s.Integer(2)-1)
K=s.expand(a**4-8*a**2*k*p**2*xi-10*a**2*p**2+16*k**2*p**4+40*k*p**4*xi+16*p**4*xi**2+9*p**4)
P=s.Poly(K,xi);A,B,C=P.all_coeffs();disc=s.factor(B**2-4*A*C)
root_plus=s.cancel((-B+d)/(2*A));root_minus=s.cancel((-B-d)/(2*A))
def mod_cover(expr):return s.factor(s.rem(s.together(expr).as_numer_denom()[0],s.Poly(d**2-disc,d),d))
assert mod_cover(K.subs(xi,root_plus))==0
assert s.simplify(root_plus.subs(d,-d)-root_minus)==0
assert A==16*p**4
out={'schema':'marici.nima.qg2-ramified-ringed-Q-map.v1','status':'exact_quadratic_Q_algebra_map_constructed',
'base_ring':'Q[p^+-1,(kappa^2-1)^+-1,x]','cover_ring':'base[d]/(d^2-Disc_xi(K_qg2))',
'quadratic_leading_coefficient':str(A),'discriminant':str(disc),
'conductor_branches':'xi_+-=(-B+-d)/(2A)','verification':'K(xi_+-)=0 modulo d^2-Disc',
'deck_involution':'d -> -d exchanges xi_+ and xi_-','filtration':'Disc has x-order one, so d has half x-order; after x=h^2 use integral h-order',
'boundary':'identify this algebraic nearby-cycle branch module with the literal physical filtered Q target and its road boundary functor'}
open('research/nima/results/qg2-ramified-ringed-Q-map.json','w').write(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
