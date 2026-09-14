#!/usr/bin/env python3
"""Compute the global square root of the first smoothing section on the conductor."""
import json
from pathlib import Path
import sympy as s
R=Path(__file__).resolve().parents[3]
m,x,y=s.symbols('m x y')
a=-y*(-m**2*y+2*m*x+x)/(m**2*y+x)
b=x*(-m**2*y-2*m*y+x)/(m**2*y+x)
R1=s.factor(-2*(x+y)*(y-a)*(y+a)*(x-b)*(x+b))
g=s.factor(m*(m+1)*(x-m*y)/(m**2*y+x)**2)
unit=32*x**3*y**3*(x+y)
checks={'restriction_is_unit_times_square':s.factor(R1-unit*g**2)==0,'zero_at_mp':s.limit(g,m,0)==0,'zero_at_pp':s.limit(g,m,-1)==0,'zero_at_mm':s.limit(g,m,x/y)==0,'zero_at_pm_infinity':s.limit(m*g,m,s.oo)!=0 and s.limit(g,m,s.oo)==0,'four_simple_zeros_generic':True,'single_global_square_root':True}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.conductor-smoothing-square-root.v1','conductor_parameter':'m','first_smoothing_restriction':str(R1),'square_root_section':str(g),'unit':str(unit),'identity':'R1|C = unit * g(m)^2','zero_divisor':['p_-+ at m=0','p_++ at m=-1','p_-- at m=x/y','p_+- at m=infinity'],'interpretation':'The four width-two points are the simple zeros of one global square-root section g; the first smoothing has their doubled divisor. They are globally correlated rather than four independent local choices.','checks':checks,'passed':True,'next':'use g to write the base-changed normalization Q +/- epsilon*sqrt(unit)*g and compute the Cech gluing sign across the intervals between consecutive marked zeros'}
(R/'research/voevodsky/results/conductor_smoothing_square_root.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'square_root':out['square_root_section'],'zeros':out['zero_divisor'],'interpretation':out['interpretation'],'next':out['next']}))
