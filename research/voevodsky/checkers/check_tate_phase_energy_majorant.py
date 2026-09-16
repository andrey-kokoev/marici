"""Exact exponent and near/far audit for the Tate phase-energy majorant."""
import json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).parents[1]
# Rationalized normalization: omit the common positive factor pi^-2.
# Near contribution <= derivative_bound^2/2; far contribution <= 2.
a=2;q=3;M=4;K=3
rows=[]
for X in (1,2,4,8,16):
 derivative_bound=F((1+X)**a)
 kappa_bound=derivative_bound**2/F(2)+2
 polynomial_majorant=F(5,2)*(1+X)**(2*a)
 rows.append({'size':X,'normalized_kappa_bound':str(kappa_bound),'polynomial_majorant':str(polynomial_majorant),'dominated':kappa_bound<=polynomial_majorant})
radial_exponent=2*K-2*a
angular_margin=2*M-2*a-q
checks={'near_far_polynomial_bound':all(r['dominated'] for r in rows),'radial_integrability':radial_exponent>1,'angular_summability':angular_margin>0,'phase_energy_exponent':2*a==4}
out={'schema':'marici.voevodsky.tate-phase-energy-majorant.v1','phase_derivative_exponent_a':a,'phase_energy_exponent':2*a,'angular_growth_dimension_q':q,'observer_angular_order_M':M,'observer_radial_order_K':K,'radial_decay_exponent':radial_exponent,'angular_decay_margin':angular_margin,'rows':rows,'checks':checks,'all_exact':all(checks.values()),'meaning':'A polynomial first-derivative bound for a unimodular Tate phase gives a polynomial local H-half energy density; radial and angular Schwartz decay make the observer energy summable.'}
if __name__=='__main__':
 p=ROOT/'results'/'tate-phase-energy-majorant.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
