#!/usr/bin/env python3
"""Exact two-ruling polarization law on the rank-one transport quadric."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'))
import sympy as s
u0,u1,v0,v1,du0,du1,dv0,dv1,e,f=s.symbols('u0 u1 v0 v1 du0 du1 dv0 dv1 e f');u=s.Matrix([u0,u1]);du=s.Matrix([du0,du1]);v=s.Matrix([[v0,v1]]);dv=s.Matrix([[dv0,dv1]])
M=u*v;image_ruling=(u+e*du)*v;covector_ruling=u*(v+f*dv);mixed=(u+e*du)*(v+f*dv);linear_sum=M+e*du*v+f*u*dv
wedge_u=u0*du1-u1*du0;wedge_v=v0*dv1-v1*dv0
checks={'base_rank_one_quadric':s.expand(M.det())==0,'image_ruling_stays_on_quadric':s.expand(image_ruling.det())==0,'kernel_ruling_stays_on_quadric':s.expand(covector_ruling.det())==0,'factorized_mixed_family_stays_on_quadric':s.expand(mixed.det())==0,'linearized_two_channel_departure_is_bilinear':s.factor(linear_sum.det()+e*f*wedge_u*wedge_v)==0,'no_pure_channel_normal_curvature':s.expand(linear_sum.det()).coeff(e,2)==0 and s.expand(linear_sum.det()).coeff(f,2)==0}
out={'schema':'marici.nima.segre-ruling-polarity-law.v1','identity':'det(u v^T + e du v^T + f u dv^T) = -e f (u wedge du)(v wedge dv)','channels':{'image_ruling':'du v^T: vary image, hold covector/kernel','kernel_ruling':'u dv^T: vary covector/kernel, hold image'},'checks':checks,'passed':all(checks.values()),'interpretation':'The rank-one boundary has exactly two intrinsic tangent polarities. Each alone remains on det=0; only their mixed incidence probes the normal determinant direction. Naming them insertion and reflow requires a source-derived orientation map.'};p=ROOT/'research/nima/results/segre-ruling-polarity-law.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
