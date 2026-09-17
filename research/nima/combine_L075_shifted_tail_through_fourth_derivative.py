#!/usr/bin/env python3
"""Combine directed jet-sector tails after exact coupled extraction through degree 1498."""
import json,re
from decimal import Decimal,getcontext
from pathlib import Path
getcontext().prec=50;ROOT=Path(__file__).resolve().parents[2];V=ROOT/'research/voevodsky/results';N=ROOT/'research/nima/results'
def U(path,key):
 s=json.loads(path.read_text())[key];m=re.fullmatch(r'\[([^ ]+) \+/- ([^\]]+)\]',s);return Decimal(m.group(1))+Decimal(m.group(2))
items=[('value',V/'L075_directed_jump_tail_from1500.json','total_jump_tail_norm_bound'),('first',V/'L075_directed_derivative_jump_tail_from1500.json','total_derivative_jump_tail_bound'),('second',V/'L075_directed_second_derivative_jump_tail_from1500.json','total_bound'),('third',V/'L075_directed_third_derivative_jump_tail_from1500.json','total_bound'),('fourth',N/'L075-directed-fourth-derivative-jump-tail-from1500.json','total_bound')];bounds={n:U(p,k) for n,p,k in items};used=sum(bounds.values(),Decimal(0));orth=Decimal('3.9113363258636923300372722743512298156e-9');reserve=orth-used
out={'schema':'marici.nima.L075-shifted-tail-through-fourth-derivative.v1','exact_coupled_prefix':[1000,1500],'sector_bounds_from_1500':{k:str(v) for k,v in bounds.items()},'triangle_bound_from_1500':str(used),'orthogonal_allowance_from_1500':str(orth),'reserve_for_C5_and_analytic_rows':str(reserve),'passed_components':used<orth,'full_tail_passed':False,'next_obligation':'joint directed bound for the five-times-continuous prime remainder plus analytic gamma and endpoint rows below the remaining reserve','rh_proved':False,'passed':used<orth};p=N/'L075-shifted-tail-through-fourth-derivative.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
