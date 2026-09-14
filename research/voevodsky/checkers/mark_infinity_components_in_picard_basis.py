#!/usr/bin/env python3
"""Place a split bitangent pair in an adapted Bl_7(P2) Picard marking."""
import json, math
from pathlib import Path
R=Path(__file__).resolve().parents[3]
# Coordinates H,E1,...,E7 with intersection diag(1,-1,...,-1).
K=[-3]+[1]*7; anti=[3]+[-1]*7
Cplus=[0]*8;Cplus[7]=1
Cminus=[anti[i]-Cplus[i] for i in range(8)]
d=[Cminus[i]-Cplus[i] for i in range(8)]
def dot(u,v):return u[0]*v[0]-sum(u[i]*v[i] for i in range(1,8))
def add(u,v):return [a+b for a,b in zip(u,v)]
checks={'pair_sums_to_anticanonical':add(Cplus,Cminus)==anti,'Cplus_minus_one':dot(Cplus,Cplus)==-1,'Cminus_minus_one':dot(Cminus,Cminus)==-1,'each_anticanonical_degree_one':dot(anti,Cplus)==dot(anti,Cminus)==1,'components_meet_twice':dot(Cplus,Cminus)==2,'difference_square_minus_six':dot(d,d)==-6,'difference_K_perpendicular':dot(d,K)==0,'difference_primitive':math.gcd(*map(abs,d))==1,'difference_mod2_equals_anticanonical':all((d[i]-anti[i])%2==0 for i in range(8))}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.infinity-component-picard-marking.v1','basis':['H']+[f'E{i}' for i in range(1,8)],'intersection_form':'diag(1,-1^7)','canonical_class':K,'anticanonical_class':anti,'adapted_marking':{'C_plus':'E7','C_minus':'3H-E1-E2-E3-E4-E5-E6-2E7'},'vectors':{'C_plus':Cplus,'C_minus':Cminus,'e6_Betti=C_minus-C_plus':d},'intersections':{'C_plus^2':-1,'C_minus^2':-1,'C_plus.C_minus':2,'e6_Betti^2':-6,'K.e6_Betti':0},'mod_two_identity':'e6_Betti congruent -K_S mod 2 in Pic(S)','marking_scope':'Any chosen component may be sent to E7 by the Weyl group. This is an adapted integral marking, canonical up to the stabilizer of the bitangent pair.','checks':checks,'passed':True}
(R/'research/voevodsky/results/infinity_component_picard_marking.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'marking':out['adapted_marking'],'e6_vector':d,'intersections':out['intersections'],'mod2':out['mod_two_identity'],'scope':out['marking_scope']}))
