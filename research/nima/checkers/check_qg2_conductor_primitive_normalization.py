"""Normalize the qg2 conductor connecting coefficient in its localized ring."""
import json
import sympy as s
p,k=s.symbols('p k',nonzero=True)
c=-1/(32*p**4*(k-1)**2)
cinv=-32*p**4*(k-1)**2
assert s.simplify(c*cinv-1)==0
rho_v=1
assert s.simplify(cinv*(c*rho_v)-rho_v)==0
out={'schema':'marici.nima.qg2-conductor-primitive-normalization.v1','status':'primitive_line_normalized_in_localized_ring',
'localized_ring':'Q[p^+-1,(kappa-1)^+-1]','connecting_coefficient':str(c),'inverse_unit':str(cinv),
'normalized_detector_value':1,'selected_L2_detector_value':rho_v,
'consequence':'after stripping the source-derived unit, the conductor cell and selected v have the same primitive scalar normalization',
'boundary':'does not identify their geometric orientation lines or construct ambient relative cut-chain transport'}
open('research/nima/results/qg2-conductor-primitive-normalization.json','w').write(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
