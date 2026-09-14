#!/usr/bin/env python3
"""Restrict the exact degree-17 odd numerator to moving physical endpoint faces."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'))
import sympy as s
exact=json.loads((ROOT/'research/benincasa/results/G12_exact_weighted_overlap_reconstruction.json').read_text());data=json.loads((ROOT/'research/benincasa/results/cleared-relative-shape-jet.json').read_text());a,b,c,t=s.symbols('a b c t');L={'a':a,'b':b,'c':c};q=[b+c+1,a+c+1,b+c+2,a+c+2];N=s.expand(s.sympify(data['terms']['G12_g23']['cleared_numerator'],locals=L)*q[3]**3-s.sympify(data['terms']['G12_g31']['cleared_numerator'],locals=L)*q[2]**3)
faces={'c=0':{c:0,a:1-t,b:1+t},'a=0':{a:0,c:1-t,b:1},'b=0':{b:0,c:1+t,a:1}}
rows=[]
for name,sub in faces.items():
 z=s.factor(N.subs(sub));poly=s.Poly(z,t);order=min(e[0] for e,x in poly.terms()) if z else None;lead=s.expand(z).coeff(t,order) if z else 0
 rows.append({'face':name,'restriction':s.sstr(z),'vanishing_order':order,'leading_coefficient':str(lead),'second_order_coefficient':str(s.expand(z).coeff(t,2))})
checks={'exact_solution_available':exact['resolution']=='++','central_restrictions_zero':all(s.expand(N.subs({k:v.subs(t,0) if hasattr(v,'subs') else v for k,v in sub.items()}))==0 for sub in faces.values()),'c_face_order_five':rows[0]['vanishing_order']==5,'a_b_faces_order_two':rows[1]['vanishing_order']==rows[2]['vanishing_order']==2,'opposite_nonzero_second_boundary_terms':int(rows[1]['second_order_coefficient'])==-int(rows[2]['second_order_coefficient'])!=0}
assert all(checks.values()),checks
out={'schema':'marici.benincasa.VC2g1-degree17-signed-minor-restrictions.v1','prospective_action':'VC2g1_signed_minor_boundary_restrictions_on_degree17_solution','physical_shape_family':'P1=1+t, P2=1-t, P3=1','moving_endpoint_substitutions':{k:{str(x):str(y) for x,y in v.items()} for k,v in faces.items()},'restrictions':rows,'resolution':'-+','reason':'All central endpoint restrictions vanish, but the a=0 and b=0 moving signed-minor faces have opposite nonzero t^2 coefficients. Therefore the second-shape operation has a surviving relative-boundary term; affine no-new-support is insufficient for physical descent.','interface_added':'degree17_boundary_obstruction','interface_withheld':'support_boundary_admissible','next':'Either include these two endpoint terms in an enlarged relative totalization or reject the degree-17 Bezout representative as a physical lowering.','checks':checks,'passed':True};p=ROOT/'research/benincasa/results/VC2g1_degree17_signed_minor_restrictions.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'resolution':'-+','orders':[r['vanishing_order'] for r in rows],'second':[r['second_order_coefficient'] for r in rows]}))
