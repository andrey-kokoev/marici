#!/usr/bin/env python3
"""Set a sufficient entrywise interval radius for the rank-80 certificate."""
import json
from decimal import Decimal,getcontext
from pathlib import Path
getcontext().prec=50
n=Decimal(80);lambda_scout=Decimal('2.6581585527296743e-8');entry_radius=Decimal('1e-10');operator_error=n*entry_radius;remaining=lambda_scout-operator_error
out={'schema':'marici.voevodsky.two-prime-interval-error-budget.v1','dimension':80,'center_smallest_eigenvalue':str(lambda_scout),'uniform_entry_radius_target':str(entry_radius),'frobenius_operator_error_upper':str(operator_error),'resulting_eigenvalue_lower_target':str(remaining),'component_entry_radius_budgets':{'finite_gamma_quadrature':'2e-11','physical_prime_overlaps':'2e-11','endpoint_matrix':'1e-11','structured_gamma_tail':'5e-11'},'criterion':'For a symmetric error matrix with every entry radius <= eps, ||E||_2 <= ||E||_F <= n*eps.','budget_closes_against_center':remaining>0,'passed':remaining>0,'rh_proved':False}
p=Path(__file__).parents[1]/'results'/'two_prime_interval_error_budget.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
