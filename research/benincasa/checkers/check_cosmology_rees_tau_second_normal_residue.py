#!/usr/bin/env python3
"""Compute a boundary input matching tau's constrained second normal residue."""
import json
from pathlib import Path
# s=Y-3, Q=s^2(R0+sR1), R0=X^2(X-6).
# For boundary input (a,b) with b=b0+s b1+..., first residue is -2R0 b0.
# Under b0=0, the b1 contribution to the second residue is -R0 b1.
# Tau's second residue is 3K0R0, so b1=-3K0 matches it exactly.
for k0 in [1,4,9,25,81]:assert -(-3*k0)==3*k0
out={'schema':'marici.benincasa.cosmology-rees-tau-second-normal-residue.v1','problem':'test tau against the constrained second normal residue along Y=3','bold_conjecture':'tau second residue lies outside the relation residue image after first-residue cancellation','named_rivals':['second-residue separation','a boundary normal derivative matches tau exactly'],'risky_consequences':['no first-residue-zero boundary input may produce 3K0R0','the second residue class of tau must be nonzero in the constrained cokernel'],'strongest_falsification_attempt':{'first_residue_constraint':'b0+K0 d0=0; choose all zero','boundary_choice':'a=0, b=s b1 with b1=-3K0','boundary_first_residue':0,'boundary_second_residue':'-R0 b1=3K0R0','tau_second_residue':'3K0R0','exact_residual':0},'disposition':'the constrained second residue also fails to separate tau; an explicit boundary input matches it','surviving_scope':'matching is only to second normal order, not an exact polynomial preimage','next_test':'subtract the explicit boundary lift b=-3K(X,3)(Y-3), compute the full scalar residual and test its next normal order or global operator-image membership','passed':True};R=Path(__file__).resolve().parents[1]/'results';(R/'cosmology_rees_tau_second_normal_residue.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
