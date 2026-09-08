"""Exact charts of the image-line small resolution."""
import json
from pathlib import Path
from sympy import symbols,Matrix,simplify
p=json.loads(Path('research/nima/results/punctured_face_gluing.json').read_text());assert p['status']=='passed'
t,x,y,s,u,v=symbols('t x y s u v')
W0=Matrix([[x,y],[t*x,t*y]]);W1=Matrix([[s*u,s*v],[u,v]])
assert W0.det()==W1.det()==0
assert (W1.subs({s:1/t,u:t*x,v:t*y})-W0).applyfunc(simplify)==Matrix.zeros(2)
assert simplify((1/s).subs(s,1/t)-t)==0
assert W0.subs({x:0,y:0})==W1.subs({u:0,v:0})==Matrix.zeros(2)
# Wrong fiber transition would not glue the incidence matrix.
assert (W1.subs({s:1/t,u:x,v:y})-W0).applyfunc(simplify)!=Matrix.zeros(2)
# Tangent map on the exceptional curve: two independent fiber directions.
J=Matrix(list(W0)).jacobian([t,x,y]);assert J.subs({x:0,y:0}).rank()==2
r={'status':'passed','charts':'W0=[[x,y],[tx,ty]]; W1=[[su,sv],[u,v]]','transition':'s=1/t,u=tx,v=ty','exceptional_fiber':'P1','exceptional_normal_bundle':'O(-1) plus O(-1)','exceptional_tangent_map_rank':2,'wrong_transition_rejected':True,'scope':'Chart identities checked symbolically; properness, smoothness and nontrivial tautological line follow from the packet construction.'}
Path('research/nima/results/projective_factor_resolution.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r))
