#!/usr/bin/env python3
"""VC2m1: test incidence of signed-minor axes with the marked-corner blowup center."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'))
import sympy as s
near=json.loads((ROOT/'research/benincasa/et-cut-nearby-normal-form.json').read_text());a,b,x,y=s.symbols('a b x y', positive=True)
# Blowup center is a=y,b=x. Add each axis ideal and eliminate a,b.
Ga=s.groebner([a,a-y,b-x],a,b,x,y);Gb=s.groebner([b,a-y,b-x],a,b,x,y)
checks={'center_typed':near['physical_real_corner'].startswith('(a,b)=(y,x)'),'a_axis_center_ideal_contains_y':any(p.as_expr()==y or p.as_expr()==-y for p in Ga.polys),'b_axis_center_ideal_contains_x':any(p.as_expr()==x or p.as_expr()==-x for p in Gb.polys),'physical_parameters_strictly_positive':all(z.is_positive for z in (x,y))}
assert all(checks.values()),checks
out={'schema':'marici.benincasa.VC2m1-axis-exceptional-incidence.v1','prospective_action':'VC2m1_axis_exceptional_incidence','blowup_center_ideal':'(E, a-y, b-x)','axis_tests':{'a=0':'intersection forces y=0','b=0':'intersection forces x=0'},'physical_parameter_domain':'x>0,y>0','incidence':{'a_axis':False,'b_axis':False},'resolution':'-+','reason':'Neither signed-minor axis meets the marked-corner blowup center for physical x,y>0; consequently their strict transforms have no points on this exceptional divisor.','parent_aggregation':'VC2m=-+ by frozen hard-failure short circuit','invalidated_descendants':['VC2m2_exceptional_point_identification','VC2m3_local_multiplicity','VC2m4_orientation','VC2m5_exchange_equivariance','VC2m6_integral_image_and_gluing'],'consequence':'The degree-17 endpoint correction cannot be transported through the available E=0 marked-corner exceptional chart.','checks':checks,'passed':True};p=ROOT/'research/benincasa/results/VC2m1_axis_exceptional_incidence.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'resolution':'-+','incidence':out['incidence'],'parent':'-+'}))
