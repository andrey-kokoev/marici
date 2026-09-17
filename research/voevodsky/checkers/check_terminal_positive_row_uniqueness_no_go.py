#!/usr/bin/env python3
"""Exact polarization/trace no-go for an ordinary terminal positive pro-row."""
import json,sys
from pathlib import Path
try: import sympy as s
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import sympy as s
# A Hermitian difference D whose quadratic form vanishes on polarization probes.
a,d,b,c=s.symbols('a d b c', real=True);D=s.Matrix([[a,b+s.I*c],[b-s.I*c,d]]);probes=[s.Matrix([1,0]),s.Matrix([0,1]),s.Matrix([1,1]),s.Matrix([1,s.I])];eq=[s.expand((v.conjugate().T*D*v)[0]) for v in probes];sol=s.solve(eq,[a,b,c,d],dict=True);L,g=s.symbols('L g',positive=True);lp=L/s.pi+s.sin(2*L*g)/(2*s.pi*g);lm=L/s.pi-s.sin(2*L*g)/(2*s.pi*g);trace=s.simplify(lp+lm);checks={'polarization_forces_zero_difference':sol==[{a:0,b:0,c:0,d:0}],'eigenvalue_sum_is_2L_over_pi':trace==2*L/s.pi,'trace_diverges':s.limit(trace,L,s.oo)==s.oo};out={'schema':'marici.voevodsky.terminal-positive-row-uniqueness-no-go.v1','polarization_equations':[str(x) for x in eq],'solution':[{str(k):str(v) for k,v in x.items()} for x in sol],'trace':str(trace),'checks':checks,'passed':all(checks.values()),'conclusion':'Exact source-faithful positivity uniquely fixes P_{gamma,L}; its trace norm 2L/pi forbids a uniformly trace-class ordinary positive pro-row.','required_reformulation':'relative positive pair or rigged/source-graph topology with new four-face compatibility proof','rh_proved':False};p=Path(__file__).parents[1]/'results'/'terminal_positive_row_uniqueness_no_go.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']
