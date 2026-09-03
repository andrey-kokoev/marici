#!/usr/bin/env python3
"""DPC test of C2 plus corner normalization for the absolute torsor connection."""
import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/benincasa';R=B/'results'
a=json.loads((B/'bivariate_soft_gram_connection.json').read_text());q=json.loads((B/'marked-wall-quotient-connection.json').read_text());torsor=json.loads((R/'cyclic_leray_transition_torsor.json').read_text());prior=json.loads((R/'cosmology_cyclic_Leray_torsor_horizontal_comparison.json').read_text());assert prior['passed'] and torsor['C2']=='-1/8'
u=Fraction(1);v=Fraction(3);D=4*u**4-4*u**3*v+4*u**3+4*u**2*v-7*u**2+2*u*v-4*u+v**2-4*v+4
E6u=(-8*u**3+6*u**2*v-6*u**2-4*u*v+7*u-v+2)/D;E6v=(2*u**3-2*u**2-u-v+2)/D
Qtu=-2*(u-1)/(u*(u-2));Qtv=-1/(v-2);assert (E6u-Qtu,E6v-Qtv)==(Fraction(-1,2),Fraction(1,2))
out={'schema':'marici.benincasa.cosmology-C2-corner-connection-normalization.v1','conjecture':'C2 normalization and the E6 v-connection equality at u=0 fix the torsor connection','risky_consequence':'the full bivariate E6 and q_top scalar connection forms must agree','falsifier':'evaluate both du and dv coefficients at a regular off-corner point','test_point':{'u':1,'v':3},'E6_coefficients':{'du':str(E6u),'dv':str(E6v)},'qtop_coefficients':{'du':str(Qtu),'dv':str(Qtv)},'connection_residual':{'du':str(E6u-Qtu),'dv':str(E6v-Qtv)},'residual_nonzero':True,'corner_v_equality_survives':True,'C2_transition_normalization_survives':True,'conjecture_disposition':'falsified','structural_reason':'C2 fixes a transition-difference class and the corner fixes one tangential pullback; neither fixes the transverse bivariate connection','independent_kernel_shift':'adding the closed regular form du preserves every transition difference and pulls back to zero on u=0','horizontal_comparison_verified':False,'next_test':'factor the full E6-minus-qtop diagonal residual and classify its vanishing pullback loci','passed':True};(R/'cosmology_C2_corner_connection_normalization.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
