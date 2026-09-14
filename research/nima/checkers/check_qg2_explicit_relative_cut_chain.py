"""Construct the affine endpoint-to-conductor relative chain on the qg2 wall."""
import json
import sympy as s
t,k=s.symbols('t k');xi=-1+t*(1-k)
assert s.simplify(xi.subs(t,0)+1)==0
assert s.simplify(xi.subs(t,1)+k)==0
sol_endpoint=s.solve(s.Eq(xi,-1),t);sol_conductor=s.solve(s.Eq(xi,-k),t)
assert sol_endpoint==[0] and sol_conductor==[1]
reversed=s.simplify(xi.subs(t,1-t));assert s.simplify(reversed-(-k+t*(k-1)))==0
out={'schema':'marici.nima.qg2-explicit-relative-cut-chain.v1','status':'relative_chain_constructed_for_kappa_not_equal_one',
'chain':'xi(t)=-1+t(1-kappa), 0<=t<=1','boundary':'[-kappa]-[-1]',
'interior_avoids_endpoint_poles':'for kappa!=1, xi(t)=-1 only at t=0 and xi(t)=-kappa only at t=1',
'reversal':'xi(1-t) traverses conductor to endpoint and negates the oriented chain',
'physical_wall':'normalized qg2 wall with poles xi=-1 and xi=-kappa',
'scope_boundary':'ambient nearby-cycle/tubular transport remains open'}
open('research/nima/results/qg2-explicit-relative-cut-chain.json','w').write(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
