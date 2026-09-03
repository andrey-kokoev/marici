#!/usr/bin/env python3
"""Verify the local cosmology wall chart is an ordered etale A3 normal model."""
import json
from pathlib import Path
P=Path(__file__).resolve();ROOT=P.parents[3];R=ROOT/'research';B=R/'benincasa'/'results';V=R/'voevodsky'/'results'
protocol=json.loads((V/'cosmology_rank26_p_normal_protocol_gate.json').read_text());theorem=json.loads((V/'cosmology_etale_linearized_carrier_theorem.json').read_text());x,y,z=protocol['test_point_xyz'];assert (x,y,z)==(3,6,-3)
# Coordinates are (u,v,s), where s moves kinematics along nx=(1,0,0).
center=(0,3,0);J=[[0,1,0],[1,0,-1],[1,1,0]]
det=(J[0][0]*(J[1][1]*J[2][2]-J[1][2]*J[2][1])-J[0][1]*(J[1][0]*J[2][2]-J[1][2]*J[2][0])+J[0][2]*(J[1][0]*J[2][1]-J[1][1]*J[2][0]));assert det==-1
# q1=v-y-z, q2=u-(x+s)-z, q3=u+v+z.
def q(U,V,S):return (V-y-z,U-(x+S)-z,U+V+z)
assert q(*center)==(0,0,0)
out={'schema':'marici.benincasa.cosmology-etale-horn-instantiation.v1','local_chart':{'coordinates':['u','v','s_nx'],'center':list(center),'ordered_walls':['q_g1','q_g2','q_g3'],'wall_map':['v-y-z','u-(x+s)-z','u+v+z'],'jacobian':J,'determinant':det,'etale':True,'orientation_sign':-1},'wall_identity':'p=-q_g1-q_g2+q_g3 with dp(nx)=1','theorem_applied':theorem['conclusion'],'local_integral_horn_instantiated':True,'cone_equation':'d Phi(Gamma)=(Xi,-sigma123)','scope':'the affine local A3 neighborhood of the marked center and its DNC','global_overlap_compatibility_verified':False,'decision':'The marked cosmology chart admits an explicit wall-preserving etale map to the ordered A3 normal model: its wall Jacobian has unit determinant -1. Universal Gamma therefore pulls back to an algebraic integral local horn. Global carrier extension remains separate.','next_gate':'test transition maps between all source charts for preservation of wall order, orientation, ratios, and the pulled-back Gamma','passed':True};(B/'cosmology_etale_horn_instantiation.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
