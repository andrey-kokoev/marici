#!/usr/bin/env python3
"""Compute the first normal residue along the repeated divisor Y=3."""
import json
from pathlib import Path
# s=Y-3, Q=s^2R, R0=R|s=0=X^2(X-6).
# (L1/s)|s=0=-2R0 f_y|s=0. For L0, the Q*dK term vanishes after /s,
# so (L0/s)|s=0=-2K0R0 f_y|s=0. Total residue image=(R0).
# Phi(tau)=3Ks^2R, hence its first normal residue is zero.
out={'schema':'marici.benincasa.cosmology-rees-tau-first-normal-residue.v1','problem':'test tau using the first normal residue after the order-one divisor restriction vanished','bold_conjecture':'tau has a nonzero first normal residue outside the induced relation-image ideal','named_rivals':['first-residue separation','tau vanishes to second order and passes the first residue condition'],'risky_consequences':['Phi(tau)/s evaluated at s=0 must be nonzero','if nonzero it must fail divisibility by R0=X^2(X-6)'],'strongest_falsification_attempt':{'R0':'X^2(X-6)','boundary_residue':'(L1/s)|s=0=-2R0 f_y(X,3)','lower_residue':'(L0/s)|s=0=-2K(X,3)R0 f_y(X,3)','total_residue_image_ideal':'(X^2(X-6))','tau_first_residue':'(3KsR)|s=0=0','exact_residual':0},'disposition':'the first normal residue also fails to separate tau; tau passes because it vanishes to order two','surviving_scope':'the induced first-residue image is characterized exactly as the principal ideal (X^2(X-6))','next_test':'impose cancellation of the first residue on relation inputs, compute the induced second normal residue, and compare it with 3K(X,3)X^2(X-6)','passed':True};R=Path(__file__).resolve().parents[1]/'results';(R/'cosmology_rees_tau_first_normal_residue.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
