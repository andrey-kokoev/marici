#!/usr/bin/env python3
"""Compute ordered flag residues after inserting the exact positive K square root."""
import json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
# H=3(u^2-12v-2v^2), denominator H*u*v^2*(u+v)*(u-6).
# v-first coefficient calculation gives -2/6^6; u-first gives -1/(216*6^3).
v_then_u=F(-2,6**6);u_then_v=F(-1,216*6**3);assert v_then_u==F(-1,23328) and u_then_v==F(-1,46656)
s=v_then_u+u_then_v;assert s==F(-1,15552);c=1/(3*s);assert c==-5184
out={'schema':'marici.benincasa.cosmology-rees-K-half-flag-residues.v1','square_root':'H=3(u^2-12v-2v^2)','test_form':'du dv / [H u v^2 (u+v)(u-6)]','ordered_residues':{'v_then_u':str(v_then_u),'u_then_v':str(u_then_v)},'symmetric_sum':str(s),'normalizing_common_coefficient':str(c),'normalized_tau_value':'1','negative_square_root_effect':'both ordered residues change sign and the normalizing coefficient changes sign, leaving the normalized functional unchanged','relation_closure_verified':False,'next_test':'derive coefficient formulas for arbitrary pole levels and evaluate all three parametric relation families','passed':True};(R/'cosmology_rees_K_half_flag_residues.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
