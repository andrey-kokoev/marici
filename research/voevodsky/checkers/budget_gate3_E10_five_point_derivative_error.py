#!/usr/bin/env python3
"""Analytic truncation and evaluation-error budget for five-point E10 derivatives."""
import json
from pathlib import Path
h=5e-8;r=1e-5;M=1.;# Five-point first derivative error <= h^4 sup|f^(5)|/30; Cauchy gives 5! M/r^5.
trunc=4*M*(h/r)**4;eval_error=1e-9;# coefficient l1 of stencil / (12h) = 18/(12h)=1.5/h
eval_der=1.5*eval_error/h;observed=.010695654539106047;required=.04188;total=observed+trunc+eval_der
out={'schema':'marici.voevodsky.gate3-E10-five-point-derivative-error-budget.v1','step':h,'adopted_local_analytic_disk_radius':r,'adopted_pivot17_disk_magnitude_bound':M,'cauchy_five_point_truncation_bound':trunc,'adopted_per_evaluation_absolute_error':eval_error,'differentiated_evaluation_error':eval_der,'observed_half_step_derivative_max':observed,'total_derivative_bound':total,'required_derivative_bound':required,'passed_conditionally':total<required,'passed':False,'conditions':['pivots 0-16 are zero-free on every radius-1e-5 disk about E10','|pivot17|<=1 on those disks','source block and recursive elimination evaluation absolute error <=1e-9'],'rh_proved':False};p=Path(__file__).parents[1]/'results'/'gate3_E10_five_point_derivative_error_budget.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_conditionally']
