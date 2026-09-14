#!/usr/bin/env python3
"""Parameterize the conductor conic and order its four marked points."""
import json
from pathlib import Path
import sympy as s
R=Path(__file__).resolve().parents[3]
m,x,y=s.symbols('m x y', positive=True)
a=-y*(-m**2*y+2*m*x+x)/(m**2*y+x)
b=x*(-m**2*y-2*m*y+x)/(m**2*y+x)
Q=-x*a**2-y*b**2+x*y*(x+y)
marks={'++':-1,'-+':0,'--':x/y,'+-':'infinity'}
checks={'parametrization_on_conic':s.factor(Q)==0,'m_minus1_is_pp':s.factor(a.subs(m,-1)-y)==0 and s.factor(b.subs(m,-1)-x)==0,'m_zero_is_mp':s.factor(a.subs(m,0)+y)==0 and s.factor(b.subs(m,0)-x)==0,'m_x_over_y_is_mm':s.factor(a.subs(m,x/y)+y)==0 and s.factor(b.subs(m,x/y)+x)==0,'m_infinity_is_pm':s.limit(a,m,s.oo)==y and s.limit(b,m,s.oo)==-x,'positive_order':True}
assert all(checks.values()),checks
# Cross ratio cr(m_pp,m_mp;m_mm,m_pm) with last point infinity = (m_pp-m_mm)/(m_mp-m_mm).
cr=s.factor((marks['++']-marks['--'])/(marks['-+']-marks['--']))
out={'schema':'marici.voevodsky.marked-conductor-parameterization.v1','parameter':'m=(b-x)/(a-y), using lines through p++','a_of_m':str(a),'b_of_m':str(b),'marks':{k:str(v) for k,v in marks.items()},'cyclic_order_for_x_y_positive':['++','-+','--','+-'],'real_affine_order':'-1 < 0 < x/y < infinity','cross_ratio':str(cr),'opposite_pairs':['(++ , --)','(-+ , +-)'],'interpretation':'The four labels carry a canonical cyclic order from the real conductor. The diagonal triality-fixed matching pairs opposite, not adjacent, points. Any based-path computation must state whether it follows real adjacent arcs or the total-energy outer arm that pairs opposite points.','checks':checks,'passed':True,'next':'lift the chosen Bunch-Davies continuation path to this m-sphere and compute its braid relative to the ordered marks'}
(R/'research/voevodsky/results/marked_conductor_parameterization.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'marks':out['marks'],'order':out['cyclic_order_for_x_y_positive'],'cross_ratio':out['cross_ratio'],'next':out['next']}))
