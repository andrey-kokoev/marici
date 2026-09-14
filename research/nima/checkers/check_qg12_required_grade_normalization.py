"""Derive the unique scalar needed for qg1/qg2 node residue cancellation."""
import json,sympy as s
p,k=s.symbols('p k',nonzero=True)
r_g1=-(k-3)/(64*p**4*(k-1)**2)
r_g2=-1/(16*p**3*(k-1)**2)
N=s.factor(-r_g1/r_g2)
assert s.simplify(N+(k-3)/(4*p))==0
assert s.simplify(r_g1+N*r_g2)==0
out={'schema':'marici.nima.qg12-required-grade-normalization.v1','status':'necessary_coefficient_derived_not_source_authorized',
'qg1_collision_residue':str(r_g1),'qg2_endpoint_residue':str(r_g2),
'unique_opposite-residue_normalization':str(N),'normalized_sum':0,
'valuation':'one inverse power of p plus kappa-dependent factor',
'warning':'derived from desired node cancellation; must be independently recovered from parent normal Jacobian/regulator chain'}
open('research/nima/results/qg12-required-grade-normalization.json','w').write(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
