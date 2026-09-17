#!/usr/bin/env python3
"""Compute tail and residual budgets for dangerous finite eigenvectors."""
import json,math
from pathlib import Path
L=.55;C=3.5526025323746278;N=1000;delta=.5*math.log1p(math.sqrt(N*(N+1))/L)-C;eigs=[2.6067399753945213e-8,7.004931468091266e-6,0.0007006860077334116,0.03711902607460704];budgets=[math.sqrt(x*delta) for x in eigs]
out={'schema':'marici.voevodsky.rank1000-dangerous-residual-budgets.v1','tail_start_degree':N,'certified_coarse_tail_margin':delta,'finite_eigenvalues':eigs,'maximum_residual_norms_for_scalar_closure':budgets,'first_residual_target':budgets[0],'second_residual_target':budgets[1],'criterion':'lambda_i-||Q A v_i||^2/delta > 0','passed':delta>0,'rh_proved':False};p=Path(__file__).parents[1]/'results'/'rank1000_dangerous_residual_budgets.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
