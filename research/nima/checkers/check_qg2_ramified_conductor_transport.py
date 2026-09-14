"""Audit the higher-order conductor face along the qg2 strict transform."""
import json
import sympy as s
r,h,k,p,xi,c=s.symbols('r h k p xi c');a=p-r*(k/s.Integer(2)-1)
K=s.expand(a**4-8*a**2*k*p**2*xi-10*a**2*p**2+16*k**2*p**4+40*k*p**4*xi+16*p**4*xi**2+9*p**4)
disc=s.factor(s.discriminant(K,xi))
assert s.factor(disc/r).subs(r,0)!=0
Kr=s.expand(K.subs({r:h**2,xi:-k+c*h}));lead=s.factor(Kr.coeff(h,2))
assert s.simplify(lead-8*p**3*(2*c**2*p-(k-2)*(k-1)*(k+1)))==0
c2=s.factor((k-2)*(k-1)*(k+1)/(2*p))
assert s.simplify(lead.subs(c**2,c2))==0
out={'schema':'marici.nima.qg2-ramified-conductor-transport.v1','status':'ambient_conductor_requires_square_root_base_change',
'discriminant':str(disc),'generic_order_in_x':1,'ordinary_x_collar':'conductor root has Puiseux order sqrt(x)',
'ramified_base_change':'x=h^2','branch_expansion':'xi=-kappa+c h+O(h^2)',
'leading_branch_law':'c^2=(kappa-2)(kappa-1)(kappa+1)/(2p)',
'monodromy':'h -> -h exchanges branches and supplies sign character -1',
'consequence':'ambient ramification, not trivial wall Kummer character, canonically supplies the odd orientation needed by the log primitive'}
open('research/nima/results/qg2-ramified-conductor-transport.json','w').write(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
