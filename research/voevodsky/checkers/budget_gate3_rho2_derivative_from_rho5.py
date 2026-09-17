#!/usr/bin/env python3
"""Cauchy derivative target transferring a rho5 scalar bound to the rho2 contour."""
import json,math
from pathlib import Path
root=Path(__file__).parents[1]/'results';r2=json.loads((root/'rho2_recursive_schur_invertibility_128.json').read_text());center=.6495;h=.0005
def axes(r):return h*(r+r**-1)/2,h*(r-r**-1)/2
a2,b2=axes(2);a5,b5=axes(5);sep=min(a5-a2,b5-b2);M=4e-8;der=M/sep;variation=der*r2['half_chord'];floor=r2['robust_scalar_schur_min_sampled_abs']-variation;out={'schema':'marici.voevodsky.gate3-rho2-derivative-from-rho5.v1','rho2_rho5_minimum_L_separation':sep,'required_directed_rho5_robust_scalar_bound':M,'cauchy_derivative_bound_on_rho2':der,'rho2_half_chord_128':r2['half_chord'],'arc_variation_bound':variation,'rho2_sampled_robust_scalar_floor':r2['robust_scalar_schur_min_sampled_abs'],'conditional_covered_robust_scalar_floor':floor,'passed_conditionally':floor>0,'passed':False,'remaining':'directed full-boundary rho5 robust scalar bound <=4e-8 and rho5 strong-block no-pole certificate','rh_proved':False};p=root/'gate3_rho2_derivative_from_rho5.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_conditionally']
