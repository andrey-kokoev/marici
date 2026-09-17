#!/usr/bin/env python3
"""Combine all fixed-window lower-form perturbation budgets."""
import json
from pathlib import Path
root=Path(__file__).parents[1]/'results'
def load(n):return json.loads((root/n).read_text())
a=load('exact_span_lower_form_error_budget.json');q=load('residual_quadrature_analytic_budget.json');r=load('residual_physical_roundoff_budget.json');margin=a['floating_margin'];alpha=.5897761979384148;residual_error=q['total_quadrature_operator_error']+r['total_physical_roundoff_operator_error'];lower_error=a['lower_form_error_from_A']+residual_error/alpha;cert=margin-lower_error
out={'schema':'marici.voevodsky.two-prime-fixed-window-combined-budget.v1','window_half_length':.55,'floating_lower_margin':margin,'finite_operator_lower_form_error':a['lower_form_error_from_A'],'residual_quadrature_operator_error':q['total_quadrature_operator_error'],'residual_roundoff_operator_error':r['total_physical_roundoff_operator_error'],'tail_floor':alpha,'combined_lower_form_error':lower_error,'conditional_certified_lower_bound':cert,'conditions':['4096-ulp frequency special-function reserve and 64-ulp elementary-function reserve','six-rounding-per-degree Clenshaw forward-error model','physical Bernstein remainder allocation in residual_quadrature_analytic_budget.json'],'passed':cert>0,'rh_proved':False};p=root/'two_prime_fixed_window_combined_budget.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']
