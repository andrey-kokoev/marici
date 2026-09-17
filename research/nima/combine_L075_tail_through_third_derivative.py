#!/usr/bin/env python3
"""Add the directed third-derivative jump tail to the L=.75 completion ledger."""
import json,re
from decimal import Decimal,getcontext
from pathlib import Path
getcontext().prec=50
ROOT=Path(__file__).resolve().parents[2];V=ROOT/'research/voevodsky/results';N=ROOT/'research/nima/results'
def load(n):return json.loads((V/n).read_text())
def upper(s):
 m=re.fullmatch(r'\[([^ ]+) \+/- ([^\]]+)\]',s);assert m,s
 return Decimal(m.group(1))+Decimal(m.group(2))
base=load('L075_directed_tail_component_ledger.json');third=load('L075_directed_third_derivative_jump_tail.json');tol=load('L075_infinite_residual_tail_tolerance.json')
third_upper=upper(third['total_bound']);used=Decimal(str(base['triangle_sum_bound']))+third_upper;allow=Decimal(str(tol['maximum_orthogonal_tail_norm']));reserve=allow-used
finite=Decimal(str(tol['directed_modes_below_1000_norm_upper']));total_if=(finite*finite+used*used).sqrt();maximum=Decimal(str(tol['maximum_total_residual_for_positivity']))
checks={'third_derivative_tail_directed':third['passed'],'four_components_below_tail_allowance':used<allow,'conditional_total_below_positive_threshold':total_if<maximum,'four_times_continuous_and_analytic_remainder_certified':False}
out={'schema':'marici.nima.L075-tail-through-third-derivative.v1','directed_components':{**base['directed_components'],'third_derivative_jumps':str(third_upper)},'triangle_sum_upper':str(used),'tail_allowance':str(allow),'reserve_for_four_times_continuous_and_analytic_remainder':str(reserve),'total_residual_if_remaining_remainder_zero':str(total_if),'maximum_total_residual':str(maximum),'checks':checks,'finite_components_passed':all(v for k,v in checks.items() if k!='four_times_continuous_and_analytic_remainder_certified'),'full_tail_passed':all(checks.values()),'next_obligation':'directed joint norm bound <= reserve for the four-times-continuous prime remainder plus analytic gamma and endpoint rows','rh_proved':False,'passed':all(v for k,v in checks.items() if k!='four_times_continuous_and_analytic_remainder_certified')}
p=N/'L075-tail-through-third-derivative.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
