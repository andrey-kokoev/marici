#!/usr/bin/env python3
"""Construct the normalized reversal-invariant combination of the two local flags."""
import json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
r_vu=F(1,216);r_uv=F(0)
# Reversal invariance forces equal coefficients c on the two ordered flags.
# tau_p has coefficient 3 on the unit numerator, so 3*c*(r_vu+r_uv)=1.
c=1/(3*(r_vu+r_uv));assert c==72
unit=c*(r_vu+r_uv);tau=3*unit;assert unit==F(1,3) and tau==1
out={'schema':'marici.benincasa.cosmology-rees-symmetric-flag-residue.v1','local_flags':{'v_then_u':str(r_vu),'u_then_v':str(r_uv)},'symmetry_constraint':'equal coefficients on the two order-reversed flags','normalization_constraint':'tau_p=3 times the unit numerator must evaluate to 1','unique_coefficient':str(c),'normalized_unit_value':str(unit),'normalized_tau_value':str(tau),'result_strength':'unique normalized reversal-invariant functional in the two-flag span','not_verified':['invariance under replacing q3 by q1+q2 or duplicating q1 as q23','annihilation of K and q multiplication rows at every pole level','twisted-derivative adjoint equations'],'canonical_tau_functional_proved':False,'next_test':'evaluate this symmetric flag combination on exact assembled relation generators before any uniform promotion','passed':True};(R/'cosmology_rees_symmetric_flag_residue.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
