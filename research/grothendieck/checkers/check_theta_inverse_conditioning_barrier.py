"""Exact constants for an analytic theta-column norm upper bound."""
from fractions import Fraction as F
from math import factorial, prod
from pathlib import Path
import json
labels = sorted(2*prod(p for j,p in enumerate((2,3,5,7)) if m>>j & 1) for m in range(16))
a,b = labels[-2:]
assert (a,b) == (210,420)
# exp(7/3)>10 implies log(10)<7/3; exp(1)>2 implies log(2)<1.
assert sum(F(7,3)**k/factorial(k) for k in range(9)) > 10
assert sum(F(1,factorial(k)) for k in range(4)) > 2
assert 1024*a**9 < 10**24
assert 12*a*a-9 > 1
power = F(6*a*a)/F(7,3)
assert power.denominator == 1
exponent = int(power)-24
assert exponent == 113376
result = {'schema':'marici.grothendieck.theta-inverse-conditioning-barrier.v1',
          'passed':True,'last_interval_endpoints':[a,b],
          'column_norm_strict_upper_bound':f'10^-{exponent}',
          'full_coefficient_left_inverse_norm_strict_lower_bound':f'10^{exponent}',
          'metric':'Euclidean unweighted interval coefficients to raw L2 half-line theta history',
          'scope':'Exact rational constants for displayed analytic estimate; not a lower bound for every selected route decoder or every weighted metric.'}
p = Path(__file__).resolve().parents[1]/'results/theta-inverse-conditioning-barrier.json'
p.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
