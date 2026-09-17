#!/usr/bin/env python3
import json
from pathlib import Path
root=Path(__file__).parents[1]/'results';rows=[]
for a in range(0,128,32):rows+=json.loads((root/f'gate3_E10_pivot17_derivative_chunk_{a}_{a+32}_h1e-06.json').read_text())['rows']
mx=max(x['derivative_abs'] for x in rows);h=1e-6;r=1e-5;M=1.;trunc=4*M*(h/r)**4;evalerr=2.139131310747118e-9;derr=1.5*evalerr/h;total=mx+trunc+derr;out={'schema':'marici.voevodsky.gate3-E10-pivot17-derivative-h1e6.v1','nodes':128,'step':h,'maximum_observed_derivative':mx,'cauchy_truncation_bound':trunc,'per_evaluation_error':evalerr,'differentiated_evaluation_error':derr,'total_derivative_bound':total,'required_bound':.04188,'passed_conditionally':total<.04188,'passed':False,'conditions':['radius-1e-5 analytic disks and |p17|<=1','strong-block Frobenius evaluation error <=2.14e-9'],'rh_proved':False};p=root/'gate3_E10_pivot17_derivative_h1e6.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_conditionally']
