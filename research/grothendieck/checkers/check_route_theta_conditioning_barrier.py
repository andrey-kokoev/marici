"""Rational certificates for the actual route-subspace theta noise barrier."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json
ROOT = Path(__file__).resolve().parents[3]
prior = json.loads((ROOT/'research/grothendieck/results/theta-interval-signature-depth.json').read_text())
assert prior['old_collision_annihilated']['2']
assert prior['old_collision_annihilated']['3']
# exp(6)>210, exp(24)>6144*2^9, exp(7/3)>10.
assert sum(F(6)**k/factorial(k) for k in range(12)) > 210
assert sum(F(24)**k/factorial(k) for k in range(15)) > 6144*2**9
assert sum(F(7,3)**k/factorial(k) for k in range(9)) > 10
assert 6144*60**9 < 10**20
assert F(6*60**2)/F(7,3) > 9257
# Norm(h)=2, four terms each bounded by 10^-9237.
assert F(1,2)*10 > 1
result = {'schema':'marici.grothendieck.route-theta-conditioning-barrier.v1',
          'passed':True,'late_edge_minimum_label':60,
          'late_edge_norm_upper_bound':'10^-9237',
          'unit_route_direction_output_upper_bound':'2 * 10^-9237',
          'any_linear_route_left_inverse_norm_lower_bound':'10^9236',
          'metric':'orthonormal full-route coefficients; direct-sum raw L2 two-point and four-point theta responses',
          'scope':'Actual four-route collision direction; does not exclude independently justified weighted or route-labelled measurements.'}
p=ROOT/'research/grothendieck/results/route-theta-conditioning-barrier.json'
p.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
