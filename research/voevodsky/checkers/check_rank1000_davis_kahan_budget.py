#!/usr/bin/env python3
"""Davis--Kahan budget for the first dangerous rank-1000 eigenvector."""
import json
from pathlib import Path
entry=3.2254342166297763e-13;n=1000;eps=n*entry;lam1=2.6067399753945213e-8;lam2=7.004931468091266e-6;gap=lam2-lam1;angle=eps/(gap-eps);cross=.2708532639661398;residual_perturb=cross*angle;finite_residual=2.6006767471288582e-6;budget=7.233397108631436e-5;reserve=budget-finite_residual-residual_perturb
out={'schema':'marici.voevodsky.rank1000-davis-kahan-budget.v1','matrix_error_norm':eps,'first_spectral_gap':gap,'sine_angle_upper':angle,'cross_norm_upper_used':cross,'residual_perturbation':residual_perturb,'finite_residual_1000_1999':finite_residual,'first_residual_budget':budget,'remaining_reserve_before_modes_ge_2000':reserve,'passed':reserve>0,'rh_proved':False};p=Path(__file__).parents[1]/'results'/'rank1000_davis_kahan_budget.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']
