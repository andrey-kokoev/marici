#!/usr/bin/env python3
"""Insertion/reflow mechanism across all seven degree shifts."""
import contextlib,io,json,runpy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
env={'__file__':str(ROOT/'research/nima/check_nnmhv_long_numeric_grade_selection.py')}
code=(ROOT/'research/nima/check_nnmhv_long_numeric_grade_selection.py').read_text().replace("raise SystemExit(0 if out['passed'] else 1)","")
with contextlib.redirect_stdout(io.StringIO()):exec(compile(code,env['__file__'],'exec'),env)
value,terminal_shell=env['value'],env['terminal_shell']
transitions={
 '-3_4to1':(4,1,lambda j:j**4+j+1,lambda j:2*j+1),
 '-2_3to1':(3,1,lambda j:j**3+j+1,lambda j:3*j+1),
 '-1_2to1':(2,1,lambda j:j*j+j+1,lambda j:4*j+1),
 '0_2to2':(2,2,lambda j:j*j+j+1,lambda j:j*j+3*j+1),
 '1_2to3':(2,3,lambda j:j*j+j+1,lambda j:j**3+2*j+1),
 '2_2to4':(2,4,lambda j:j*j+2*j+2,lambda j:j**4+j+1),
 '3_1to4':(1,4,lambda j:5*j+1,lambda j:j**4+2*j+1)}
rows={}
for name,(p,q,lf,tf) in transitions.items():
 samples=[]
 for n in (32,48,64):
  vn=value(n,lf,tf);inc=vn-value(n-1,lf,tf);term,_=terminal_shell(n,lf,tf);samples.append({'n':n,'net_increment':inc,'terminal_insertion':term,'prior_history_reflow':inc-term,'insertion_fraction':term/inc,'reflow_fraction':(inc-term)/inc})
 rows[name]={'delta':q-p,'p':p,'q':q,'samples':samples}
late=[v['samples'][-1] for v in rows.values()];negative=[r for k,r in rows.items() if r['delta']<0];positive=[r for k,r in rows.items() if r['delta']>0]
checks={'all_seven_shifts':sorted(r['delta'] for r in rows.values())==list(range(-3,4)),'all_values_finite':all(abs(s['net_increment'])<float('inf') for r in rows.values() for s in r['samples']),'negative_shifts_insertion_dominated':all(r['samples'][-1]['insertion_fraction']>0.5 for r in negative),'positive_shifts_reflow_dominated':all(r['samples'][-1]['reflow_fraction']>0.5 for r in positive)}
out={'schema':'marici.nima.nnmhv-seven-transition-flux.v1','transitions':rows,'checks':checks,'passed':all(checks.values()),'scope':'Double-precision supported-history evaluation at n=32,48,64 for one representative of every degree shift.'};p=ROOT/'research/nima/results/nnmhv-seven-transition-flux.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
