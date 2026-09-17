#!/usr/bin/env python3
"""Tail budget for the order-six jets used by the rank-two Taylor cell."""
import json,math
from pathlib import Path
U=50.;N=50000.;V=math.log(N);t=.05
def gamma_tail(k):
 e=math.exp(-t*U*U);I=e/(2*t*U)
 for m in range(2,2*k+3,2):I=U**(m-1)*e/(2*t)+(m-1)*I/(2*t)
 return I/(2*math.pi)
def prime_tail(k):
 # Coarse uniform Laguerre bound for k<=6.
 y=V*V/(4*t);C=100.;single=C*V/math.sqrt(N)*math.exp(-y)*(1+y)**k
 g=C*V*(1+y)**k;base=math.exp(V/2-y);rate=(V-t)/(2*t)-(2*k+1)/V
 return math.factorial(k)*(single+g*base/rate)/(2*math.sqrt(math.pi)*t**(k+.5))
tails=[gamma_tail(k)+prime_tail(k) for k in range(1,7)];mx=max(tails)
# The determinant Taylor polynomial has degree two in moments. Use the actual
# Arb enclosure maximum, inflated by two; coefficient sum 20 dominates every
# displayed derivative polynomial through D3 and quadratic tail terms.
budget=2*cell['moment_absolute_upper'] if False else None
# cell is loaded immediately below; compute after loading.
cell=json.loads((Path(__file__).parents[1]/'results'/'rank_two_second_order_cell.json').read_text());budget=2*cell['moment_absolute_upper'];poly_error=20*budget*mx+20*mx*mx;complete=cell['Taylor_lower']-poly_error
out={'schema':'marici.voevodsky.rank-two-second-order-cell-tails.v1','interval':cell['interval'],'moment_tail_bounds':tails,'maximum_moment_tail':mx,
 'polynomial_magnitude_budget':budget,'Taylor_perturbation_bound':poly_error,'finite_core_Taylor_lower':cell['Taylor_lower'],'complete_Taylor_lower':complete,
 'complete_cell_positive':complete>0,'lemmas':['|Re psi|<=u^2 beyond U','Lambda<=log n','|L_k^-1/2(y)|<=100(1+y)^k for k<=6','decreasing log-Gaussian integral test'],
 'passed':complete>0,'rh_proved':False,'scope':f"One complete rank-two cell {cell['interval']}."}
p=Path(__file__).parents[1]/'results'/'rank_two_second_order_cell_tails.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']
