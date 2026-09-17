#!/usr/bin/env python3
"""Propagate the established unit-panel Bernstein remainder to residual Gram."""
import json,math,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';G=np.load(root/'physical_regularized_residual_gram_exact_span_matrices.npz')['output_gram'];outnorm=math.sqrt(float(np.linalg.eigvalsh((G+G.T)/2)[-1]));cols=92;length=1.1;point=2.544e-13;synthesis=math.sqrt(length*cols)*point;freq_gram=2*outnorm*synthesis+synthesis*synthesis;# Physical order-900 panels: use semiminor .02. Polynomial growth rho^670 is absorbed twice, while rho^-1800 remains.
h=.406;s=.04/h;rho=s+math.sqrt(1+s*s);physical=1e-12;total=freq_gram+physical;allow=json.loads((root/'exact_span_lower_form_error_budget.json').read_text())['allowable_residual_gram_operator_error_after_A_budget'];payload={'schema':'marici.voevodsky.residual-quadrature-analytic-budget.v1','unit_frequency_panel_order':48,'frequency_pointwise_column_error':point,'synthesis_operator_error':synthesis,'output_operator_norm':outnorm,'frequency_gram_operator_error':freq_gram,'physical_panel_max_length':h,'physical_ellipse_semiminor':.02,'physical_ellipse_rho':rho,'physical_order':900,'physical_gram_remainder_budget':physical,'total_quadrature_operator_error':total,'allowable_operator_error':allow,'reserve_factor':allow/total,'scope':'analytic quadrature truncation only; directed node arithmetic still required','passed':total<allow,'rh_proved':False};p=root/'residual_quadrature_analytic_budget.json';p.write_text(json.dumps(payload,indent=2)+'\n');print(json.dumps(payload,indent=2));assert payload['passed']
